"""`wiki ingest`: raw sources -> Gemma-drafted wiki notes -> index.md -> retrieval index.

Flow for each source file under vault/raw/:
  1. Hash the file and record it in the source catalog (state/catalog.json).
     Originals are only read, never modified.
  2. Find the wiki notes that draw on it. Curated notes come from
     config/wiki_plan.json (readable title, topic folder, which sections to use,
     and which related notes to link, with the reason). A file that is not in the
     plan gets one note in Notes/, titled by Gemma once and then remembered in the
     catalog, so re-ingesting never produces a second copy under a new name.
  3. For each note: collect the relevant sections (labelled [E1], [E2] ...), send
     them with instructions/ingest-instructions.md to local Gemma, parse
     SUMMARY/DETAILS, turn [E#] labels into links back to the exact section of the
     original, and write the note.
     - Note unchanged sources and existing note  -> "up to date", no model call.
     - Note marked `reviewed: true` (a human checked it against the source)
       -> the new Gemma draft goes to runs/ingest/<time>/drafts/ and the reviewed
          note is kept, unless --overwrite-reviewed.
  4. Rewrite vault/index.md and vault/Source Catalog.md, rebuild the retrieval
     index (state/index/), run the link checker, and save a run log.
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from . import wikiwriter
from .config import Settings, read_instruction
from .ollama_client import ModelUnavailable, OllamaClient
from .retrieval import Index, build_embeddings, _doc_prompt
from .sources import (Passage, file_sha256, iter_source_files, load_sections, passages_for_file, slugify)

BAD_TITLE_CHARS = re.compile(r'[\\/:*?"<>|#^\[\]]')


def _now() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def load_json(path: Path, default):
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return default


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# ------------------------------------------------------------------ plan helpers

def _plan_source_by_path(plan: dict) -> Dict[str, dict]:
    return {s["path"]: s for s in plan.get("sources", [])}


def _select_sections(sections, wanted: List[str]):
    if not wanted or wanted == ["*"]:
        return list(sections)
    out = []
    for sec in sections:
        loc = sec.locator.lower()
        for w in wanted:
            wl = w.lower()
            if ((w == "#intro" and " > " not in sec.locator)          # text under the document title
                    or (w.startswith("=") and loc == wl[1:])           # exact locator
                    or (w.startswith("^") and loc.startswith(wl[1:]))  # locator prefix
                    or (w[0] not in "=^#" and wl in loc)):             # substring (also matches "part: ...")
                out.append(sec)
                break
    return out


def _clean_title(t: str) -> str:
    t = BAD_TITLE_CHARS.sub("", t.strip().strip("'\"").splitlines()[0] if t.strip() else "")
    t = re.sub(r"^(title|note)\s*[:\-]\s*", "", t, flags=re.I)
    words = t.split()[:6]
    return " ".join(w if w.isupper() else w[:1].upper() + w[1:] for w in words) or "Untitled Note"


# ------------------------------------------------------------------ model step

def parse_draft(text: str) -> (str, List[str]):
    summary, details, mode = [], [], None
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        up = s.upper().lstrip("#* ")
        if up.startswith("SUMMARY"):
            mode = "s"
            rest = s.split(":", 1)[1].strip() if ":" in s else ""
            if rest:
                summary.append(rest)
            continue
        if up.startswith("DETAILS"):
            mode = "d"
            continue
        if s[:1] in "-*•" and (mode == "d" or mode is None or summary):
            mode = "d"
            details.append(s[1:].strip())
        elif mode == "s":
            summary.append(s)
        elif mode == "d" and details:
            details[-1] += " " + s
    return " ".join(summary).strip(), [d for d in details if d]


def _resolve_labels(text: str, excerpts: List[dict]) -> str:
    def repl(m):
        refs = []
        for n in re.findall(r"\d+", m.group(0)):
            i = int(n) - 1
            if 0 <= i < len(excerpts):
                e = excerpts[i]
                if e["url"]:
                    refs.append(f"[{e['short']}]({e['url']})")
                else:
                    refs.append(wikiwriter.raw_link(e["vault_path"], e["short"], e["heading"]))
        return (" (" + "; ".join(dict.fromkeys(refs)) + ")") if refs else ""
    text = re.sub(r"\s*\[E\d+(?:\s*[,;]\s*E?\d+)*\]", repl, text)
    return text.strip()


def draft_note(client: OllamaClient, settings: Settings, title: str, focus: str, excerpts: List[dict]) -> dict:
    system = read_instruction(settings, "ingest-instructions.md")
    blocks, used = [], 0
    for i, e in enumerate(excerpts, 1):
        block = f"[E{i}] {e['doc']} — {e['locator']}\n{e['text']}"
        if used + len(block) > settings.ingest_source_chars and blocks:
            break
        blocks.append(block[: settings.ingest_source_chars - used])
        used += len(block)
    user = (f"Subject of the note: {title}\n"
            + (f"Focus: {focus}\n" if focus else "")
            + "\nExcerpts:\n\n" + "\n\n".join(blocks)
            + f"\n\nWrite the note about \"{title}\" in the required format.")
    res = client.chat([{"role": "system", "content": system}, {"role": "user", "content": user}],
                      temperature=settings.temperature["ingest"], max_tokens=700)
    summary, details = parse_draft(res["text"])
    return {"raw_output": res["text"], "summary": summary, "details": details, "stats": res["stats"],
            "excerpt_chars": used, "excerpts_sent": len(blocks)}


# ------------------------------------------------------------------ retrieval index

def rebuild_index(settings: Settings, client: Optional[OllamaClient], log=print) -> dict:
    passages: List[Passage] = []
    for f in iter_source_files(settings.raw):
        passages += passages_for_file(f, settings.rel(f), "raw", settings.chunk_chars, settings.chunk_overlap)
    for f in wikiwriter.list_notes(settings.wiki):
        passages += passages_for_file(f, settings.rel(f), "wiki", settings.chunk_chars, settings.chunk_overlap)

    # Re-use vectors whose passage text has not changed (saves time on re-ingest).
    old = load_json(settings.embeddings_file, {})
    old_vecs, old_hash = old.get("vectors", {}), old.get("hashes", {})
    same_model = old.get("model") == settings.embed_model
    hashes = {p.id: hashlib.sha1(_doc_prompt(p).encode()).hexdigest() for p in passages}
    vecs = {pid: old_vecs[pid] for pid in hashes if same_model and old_hash.get(pid) == hashes[pid] and pid in old_vecs}
    todo = [p for p in passages if p.id not in vecs]
    note = ""
    if client is not None and todo:
        try:
            t0 = time.time()
            vecs.update(build_embeddings(todo, client,
                                         progress=lambda d, n: log(f"  embedded {d}/{n} passages") if d % 160 == 0 else None))
            log(f"  embedded {len(todo)} new/changed passages in {time.time() - t0:.1f}s" + " " * 20)
        except ModelUnavailable as e:
            note = f"embeddings skipped ({str(e).splitlines()[0]}); search will be keyword-only"
            log("  " + note)
    idx = Index(passages, vecs)
    idx.save(settings.chunks_file, settings.embeddings_file, settings.embed_model)
    data = load_json(settings.embeddings_file, {})
    data["hashes"] = {k: v for k, v in hashes.items() if k in vecs}
    save_json(settings.embeddings_file, data)
    return {"passages": len(passages), "raw_passages": sum(p.kind == "raw" for p in passages),
            "wiki_passages": sum(p.kind == "wiki" for p in passages),
            "embedded": len(vecs), "reused_vectors": len(passages) - len(todo), "note": note}


# ------------------------------------------------------------------ main entry

def run_ingest(settings: Settings, client: OllamaClient, target: Path, force: bool = False,
               overwrite_reviewed: bool = False, log=print) -> dict:
    t_start = time.time()
    target = target.resolve()
    raw_root = settings.raw.resolve()
    if not target.exists():
        raise FileNotFoundError(f"Path not found: {target}")
    if raw_root not in target.parents and target != raw_root:
        raise ValueError(f"Sources must live under {settings.rel(raw_root)}/ so originals stay separate from notes. "
                         f"Copy the file there first (the harness never edits it).")
    files = [target] if target.is_file() else iter_source_files(target)
    if not files:
        raise FileNotFoundError(f"No .md/.txt/.html sources found in {settings.rel(target)}")

    plan = load_json(settings.plan, {"sources": [], "notes": []})
    plan_src = _plan_source_by_path(plan)
    catalog = load_json(settings.catalog_file, {"sources": {}})
    run_id = _now()
    run_dir = settings.runs / "ingest" / run_id
    record = {"run_id": run_id, "command": f"wiki ingest {settings.rel(target)}", "model": client.model,
              "execution": "local", "force": force, "sources": [], "notes": [], "errors": []}

    # ---- 1. catalog every source in the target
    touched: Dict[str, dict] = {}
    for f in files:
        vault_rel = settings.vault_rel(f)
        ps = plan_src.get(vault_rel, {})
        sid = ps.get("id") or slugify(f.stem)
        sha = file_sha256(f)
        entry = catalog["sources"].get(sid, {})
        changed = entry.get("sha256") not in (None, sha)
        doc_title, _ = load_sections(f)
        entry.update({
            "vault_path": vault_rel, "original_filename": ps.get("original_filename", f.name),
            "origin": ps.get("origin", "added by user"), "public": ps.get("public", True),
            "url": ps.get("url", ""), "title": ps.get("label") or doc_title or f.stem, "sha256": sha,
            "bytes": f.stat().st_size, "first_ingested": entry.get("first_ingested", run_id), "last_ingested": run_id,
        })
        entry.setdefault("notes", [])
        catalog["sources"][sid] = entry
        touched[vault_rel] = {"id": sid, "path": f, "entry": entry}
        record["sources"].append({"id": sid, "path": vault_rel, "sha256": sha, "changed_since_last": changed})
        log(f"source  {vault_rel}  ({entry['bytes']:,} bytes, sha {sha[:12]}{', CHANGED' if changed else ''})")

    # ---- 2. which notes draw on these sources?
    specs = []
    for n in plan.get("notes", []):
        if any(s["path"] in touched for s in n.get("sources", [])):
            specs.append(n)
    planned_paths = {s["path"] for n in plan.get("notes", []) for s in n.get("sources", [])}
    for vault_rel, t in touched.items():
        if vault_rel not in planned_paths:
            specs.append({"auto": True, "folder": "Notes", "title": t["entry"].get("auto_title"),
                          "focus": "", "sources": [{"path": vault_rel, "sections": ["*"]}], "related": []})

    # notes that exist (or will) so related links never point at nothing
    planned_titles = set()
    for n in plan.get("notes", []):
        if all((settings.vault / s["path"]).exists() for s in n.get("sources", [])):
            planned_titles.add(n["title"])
    existing_titles = {p.stem for p in wikiwriter.list_notes(settings.wiki)}

    # ---- 3. draft each note
    for spec in specs:
        missing = [s["path"] for s in spec["sources"] if not (settings.vault / s["path"]).exists()]
        if missing:
            log(f"skip    {spec.get('title')}: missing source {missing[0]}")
            record["notes"].append({"title": spec.get("title"), "action": "skipped (missing source)", "missing": missing})
            continue
        refs, excerpts = [], []
        for s in spec["sources"]:
            f = settings.vault / s["path"]
            ps = plan_src.get(s["path"], {})
            sid = ps.get("id") or slugify(f.stem)
            cat = catalog["sources"].get(sid) or {}
            doc_title, sections = load_sections(f)
            chosen = _select_sections(sections, s.get("sections", ["*"]))
            label = ps.get("label") or doc_title or f.stem
            base_url = ps.get("url", "")
            for sec in chosen:
                excerpts.append({"doc": label, "locator": sec.locator, "text": sec.text,
                                 "vault_path": s["path"],
                                 # Obsidian heading links can't contain [ ] | # ^ ; fall back to the file link
                                 "heading": None if base_url or re.search(r"[\[\]|#^]", sec.anchor or "") else (sec.anchor or sec.title),
                                 "short": ("§ " + sec.title) if not base_url else f"{label}, {sec.locator.split(' (part')[0]}",
                                 "url": (base_url + "#/" + sec.anchor) if base_url and sec.anchor else base_url})
            refs.append({"id": sid, "vault_path": s["path"], "label": label, "sha256": cat.get("sha256") or file_sha256(f),
                         "url": base_url,
                         "sections": [] if s.get("sections", ["*"]) == ["*"] else
                         list(dict.fromkeys(x.title for x in chosen))[:8]})
        if not excerpts:
            log(f"skip    {spec.get('title')}: none of the requested sections were found")
            record["notes"].append({"title": spec.get("title"), "action": "skipped (sections not found)"})
            continue

        # Auto notes get a readable title from Gemma once; the catalog remembers it.
        if spec.get("auto") and not spec.get("title"):
            res = client.chat([{"role": "system", "content": "You name wiki notes. Reply with a title only."},
                               {"role": "user", "content": "Suggest a short, natural title (2 to 6 words, Title Case, "
                                "no dates, no file names) for a wiki note about this document:\n\n"
                                + excerpts[0]["text"][:1500]}], temperature=0.1, max_tokens=20)
            spec["title"] = _clean_title(res["text"])
            if spec["title"] in existing_titles | planned_titles:
                spec["title"] += " - " + refs[0]["label"][:30]
            catalog["sources"][refs[0]["id"]]["auto_title"] = spec["title"]

        title, folder = spec["title"], spec.get("folder", "Notes")
        note_path = settings.wiki / folder / f"{title}.md"
        cur_hashes = sorted(f"{r['id']}@{r['sha256'][:12]}" for r in refs)
        fm = wikiwriter.parse_frontmatter(note_path.read_text(encoding="utf-8")) if note_path.exists() else {}
        up_to_date = note_path.exists() and sorted(fm.get("source_sha256", []) or []) == cur_hashes
        reviewed = bool(fm.get("reviewed"))

        for r in refs:  # catalog: source -> notes
            notes = catalog["sources"].setdefault(r["id"], {}).setdefault("notes", [])
            if title not in notes:
                notes.append(title)

        if up_to_date and not force:
            log(f"ok      {folder}/{title}.md  up to date (sources unchanged{', reviewed' if reviewed else ''}) — no model call")
            record["notes"].append({"title": title, "path": settings.rel(note_path), "action": "up to date"})
            continue

        log(f"draft   {folder}/{title}.md  <- {len(excerpts)} section(s), asking {client.model} ...")
        d = draft_note(client, settings, title, spec.get("focus", ""), excerpts)
        if not d["summary"] or not d["details"]:
            record["errors"].append({"title": title, "error": "model output did not follow the format",
                                     "raw_output": d["raw_output"]})
            log(f"  !! model output did not follow SUMMARY/DETAILS format; note not written (see run log)")
            continue
        summary = _resolve_labels(d["summary"], excerpts)
        details = [_resolve_labels(x, excerpts) for x in d["details"]]
        related = [r for r in spec.get("related", []) if r["title"] in planned_titles | existing_titles]
        text = wikiwriter.render_note(title, folder, summary, details, related, refs,
                                      {"model": client.model, "execution": "local", "reviewed": False})
        s = d["stats"]
        entry = {"title": title, "path": settings.rel(note_path), "excerpts_sent": d["excerpts_sent"],
                 "excerpt_chars": d["excerpt_chars"], "stats": s, "raw_output": d["raw_output"]}
        if reviewed and not overwrite_reviewed:
            draft_path = run_dir / "drafts" / f"{title}.md"
            draft_path.parent.mkdir(parents=True, exist_ok=True)
            draft_path.write_text(text, encoding="utf-8")
            entry.update({"action": "draft saved; reviewed note kept", "draft": settings.rel(draft_path)})
            log(f"  kept reviewed note; new draft -> {settings.rel(draft_path)}  ({s['wall_seconds']}s)")
        else:
            note_path.parent.mkdir(parents=True, exist_ok=True)
            entry["action"] = "updated" if note_path.exists() else "created"
            note_path.write_text(text, encoding="utf-8")
            log(f"  {entry['action']} ({s['wall_seconds']}s, {s['output_tokens']} tokens)")
        record["notes"].append(entry)

    # ---- 4. navigation, catalog, retrieval index, checks
    save_json(settings.catalog_file, catalog)
    wikiwriter.write_catalog(settings.catalog_md, catalog)
    wikiwriter.write_index(settings.vault, settings.wiki, settings.catalog_md.stem)
    log("index   vault/index.md and vault/Source Catalog.md updated")
    log("index   rebuilding retrieval index ...")
    record["retrieval_index"] = rebuild_index(settings, client, log=_log_end(log))
    ri = record["retrieval_index"]
    log(f"index   {ri['passages']} passages ({ri['raw_passages']} raw, {ri['wiki_passages']} wiki), "
        f"{ri['embedded']} with embeddings")
    record["lint"] = wikiwriter.lint(settings.vault, settings.wiki)
    names = [p.stem for p in wikiwriter.list_notes(settings.wiki)]
    record["note_count"] = len(names)
    record["duplicate_names"] = sorted({n for n in names if names.count(n) > 1})
    record["seconds"] = round(time.time() - t_start, 1)
    log(f"check   {len(names)} notes, {len(record['duplicate_names'])} duplicate names, "
        f"{len(record['lint'])} link/naming problems")
    for p in record["lint"][:15]:
        log("   - " + p)
    save_json(run_dir.with_suffix(".json"), record)
    log(f"saved   {settings.rel(run_dir.with_suffix('.json'))}  ({record['seconds']}s total)")
    return record


def _log_end(log):
    def inner(msg, end="\n"):
        try:
            log(msg, end=end)
        except TypeError:
            log(msg)
    return inner
