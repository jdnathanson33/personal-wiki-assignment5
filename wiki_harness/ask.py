"""`wiki ask`: the RAG workflow for standalone, neutral, cited answers.

question -> retrieve passages from the ORIGINAL sources (vault/raw by default)
         -> number them [S1..Sk] with their path and section
         -> system prompt = instructions/wiki-instructions.md (research rules only;
            no persona, no chat history)
         -> local Gemma answers -> citation check -> display -> save evidence card
"""
from __future__ import annotations

import sys
from typing import Callable, Optional

from . import citations, records
from .config import Settings, read_instruction
from .ollama_client import OllamaClient
from .retrieval import Index


def _label(p) -> str:
    return f"{p.path} — {p.locator}"


def run_ask(settings: Settings, client: OllamaClient, question: str, k: Optional[int] = None,
            scope: str = "raw", out: Callable = print, test: Optional[dict] = None, stream: bool = True) -> dict:
    ctx = records.run_context(settings, client, "ask")
    k = k or settings.top_k
    idx = Index.load(settings.chunks_file, settings.embeddings_file)
    ret = idx.search(question, k=k, scope=scope, client=client, max_per_file=settings.max_per_file)

    # Fit passages into the context budget, highest-ranked first.
    shown, used = [], 0
    for r in ret["results"]:
        t = r["passage"].text
        if used + len(t) > settings.ask_context_chars and shown:
            break
        shown.append(r)
        used += len(t)
    labels = {f"S{i}": r for i, r in enumerate(shown, 1)}

    out(f"[ask · {ctx['execution']} · {client.model} · internet: {ctx['internet_at_run_time']}]")
    out(f"retrieval: {ret['method']}, scope={scope}, {len(shown)} passage(s)" + (f" — {ret['note']}" if ret["note"] else ""))
    for lab, r in labels.items():
        out(f"  [{lab}] {_label(r['passage'])}  (bm25 {r['bm25']}, cos {r['cosine']})")

    system = read_instruction(settings, "wiki-instructions.md")
    if not shown:
        answer, stats, model_called = ("INSUFFICIENT EVIDENCE: no passage in the local wiki matched the question.",
                                       {}, False)
        out("\n" + answer)
    else:
        blocks = "\n\n".join(f"[{lab}] ({_label(r['passage'])})\n{r['passage'].text}" for lab, r in labels.items())
        user = (f"Question: {question}\n\nSource passages:\n\n{blocks}\n\n"
                f"Answer the question using only these passages, citing them as [S1], [S2], ...")
        out("\nanswer:")
        res = client.chat([{"role": "system", "content": system}, {"role": "user", "content": user}],
                          temperature=settings.temperature["ask"],
                          on_token=(lambda t: (sys.stdout.write(t), sys.stdout.flush())) if stream else None,
                          max_tokens=450)
        answer, stats, model_called = res["text"], res["stats"], True
        if stream:
            out("")
        else:
            out(answer)

    chk = citations.check(answer, {lab: r["passage"].text for lab, r in labels.items()}, prefix="S")
    out("\ncitations:")
    for lab in chk["labels_used"] or []:
        if lab in labels:
            out(f"  [{lab}] {_label(labels[lab]['passage'])}")
    if chk["invalid_labels"]:
        out(f"  !! labels not among retrieved passages: {', '.join(chk['invalid_labels'])}")
    out(f"check: {chk['verdict']}"
        + (f"; numbers not found in cited passages: {chk['unsupported_numbers']}" if chk["unsupported_numbers"] else "")
        + (f"; {len(chk['uncited_sentences'])} uncited sentence(s)" if chk["uncited_sentences"] else ""))
    if stats:
        out(f"time: {stats['wall_seconds']}s total (load {stats['load_seconds']}s, prompt {stats['prompt_tokens']} tok "
            f"in {stats['prompt_seconds']}s, answer {stats['output_tokens']} tok at {stats['tokens_per_second']} tok/s)")

    record = {**ctx, "question": question, "test": test, "retrieval": {
        "method": ret["method"], "note": ret["note"], "scope": scope, "k": k,
        "max_bm25": ret.get("max_bm25"), "max_cosine": ret.get("max_cosine"),
        "passages": [{"label": lab, "id": r["passage"].id, "path": r["passage"].path, "locator": r["passage"].locator,
                      "bm25": r["bm25"], "cosine": r["cosine"], "rrf": r["rrf"], "matched_terms": r["matched_terms"],
                      "text": r["passage"].text} for lab, r in labels.items()]},
        "prompt": {"system_file": "instructions/wiki-instructions.md", "passage_chars": used,
                   "chat_history_included": False, "persona_included": False},
        "model_called": model_called, "answer": answer, "citation_check": chk, "stats": stats}
    name = records.stamp() + "-" + (test["id"] + "-" if test else "") + records.slug(question)
    path = records.save(settings.runs / "ask", name, record, render_card(record))
    out(f"saved: {settings.rel(path)} (+ .md evidence card)")
    return record


def render_card(r: dict) -> str:
    t = r.get("test") or {}
    L = [f"# Ask-mode evidence card{': ' + t['id'] if t else ''}", "",
         f"**Question:** {r['question']}", "",
         "| Field | Value |", "|---|---|",
         f"| Mode | ask (standalone; no chat history, no persona) |",
         f"| Execution | {r['execution']} |",
         f"| Model | `{r['model']}` ({r.get('model_parameter_size')}, {r.get('model_quantization')}, digest `{r.get('model_digest')}`) |",
         f"| Embedding model | `{r['embed_model']}` |",
         f"| Runtime | {r.get('runtime')} |",
         f"| Internet at run time | **{r['internet_at_run_time']}** |",
         f"| Timestamp | {r['timestamp']} |", ""]
    if t:
        L += ["## Expected (written before running)", "", f"- Type: {t.get('type')}",
              f"- Expected behavior: {t.get('expected_behavior')}",
              f"- Expected source(s): {', '.join('`' + s + '`' for s in t.get('expected_sources', [])) or '—'}"]
        for q in t.get("expected_passages", []):
            L.append(f"- Expected passage: “{q}”")
        L.append("")
    ret = r["retrieval"]
    L += [f"## Retrieved passages ({ret['method']}, scope `{ret['scope']}`, top {ret['k']})", ""]
    if ret.get("note"):
        L += [f"_Note: {ret['note']}_", ""]
    L += ["| Label | Source path | Location | BM25 | Cosine | Matched terms |", "|---|---|---|---|---|---|"]
    for p in ret["passages"]:
        L.append(f"| {p['label']} | `{p['path']}` | {p['locator']} | {p['bm25']} | {p['cosine']} | "
                 f"{', '.join(p['matched_terms'][:8])} |")
    L.append("")
    for p in ret["passages"]:
        body = p["text"].replace("\n", "\n> ")
        L += [f"<details><summary>{p['label']} — {p['path']} — {p['locator']}</summary>", "", f"> {body}", "",
              "</details>", ""]
    L += ["## Actual Gemma answer", "", "```text", r["answer"], "```", ""]
    chk = r["citation_check"]
    L += ["## Citations", ""]
    lab2p = {p["label"]: p for p in ret["passages"]}
    for lab in chk["labels_used"]:
        p = lab2p.get(lab)
        L.append(f"- [{lab}] → " + (f"`{p['path']}` — {p['locator']}" if p else "**not a retrieved passage**"))
    if not chk["labels_used"]:
        L.append("- (none)")
    L += ["", "## Automatic citation check", "", f"- Verdict: **{chk['verdict']}**"]
    if chk["unsupported_numbers"]:
        L.append(f"- Numbers not found in the cited passages: {chk['unsupported_numbers']}")
    if chk["uncited_sentences"]:
        L.append(f"- Uncited sentences: {chk['uncited_sentences']}")
    for s in chk["sentences"]:
        if "word_overlap_with_cited" in s:
            L.append(f"- “{s['sentence'][:140]}” → {s['labels'] or 'no label'}, word overlap {s['word_overlap_with_cited']}")
    st = r.get("stats") or {}
    if st:
        L += ["", "## Timing", "",
              f"{st.get('wall_seconds')} s wall · model load {st.get('load_seconds')} s · prompt {st.get('prompt_tokens')} tokens "
              f"in {st.get('prompt_seconds')} s · answer {st.get('output_tokens')} tokens at {st.get('tokens_per_second')} tokens/s"]
    L += ["", "## Assessment (human, after opening the cited passages)", "", t.get("assessment", "_Pending review._"), ""]
    return "\n".join(L)
