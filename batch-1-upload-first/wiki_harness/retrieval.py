"""The retrieval tool: find relevant original passages in the local index.

Two local signals are combined:
  * BM25 keyword scoring (pure Python, always available, works with the model off)
  * cosine similarity of EmbeddingGemma vectors (via the local Ollama server)

Results are merged with Reciprocal Rank Fusion (RRF). If the embedding model is
not reachable, search silently degrades to BM25-only and says so in the result.
Retrieval only *finds evidence*; it never generates text.
"""
from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional

from .sources import Passage

STOPWORDS = set("""
a an the and or but if then else of to in on at by for with from as is are was were be been being
it its this that these those i me my we our you your he she they them their what which who whom
how why when where do does did done can could should would will shall may might must not no yes
about into over under than so such there here also just only very more most much many any some
all each both few other own same too s t don doesn didn isn wasn aren weren have has had having
""".split())


def tokenize(text: str) -> List[str]:
    toks = re.findall(r"[a-z0-9]+(?:[.'][a-z0-9]+)*", text.lower())
    out = []
    for t in toks:
        t = t.replace("'", "")
        if t in STOPWORDS or len(t) == 1 and not t.isdigit():
            continue
        out.append(stem(t))
    return out


def stem(t: str) -> str:
    """Very light suffix stripping so 'policies'~'policy', 'trained'~'train'."""
    if t.isdigit() or len(t) <= 4:
        return t
    for suf, rep in (("ies", "y"), ("ing", ""), ("ed", ""), ("es", ""), ("s", "")):
        if t.endswith(suf) and len(t) - len(suf) >= 3:
            return t[: -len(suf)] + rep
    return t


_MD_LINK = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
_WIKI_LINK = re.compile(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]")
_URL = re.compile(r"https?://\S+")


def clean_for_index(text: str) -> str:
    """Text used for scoring only: keep link labels, drop URLs and file paths inside links.

    Evidence tables in my READMEs carry long run-folder links; without this they
    dilute both keyword scores and embeddings. The displayed/cited passage is
    always the original text.
    """
    text = _MD_LINK.sub(r"\1", text)
    text = _WIKI_LINK.sub(r"\1", text)
    return _URL.sub(" ", text)


def _query_prompt(q: str) -> str:
    # Task prefixes recommended for EmbeddingGemma retrieval.
    return f"task: search result | query: {q}"


def _doc_prompt(p: Passage) -> str:
    return f"title: {p.title} — {p.locator} | text: {clean_for_index(p.text)}"


def _cosine(a: List[float], b: List[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


class Index:
    def __init__(self, passages: List[Passage], embeddings: Optional[Dict[str, List[float]]] = None):
        self.passages = passages
        self.embeddings = embeddings or {}
        self._prep_bm25()

    # ---------- persistence ----------
    @classmethod
    def load(cls, chunks_file: Path, embeddings_file: Path) -> "Index":
        if not chunks_file.exists():
            raise FileNotFoundError("No retrieval index yet. Run:  ./wiki ingest vault/raw")
        passages = []
        with open(chunks_file, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    passages.append(Passage(**json.loads(line)))
        emb = {}
        if embeddings_file.exists():
            with open(embeddings_file, encoding="utf-8") as f:
                emb = json.load(f).get("vectors", {})
        return cls(passages, emb)

    def save(self, chunks_file: Path, embeddings_file: Path, embed_model: str = "") -> None:
        chunks_file.parent.mkdir(parents=True, exist_ok=True)
        with open(chunks_file, "w", encoding="utf-8") as f:
            for p in self.passages:
                f.write(json.dumps(p.to_dict(), ensure_ascii=False) + "\n")
        with open(embeddings_file, "w", encoding="utf-8") as f:
            json.dump({"model": embed_model,
                       "vectors": {k: [round(x, 5) for x in v] for k, v in self.embeddings.items()}}, f)

    # ---------- BM25 ----------
    def _prep_bm25(self, k1: float = 1.4, b: float = 0.75):
        self.k1, self.b = k1, b
        self.doc_tokens = [Counter(tokenize(p.title + " " + p.locator + " " + clean_for_index(p.text)))
                           for p in self.passages]
        self.doc_len = [sum(c.values()) for c in self.doc_tokens]
        self.avgdl = (sum(self.doc_len) / len(self.doc_len)) if self.doc_len else 1.0
        df: Counter = Counter()
        for c in self.doc_tokens:
            df.update(c.keys())
        n = len(self.passages)
        self.idf = {t: math.log(1 + (n - d + 0.5) / (d + 0.5)) for t, d in df.items()}

    def bm25(self, query: str) -> List[float]:
        q = tokenize(query)
        scores = []
        for c, dl in zip(self.doc_tokens, self.doc_len):
            s = 0.0
            for t in q:
                f = c.get(t)
                if f:
                    s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * dl / self.avgdl))
            scores.append(s)
        return scores

    # ---------- hybrid search ----------
    def search(self, query: str, k: int = 6, scope: str = "all", client=None, rrf_k: int = 60,
               max_per_file: int = 0) -> dict:
        """Return {'method', 'note', 'results': [ {passage, scores...} ]}."""
        idx = [i for i, p in enumerate(self.passages) if scope == "all" or p.kind == scope]
        if not idx:
            return {"method": "none", "note": f"no passages in scope '{scope}'", "results": []}
        bm = self.bm25(query)
        q_terms = set(tokenize(query))
        bm_rank = sorted(idx, key=lambda i: -bm[i])

        method, note, cos = "bm25", "", {}
        if client is not None and self.embeddings:
            try:
                qv = client.embed([_query_prompt(query)])[0]
                cos = {i: _cosine(qv, self.embeddings[self.passages[i].id])
                       for i in idx if self.passages[i].id in self.embeddings}
                method = "hybrid (bm25 + embeddinggemma, RRF)"
            except Exception as e:  # model off / not pulled: keep keyword search working
                note = f"embedding model unavailable, keyword-only ({str(e).splitlines()[0]})"
        elif not self.embeddings:
            note = "index has no embeddings, keyword-only"

        fused: Dict[int, float] = {}
        for r, i in enumerate(bm_rank):
            if bm[i] > 0:
                fused[i] = fused.get(i, 0) + 1 / (rrf_k + r + 1)
        if cos:
            for r, i in enumerate(sorted(cos, key=lambda i: -cos[i])):
                fused[i] = fused.get(i, 0) + 1 / (rrf_k + r + 1)
        ranked, per_file = [], {}
        for i in sorted(fused, key=lambda i: -fused[i]):
            path = self.passages[i].path
            # Optional diversity cap: stop one long file from filling every slot, so a
            # question that spans two sources can still see both.
            if max_per_file and per_file.get(path, 0) >= max_per_file:
                continue
            per_file[path] = per_file.get(path, 0) + 1
            ranked.append(i)
            if len(ranked) == k:
                break
        results = []
        for i in ranked:
            p = self.passages[i]
            matched = sorted(q_terms & set(self.doc_tokens[i].keys()))
            results.append({"passage": p, "rrf": round(fused[i], 5), "bm25": round(bm[i], 3),
                            "cosine": round(cos[i], 4) if i in cos else None, "matched_terms": matched})
        return {"method": method, "note": note, "results": results,
                "max_bm25": round(max(bm[i] for i in idx), 3),
                "max_cosine": round(max(cos.values()), 4) if cos else None}


def build_embeddings(passages: List[Passage], client, progress=None) -> Dict[str, List[float]]:
    vecs: Dict[str, List[float]] = {}
    batch = 16
    for s in range(0, len(passages), batch):
        group = passages[s:s + batch]
        out = client.embed([_doc_prompt(p) for p in group], batch=batch)
        for p, v in zip(group, out):
            vecs[p.id] = v
        if progress:
            progress(min(s + batch, len(passages)), len(passages))
    return vecs
