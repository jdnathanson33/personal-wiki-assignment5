"""Write and check the Obsidian-facing side of the wiki.

- render_note(): frontmatter + heading (= filename) + summary + details +
  related-note links (with the reason for each link) + source references.
- write_index(): vault/index.md, the human landing page, grouped by topic folder.
- write_catalog(): vault/Source Catalog.md, mapping machine source ids and
  original filenames to readable notes.
- lint(): broken links, heading/filename mismatches, machine-style names,
  duplicate note names, notes without sources.
"""
from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

LINK = re.compile(r"\[\[([^\]|#]+)(?:#([^\]|]+))?(?:\|([^\]]+))?\]\]")
MACHINE_NAME = re.compile(r"([0-9a-f]{8,}|\d{8}T?\d{0,6}|--|_{2,}|\bchunk\b|\btask[- ]\d)", re.I)

FOLDER_BLURBS = {
    "Course": "Class-by-class notes from the Fundamentals of Agentic AI slide decks.",
    "Projects": "My course assignments: what I built, the settings I chose, and what happened.",
    "Concepts": "Ideas that show up across classes and projects, explained with my own evidence.",
    "Notes": "Other notes created from sources that are not in the curated plan yet.",
}
FOLDER_ORDER = ["Course", "Projects", "Concepts", "Notes"]


# ------------------------------------------------------------------ frontmatter

def parse_frontmatter(text: str) -> Dict[str, object]:
    """Tiny parser for the frontmatter this harness writes (scalars and '- ' lists)."""
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    data: Dict[str, object] = {}
    key = None
    for line in m.group(1).splitlines():
        if re.match(r"^\s+- ", line) and key:
            val = line.strip()[2:].strip().strip('"')
            lst = data.setdefault(key, [])
            if isinstance(lst, list):
                lst.append(val)
        elif ":" in line and not line.startswith(" "):
            key, val = line.split(":", 1)
            key, val = key.strip(), val.strip()
            if val == "":
                data[key] = []
            else:
                val = val.strip('"')
                data[key] = {"true": True, "false": False}.get(val, val)
    return data


def first_sentence(text: str) -> str:
    """First sentence, not fooled by abbreviations like 'Ms. Pac-Man' (used for index descriptions)."""
    from .citations import split_sentences
    parts = split_sentences(text.strip().split("\n")[0])
    return parts[0] if parts else text.strip()


def _q(s: str) -> str:
    return '"' + s.replace('"', "'") + '"'


def raw_link(vault_rel: str, label: str, heading: Optional[str] = None) -> str:
    target = vault_rel + (f"#{heading}" if heading else "")
    return f"[[{target}|{label}]]"


# ------------------------------------------------------------------ note rendering

def render_note(title: str, folder: str, summary: str, details: List[str],
                related: List[dict], source_refs: List[dict], meta: dict) -> str:
    desc = first_sentence(summary)
    fm = ["---", f"title: {_q(title)}", f"description: {_q(desc)}", f"type: {folder.lower().rstrip('s')}"]
    fm.append("sources:")
    fm += [f"  - {_q('[[' + r['vault_path'] + ']]')}" for r in source_refs]
    fm.append("source_ids:")
    fm += [f"  - {r['id']}" for r in source_refs]
    fm.append("source_sha256:")
    fm += [f"  - {r['id']}@{r['sha256'][:12]}" for r in source_refs]
    fm += [f"model: {meta.get('model', '')}", f"execution: {meta.get('execution', 'local')}",
           f"generated: {meta.get('generated', datetime.now().strftime('%Y-%m-%d'))}",
           f"reviewed: {'true' if meta.get('reviewed') else 'false'}"]
    if meta.get("review_note"):
        fm.append(f"review_note: {_q(meta['review_note'])}")
    fm.append("---")

    body = [f"# {title}", "", summary.strip(), "", "## Key details", ""]
    body += [f"- {d}" for d in details] or ["- (no details extracted)"]
    if related:
        body += ["", "## Related notes", ""]
        body += [f"- [[{r['title']}]] — {r['why']}" for r in related]
    body += ["", "## Sources", ""]
    for r in source_refs:
        line = f"- {raw_link(r['vault_path'], r['label'])}"
        if r.get("sections"):
            line += " — " + ", ".join(r["sections"])
        if r.get("url"):
            line += f" · [public page]({r['url']})"
        body.append(line)
    return "\n".join(fm) + "\n\n" + "\n".join(body) + "\n"


# ------------------------------------------------------------------ vault scanning

def list_notes(wiki_dir: Path) -> List[Path]:
    return sorted(p for p in wiki_dir.rglob("*.md") if not any(x.startswith(".") for x in p.parts))


def first_heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def write_index(vault: Path, wiki_dir: Path, catalog_name: str) -> Path:
    groups: Dict[str, List[tuple]] = {}
    for p in list_notes(wiki_dir):
        folder = p.relative_to(wiki_dir).parts[0] if len(p.relative_to(wiki_dir).parts) > 1 else "Notes"
        fm = parse_frontmatter(p.read_text(encoding="utf-8"))
        groups.setdefault(folder, []).append((p.stem, str(fm.get("description", ""))))
    lines = ["# Personal Wiki Index", "",
             "My course memory for **Fundamentals of Agentic AI** (Berkeley Haas, Fall 2026): the class slide decks "
             "and my own assignment write-ups, organized into linked notes. Start with "
             "[[Fundamentals of Agentic AI]] for the course map, or pick a topic below.", "",
             f"Every note ends with a **Sources** list that links back to the unchanged original in `raw/`. "
             f"The [[{catalog_name}]] maps each original file to the notes made from it.", ""]
    order = FOLDER_ORDER + sorted(k for k in groups if k not in FOLDER_ORDER)
    for folder in order:
        if folder not in groups:
            continue
        lines += [f"## {folder}", "", f"_{FOLDER_BLURBS.get(folder, '')}_", ""]
        for stem, desc in sorted(groups[folder], key=lambda x: _natural(x[0])):
            lines.append(f"- [[{stem}]] — {desc}" if desc else f"- [[{stem}]]")
        lines.append("")
    lines += ["---", f"_Updated by `wiki ingest` on {datetime.now().strftime('%Y-%m-%d %H:%M')}._", ""]
    out = vault / "index.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def _natural(s: str):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]


def write_catalog(path: Path, catalog: dict) -> Path:
    lines = [f"# {path.stem}", "",
             "Each original source in `raw/` is kept unchanged. This table maps its machine id and original "
             "filename to the readable wiki notes generated from it. The same data, for the harness, is in "
             "`state/catalog.json` (outside the vault).", "",
             "| Source id | Original file (in raw/) | Came from | SHA-256 (first 12) | In public repo | Notes made from it |",
             "|---|---|---|---|---|---|"]
    for sid, s in sorted(catalog.get("sources", {}).items()):
        notes = ", ".join(f"[[{n}]]" for n in s.get("notes", [])) or "—"
        origin = s.get("origin", "")
        lines.append(f"| `{sid}` | [[{s['vault_path']}\\|{Path(s['vault_path']).name}]] | {origin} | "
                     f"`{s['sha256'][:12]}` | {'yes' if s.get('public', True) else 'no (local only)'} | {notes} |")
    lines += ["", "Related: [[index]] · [[Fundamentals of Agentic AI]]", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


# ------------------------------------------------------------------ lint

def lint(vault: Path, wiki_dir: Path) -> List[str]:
    problems: List[str] = []
    notes = list_notes(wiki_dir)
    stems: Dict[str, List[Path]] = {}
    for p in notes:
        stems.setdefault(p.stem.lower(), []).append(p)
    for stem, paths in stems.items():
        if len(paths) > 1:
            problems.append(f"duplicate note name '{stem}': " + ", ".join(str(x.relative_to(vault)) for x in paths))
    all_files = {p.relative_to(vault).as_posix().lower() for p in vault.rglob("*") if p.is_file()}
    all_stems = {p.stem.lower() for p in vault.rglob("*.md")}
    check = notes + [vault / "index.md"] + list(vault.glob("*.md"))
    for p in dict.fromkeys(check):
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        rel = p.relative_to(vault).as_posix()
        if p.parent != vault:
            if first_heading(text) != p.stem:
                problems.append(f"{rel}: first heading '{first_heading(text)}' does not match filename")
            if MACHINE_NAME.search(p.stem) or len(p.stem.split()) > 7:
                problems.append(f"{rel}: filename looks machine-generated or too long")
            if "## Sources" not in text:
                problems.append(f"{rel}: no Sources section")
            if re.search(r"\[E\d+\]", text):
                problems.append(f"{rel}: unresolved excerpt label left in text")
        for m in LINK.finditer(text):
            target = m.group(1).strip().rstrip("\\")  # '\|' is a table-escaped alias pipe
            t = target.lower()
            if t in all_stems or t in all_files or (t + ".md") in all_files:
                continue
            problems.append(f"{rel}: broken link [[{target}]]")
    return problems
