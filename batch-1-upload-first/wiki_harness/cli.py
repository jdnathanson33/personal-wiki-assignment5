"""Command-line interface: parses the command, picks the mode, and hands off.

  wiki ingest [PATH]   raw sources -> Gemma-drafted notes -> index.md -> retrieval index
  wiki search "..."    retrieval tool only: original passages + paths, no generation
  wiki ask "..."       RAG: retrieve -> research rules -> Gemma -> checked citations
  wiki chat            personal assistant with conversation memory; retrieves only when useful
  wiki eval            run the four fixed ask-mode tests in tests/ask_questions.json
  wiki status          device, runtime, model, index and vault health
  wiki measure         memory use and response time for one real RAG answer
  wiki lint            check wiki links, headings, and note names
"""
from __future__ import annotations

import argparse
import json
import sys
import threading
import time
from pathlib import Path

from . import records, wikiwriter
from .config import ROOT, load_settings
from .ollama_client import ModelUnavailable, OllamaClient
from .retrieval import Index
from .system import device_info, internet_status, ollama_process_rss_mb

EPILOG = """examples:
  ./wiki status
  ./wiki ingest vault/raw
  ./wiki search "row level security update policy"
  ./wiki ask "What was the Pac-Man agent's mean evaluation score before and after training?"
  ./wiki chat
  ./wiki eval

configuration: config/settings.json (model, embedding model, chunk size, top-k, context budgets)
instructions:  instructions/persona.md (chat), instructions/wiki-instructions.md (ask),
               instructions/ingest-instructions.md (ingest)
requires:      Ollama running locally with the models pulled:
                 ollama pull gemma4:e2b-it-qat
                 ollama pull embeddinggemma
"""


def make_client(settings) -> OllamaClient:
    return OllamaClient(settings.ollama_url, settings.model, settings.embed_model, settings.num_ctx, settings.keep_alive)


def require_model(client: OllamaClient) -> None:
    """Fail early with a useful message instead of a stack trace."""
    try:
        if not client.has_model(client.model):
            raise ModelUnavailable(f"Model '{client.model}' is not downloaded.\n  While online, run:  ollama pull {client.model}")
    except ModelUnavailable:
        raise


def show_search(settings, client, query: str, k: int, scope: str, full: bool, save: bool = True) -> dict:
    try:
        idx = Index.load(settings.chunks_file, settings.embeddings_file)
    except FileNotFoundError as e:
        print(f"error: {e}")
        return {}
    res = idx.search(query, k=k, scope=scope, client=client)
    print(f"[search · retrieval only, no text generation · {res['method']} · scope={scope} · "
          f"internet: {internet_status()}]")
    if res["note"]:
        print(f"note: {res['note']}")
    if not res["results"]:
        print("no matching passages.")
    for n, r in enumerate(res["results"], 1):
        p = r["passage"]
        print(f"\n#{n} [{p.kind}] {p.path}\n    location: {p.locator}\n    scores: bm25 {r['bm25']}, cosine {r['cosine']}, "
              f"rrf {r['rrf']}; matched: {', '.join(r['matched_terms'][:8])}")
        text = p.text if full else (p.text[:600] + (" …" if len(p.text) > 600 else ""))
        print("    " + text.replace("\n", "\n    "))
    if save:
        rec = {"mode": "search", "execution": "local", "query": query, "scope": scope, "method": res["method"],
               "note": res["note"], "internet_at_run_time": internet_status(), "generated_answer": None,
               "results": [{"rank": n, "kind": r["passage"].kind, "path": r["passage"].path, "locator": r["passage"].locator,
                            "bm25": r["bm25"], "cosine": r["cosine"], "text": r["passage"].text}
                           for n, r in enumerate(res["results"], 1)]}
        path = records.save(settings.runs / "search", records.stamp() + "-" + records.slug(query), rec)
        print(f"\nsaved: {settings.rel(path)}")
    return res


class MemorySampler:
    """Samples resident memory of the Ollama processes while a call runs."""
    def __init__(self, every: float = 0.5):
        self.every, self.peak, self.samples, self._stop = every, 0.0, [], False

    def __enter__(self):
        def loop():
            while not self._stop:
                v = ollama_process_rss_mb()
                if v:
                    self.samples.append(v)
                    self.peak = max(self.peak, v)
                time.sleep(self.every)
        self._t = threading.Thread(target=loop, daemon=True)
        self._t.start()
        return self

    def __exit__(self, *a):
        self._stop = True
        self._t.join(timeout=2)


def cmd_status(settings, client, args) -> int:
    info = device_info()
    print("device:")
    for k, v in info.items():
        print(f"  {k}: {v}")
    print(f"internet: {internet_status()}")
    print(f"mode: local (default)  ·  settings: config/settings.json")
    ok = True
    try:
        print(f"runtime: ollama {client.version()} at {settings.ollama_url}")
        names = {m['name']: m for m in client.list_models()}
        for want in (settings.model, settings.embed_model):
            m = names.get(want) or names.get(want + ":latest")
            if m:
                d = m.get("details", {})
                print(f"  model {want}: present, {m.get('size', 0) / 1e9:.2f} GB on disk, "
                      f"{d.get('parameter_size')} params, {d.get('quantization_level')}, digest {m.get('digest', '')[:12]}")
            else:
                ok = False
                print(f"  model {want}: MISSING  ->  ollama pull {want}")
        for m in client.running():
            print(f"  loaded now: {m.get('name')}  {m.get('size', 0) / 1e9:.2f} GB in memory "
                  f"(VRAM {m.get('size_vram', 0) / 1e9:.2f} GB), context {m.get('context_length', '?')}")
        rss = ollama_process_rss_mb()
        if rss:
            print(f"  ollama processes resident memory: {rss:.0f} MB")
    except ModelUnavailable as e:
        ok = False
        print(f"runtime: NOT AVAILABLE\n  {e}")
    try:
        idx = Index.load(settings.chunks_file, settings.embeddings_file)
        print(f"index: {len(idx.passages)} passages ({sum(p.kind == 'raw' for p in idx.passages)} raw, "
              f"{sum(p.kind == 'wiki' for p in idx.passages)} wiki), {len(idx.embeddings)} embedded")
    except FileNotFoundError as e:
        print(f"index: none yet ({e})")
    notes = wikiwriter.list_notes(settings.wiki)
    problems = wikiwriter.lint(settings.vault, settings.wiki)
    print(f"vault: {len(notes)} notes, {len(problems)} link/naming problems (run ./wiki lint)")
    if args.save:
        path = records.save(ROOT / "evidence", "device", {"device": info, "internet": internet_status(),
                                                        "model": settings.model, "embed_model": settings.embed_model,
                                                        "timestamp": records.run_context(settings, client, "status")})
        print(f"saved: {settings.rel(path)}")
    return 0 if ok else 1


def cmd_measure(settings, client, args) -> int:
    from .ask import run_ask
    require_model(client)
    q = args.question
    before = ollama_process_rss_mb()
    print(f"ollama resident memory before: {before} MB (model may be unloaded)")
    with MemorySampler() as ms:
        t0 = time.time()
        rec = run_ask(settings, client, q, out=print)
        wall = time.time() - t0
    loaded = client.running()
    result = {"question": q, "wall_seconds_end_to_end": round(wall, 2), "model_stats": rec["stats"],
              "ollama_rss_before_mb": before, "ollama_rss_peak_mb": ms.peak,
              "ollama_ps": [{"name": m.get("name"), "size_gb": round(m.get("size", 0) / 1e9, 2),
                             "size_vram_gb": round(m.get("size_vram", 0) / 1e9, 2), "context_length": m.get("context_length")}
                            for m in loaded],
              "device": device_info(), "internet_at_run_time": internet_status(), "model": settings.model}
    print("\nmeasurement:")
    print(json.dumps({k: v for k, v in result.items() if k != "device"}, indent=2))
    path = records.save(ROOT / "evidence" / "measurements", records.stamp() + "-rag-answer", result)
    print(f"saved: {settings.rel(path)}")
    return 0


def retrieval_check(settings, client, tests) -> dict:
    """Inspect retrieval before blaming the model: where do the expected passages rank?"""
    idx = Index.load(settings.chunks_file, settings.embeddings_file)
    report = {"run": records.stamp(), "top_k_used_by_ask": settings.top_k,
              "max_passages_per_file": settings.max_per_file, "tests": []}
    for t in tests:
        res = idx.search(t["question"], k=40, scope="raw", client=client)
        capped = idx.search(t["question"], k=settings.top_k, scope="raw", client=client,
                            max_per_file=settings.max_per_file)
        capped_ids = [r["passage"].id for r in capped["results"]]
        row = {"id": t["id"], "method": res["method"], "expected": []}
        for e in t.get("expected_passages", []):
            rank = next((n for n, r in enumerate(res["results"], 1) if e.lower() in r["passage"].text.lower()), None)
            hit = next((r["passage"].id for r in res["results"] if e.lower() in r["passage"].text.lower()), None)
            row["expected"].append({"passage": e, "rank_without_cap": rank,
                                    "in_ask_context_with_cap": hit in capped_ids if hit else False})
        report["tests"].append(row)
        print(f"{t['id']}: " + ("; ".join(f"“{x['passage']}” rank {x['rank_without_cap']}, in ask top-{settings.top_k} "
                                         f"(cap {settings.max_per_file}/file): {x['in_ask_context_with_cap']}"
                                         for x in row["expected"]) or "no expected passage (unanswerable)"))
    path = records.save(settings.runs / "eval", report["run"] + "-retrieval-check", report)
    print(f"saved: {settings.rel(path)}")
    return report


def cmd_eval(settings, client, args) -> int:
    from .ask import run_ask
    tests = json.loads((ROOT / "tests" / "ask_questions.json").read_text(encoding="utf-8"))["tests"]
    if args.retrieval_only:
        retrieval_check(settings, client, tests)
        return 0
    require_model(client)
    summary = []
    for t in tests:
        if args.only and t["id"] not in args.only:
            continue
        print("\n" + "=" * 78 + f"\n{t['id']}: {t['question']}\n" + "=" * 78)
        with MemorySampler() as ms:
            rec = run_ask(settings, client, t["question"], test=t, out=print)
        got = rec["retrieval"]["passages"]
        paths = {p["path"] for p in got}
        exp_src = t.get("expected_sources", [])
        src_hit = all(any(s in pth for pth in paths) for s in exp_src) if exp_src else None
        texts = " ".join(p["text"] for p in got).lower()
        passage_hit = all(e.lower() in texts for e in t.get("expected_passages", [])) if t.get("expected_passages") else None
        insuff = rec["citation_check"]["verdict"] == "insufficient_evidence"
        summary.append({"id": t["id"], "question": t["question"], "type": t["type"],
                        "expected_sources_retrieved": src_hit, "expected_passages_retrieved": passage_hit,
                        "answer": rec["answer"], "citation_verdict": rec["citation_check"]["verdict"],
                        "insufficient_evidence_response": insuff,
                        "expected_insufficient": t["type"] == "unanswerable",
                        "wall_seconds": (rec.get("stats") or {}).get("wall_seconds"),
                        "ollama_rss_peak_mb": ms.peak, "internet": rec["internet_at_run_time"]})
    out = {"run": records.stamp(), "model": settings.model, "execution": "local", "results": summary}
    path = records.save(settings.runs / "eval", out["run"] + "-ask-tests", out)
    print("\n" + "-" * 78)
    for s in summary:
        print(f"{s['id']}: retrieval source hit={s['expected_sources_retrieved']}, passage hit={s['expected_passages_retrieved']}, "
              f"citation check={s['citation_verdict']}, {s['wall_seconds']}s, internet={s['internet']}")
    print(f"saved: {settings.rel(path)}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="wiki", description="Personal wiki CLI: local Gemma + RAG over my own notes.",
                                 epilog=EPILOG, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mode", choices=["local", "online"], default="local",
                    help="where the model runs (default: local; online is not configured in this project)")
    sub = ap.add_subparsers(dest="cmd", metavar="COMMAND")

    p = sub.add_parser("ingest", help="read local sources, generate linked wiki pages, update index")
    p.add_argument("path", nargs="?", default="vault/raw", help="a file or folder under vault/raw (default: vault/raw)")
    p.add_argument("--force", action="store_true", help="re-draft notes even if their sources are unchanged")
    p.add_argument("--overwrite-reviewed", action="store_true", help="replace human-reviewed notes with new drafts")
    p.add_argument("--index-only", action="store_true", help="only rebuild index.md, catalog, and retrieval index")

    p = sub.add_parser("search", help="show original matching passages and paths (no generation)")
    p.add_argument("query")
    p.add_argument("-k", type=int, default=5)
    p.add_argument("--scope", choices=["all", "raw", "wiki"], default="all")
    p.add_argument("--full", action="store_true", help="print whole passages")

    p = sub.add_parser("ask", help="standalone factual answer with citations, or insufficient evidence")
    p.add_argument("question")
    p.add_argument("-k", type=int, default=None)
    p.add_argument("--scope", choices=["raw", "all", "wiki"], default="raw",
                   help="raw = original sources only (default)")

    p = sub.add_parser("chat", help="personal assistant with conversation context")
    p.add_argument("--script", help="read user messages from a file (for repeatable demos)")

    p = sub.add_parser("eval", help="run the fixed ask-mode tests (tests/ask_questions.json)")
    p.add_argument("--only", nargs="*", help="test ids to run, e.g. T1 T4")
    p.add_argument("--retrieval-only", action="store_true",
                   help="only check where the expected passages rank (no generation)")

    p = sub.add_parser("status", help="device, runtime, model, and index status")
    p.add_argument("--save", action="store_true", help="save to evidence/device.json")

    p = sub.add_parser("measure", help="measure memory and response time for one RAG answer")
    p.add_argument("question", nargs="?",
                   default="What exploration, episodes, and learning rate did I use for the Pac-Man DQN?")

    sub.add_parser("lint", help="check wiki links, headings, names, and sources")

    args = ap.parse_args(argv)
    if not args.cmd:
        ap.print_help()
        return 0
    if args.mode == "online":
        print("error: online mode is an optional extension that this project does not configure. "
              "Everything runs locally; drop --mode online.")
        return 2

    settings = load_settings()
    client = make_client(settings)
    try:
        if args.cmd == "ingest":
            from .ingest import rebuild_index, run_ingest
            if args.index_only:
                from .ingest import load_json
                wikiwriter.write_catalog(settings.catalog_md, load_json(settings.catalog_file, {"sources": {}}))
                wikiwriter.write_index(settings.vault, settings.wiki, settings.catalog_md.stem)
                print(rebuild_index(settings, client))
                return 0
            require_model(client)
            path = Path(args.path)
            path = path if path.is_absolute() else (Path.cwd() / path)
            if not path.exists():
                path = ROOT / args.path
            print(f"[ingest · local · {client.model} · internet: {internet_status()}]")
            run_ingest(settings, client, path, force=args.force, overwrite_reviewed=args.overwrite_reviewed)
        elif args.cmd == "search":
            show_search(settings, client, args.query, args.k, args.scope, args.full)
        elif args.cmd == "ask":
            from .ask import run_ask
            require_model(client)
            run_ask(settings, client, args.question, k=args.k, scope=args.scope)
        elif args.cmd == "chat":
            from .chat import run_chat
            require_model(client)
            run_chat(settings, client, script=args.script,
                     search_fn=lambda q: show_search(settings, client, q, 4, "all", False))
        elif args.cmd == "eval":
            return cmd_eval(settings, client, args)
        elif args.cmd == "status":
            return cmd_status(settings, client, args)
        elif args.cmd == "measure":
            return cmd_measure(settings, client, args)
        elif args.cmd == "lint":
            problems = wikiwriter.lint(settings.vault, settings.wiki)
            print(f"{len(wikiwriter.list_notes(settings.wiki))} notes checked, {len(problems)} problem(s)")
            for pr in problems:
                print("  - " + pr)
            return 1 if problems else 0
    except ModelUnavailable as e:
        print(f"error: {e}")
        return 3
    except (FileNotFoundError, ValueError) as e:
        print(f"error: {e}")
        return 4
    return 0


if __name__ == "__main__":
    sys.exit(main())
