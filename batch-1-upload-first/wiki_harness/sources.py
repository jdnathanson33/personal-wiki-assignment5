"""Read local sources and split them into citable passages.

Two formats are supported, both parsed locally with the standard library:
  * Markdown (.md, .txt): split at headings (ignoring '#' lines inside code
    fences); each passage keeps its heading path, e.g.
    "Authentication and RLS ownership > The four policies".
  * Quarto/reveal.js slide decks (.html): one section per slide; each passage
    keeps "slide N: <title>" and the slide's anchor (class1.html#/<id>).

Long sections are packed into passages of about `chunk_chars` characters on
paragraph boundaries, with a short overlap so a sentence cut at the boundary is
still findable.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field, asdict
from html.parser import HTMLParser
from pathlib import Path
from typing import List, Optional

SUPPORTED = {".md", ".markdown", ".txt", ".html", ".htm"}


@dataclass
class Section:
    locator: str            # human-readable place in the source
    text: str
    anchor: str = ""        # heading slug or slide id, for links
    title: str = ""


@dataclass
class Passage:
    id: str                 # e.g. "pacman-dqn-README#07"
    kind: str               # "raw" (original evidence) or "wiki" (generated note)
    path: str               # project-relative path of the file
    locator: str
    anchor: str
    text: str
    title: str = ""         # document title
    extra: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def slugify(text: str) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    return re.sub(r"[\s_]+", "-", s)


# ---------------------------------------------------------------- Markdown

_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)


def strip_frontmatter(text: str) -> str:
    return _FRONTMATTER.sub("", text, count=1)


def parse_markdown(text: str) -> tuple[str, List[Section]]:
    text = strip_frontmatter(text)
    sections: List[Section] = []
    path: List[tuple[int, str]] = []
    raw_heads: List[str] = []
    buf: List[str] = []
    doc_title = ""
    in_fence = False

    def flush():
        body = "\n".join(buf).strip()
        if body:
            names = [h for _, h in path] or ["(top)"]
            loc = " > ".join(names)
            # anchor keeps the heading exactly as written, so Obsidian [[file#heading]] links resolve
            sections.append(Section(locator=loc, text=body, anchor=raw_heads[-1] if raw_heads else "", title=names[-1]))
        buf.clear()

    for line in text.splitlines():
        if line.strip().startswith("```") or line.strip().startswith("~~~"):
            in_fence = not in_fence
            buf.append(line)
            continue
        m = None if in_fence else _HEADING.match(line)
        if m:
            flush()
            level, heading = len(m.group(1)), m.group(2).strip()
            heading = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # "[text](url)" -> "text"
            heading = re.sub(r"[*`]", "", heading)
            if level == 1 and not doc_title:
                doc_title = heading
            while path and path[-1][0] >= level:
                path.pop()
                raw_heads.pop()
            path.append((level, heading))
            raw_heads.append(m.group(2).strip())
        else:
            buf.append(line)
    flush()
    return doc_title, sections


# ---------------------------------------------------------------- Slides (HTML)

_BLOCK = {"p", "div", "li", "ul", "ol", "br", "tr", "table", "pre", "blockquote",
          "h1", "h2", "h3", "h4", "h5", "h6", "section", "td", "th", "figcaption", "dt", "dd"}
_SKIP = {"script", "style", "noscript", "template", "button"}


class _SlideParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.slides: List[dict] = []
        self._stack: List[Optional[dict]] = []   # one entry per open <section>
        self._skip = 0
        self._in_heading = None
        self.doc_title = ""
        self._in_title_tag = False
        self.part = ""

    def _current(self) -> Optional[dict]:
        for s in reversed(self._stack):
            if s is not None:
                return s
        return None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in _SKIP:
            self._skip += 1
            return
        if tag == "title":
            self._in_title_tag = True
        if tag == "section":
            cls = a.get("class", "") or ""
            sid = a.get("id", "") or ""
            if "slide" in cls.split() or sid == "title-slide":
                slide = {"id": sid, "title": "", "text": [], "level1": "level1" in cls.split()}
                self.slides.append(slide)
                self._stack.append(slide)
            else:
                self._stack.append(None)
            return
        cur = self._current()
        if cur is None or self._skip:
            return
        if tag in ("h1", "h2") and not cur["title"]:
            self._in_heading = cur
        if tag == "li":
            cur["text"].append("\n- ")
        elif tag in _BLOCK:
            cur["text"].append("\n")
        elif tag in ("td", "th"):
            cur["text"].append(" | ")

    def handle_endtag(self, tag):
        if tag in _SKIP:
            self._skip = max(0, self._skip - 1)
            return
        if tag == "title":
            self._in_title_tag = False
        if tag == "section":
            if self._stack:
                self._stack.pop()
            return
        if tag in ("h1", "h2"):
            self._in_heading = None
        cur = self._current()
        if cur is not None and tag in _BLOCK:
            cur["text"].append("\n")

    def handle_data(self, data):
        if self._in_title_tag:
            self.doc_title += data
        if self._skip:
            return
        cur = self._current()
        if cur is None:
            return
        if self._in_heading is cur:
            cur["title"] += data
        cur["text"].append(data)


def _tidy(text: str) -> str:
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def parse_slides(html: str) -> tuple[str, List[Section]]:
    p = _SlideParser()
    p.feed(html)
    sections: List[Section] = []
    part = ""
    for n, s in enumerate(p.slides, start=1):
        title = _tidy(s["title"]) or "(untitled)"
        body = _tidy("".join(s["text"]))
        if s["level1"]:
            part = title
        loc = f"slide {n}: {title}"
        if part and part != title:
            loc += f" (part: {part})"
        # Part-divider slides carry only their title; they add noise to retrieval.
        if body and not (len(body) < 40 and body.strip() == title):
            sections.append(Section(locator=loc, text=body, anchor=s["id"], title=title))
    doc_title = _tidy(p.doc_title)
    if sections and sections[0].anchor == "title-slide":
        doc_title = sections[0].title or doc_title
    return doc_title, sections


# ---------------------------------------------------------------- loading + chunking

def load_sections(path: Path) -> tuple[str, List[Section]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() in (".html", ".htm"):
        return parse_slides(text)
    return parse_markdown(text)


def _split_units(text: str, limit: int) -> List[str]:
    """Paragraphs, falling back to lines and then hard cuts for very long ones."""
    units: List[str] = []
    for para in re.split(r"\n\s*\n", text):
        para = para.strip()
        if not para:
            continue
        if len(para) <= limit:
            units.append(para)
            continue
        for line in para.splitlines():
            while len(line) > limit:
                cut = line.rfind(" ", 0, limit)
                cut = cut if cut > limit // 2 else limit
                units.append(line[:cut])
                line = line[cut:].lstrip()
            if line.strip():
                units.append(line)
    return units


def chunk_section(sec: Section, chunk_chars: int, overlap: int) -> List[str]:
    units = _split_units(sec.text, chunk_chars)
    chunks: List[str] = []
    cur = ""
    for u in units:
        if cur and len(cur) + len(u) + 2 > chunk_chars:
            chunks.append(cur)
            tail = cur[-overlap:]
            tail = tail[tail.find(" ") + 1:] if " " in tail else tail
            cur = ("…" + tail + "\n\n" + u) if overlap else u
        else:
            cur = (cur + "\n\n" + u) if cur else u
    if cur:
        chunks.append(cur)
    return chunks


def passages_for_file(path: Path, rel_path: str, kind: str, chunk_chars: int, overlap: int) -> List[Passage]:
    doc_title, sections = load_sections(path)
    stem = slugify(path.stem) or "doc"
    out: List[Passage] = []
    n = 0
    for sec in sections:
        # In generated notes, link lists are navigation, not content: keep them out of retrieval.
        if kind == "wiki" and sec.title in ("Related notes", "Sources"):
            continue
        for piece in chunk_section(sec, chunk_chars, overlap):
            n += 1
            out.append(Passage(id=f"{stem}#{n:03d}", kind=kind, path=rel_path, locator=sec.locator,
                               anchor=sec.anchor, text=piece, title=doc_title or path.stem))
    return out


def iter_source_files(folder: Path) -> List[Path]:
    files = [p for p in sorted(folder.rglob("*")) if p.is_file() and p.suffix.lower() in SUPPORTED
             and not any(part.startswith(".") for part in p.relative_to(folder).parts)]
    return files
