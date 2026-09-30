"""Check an answer's citations against the passages that were actually retrieved.

A citation is not proof by itself, so the harness runs three mechanical checks:
  1. every [S#] label refers to a passage that was shown to the model;
  2. every factual sentence carries at least one label;
  3. every number in a sentence appears in the passages it cites
     (catches the most common silent hallucination: a wrong figure).
It also reports word overlap per sentence as a rough "is this really in there?"
signal. A human still has to read the cited passage; the evidence cards leave
room for that assessment.
"""
from __future__ import annotations

import re
from typing import Dict, List

from .retrieval import tokenize

LABEL = re.compile(r"\[([SN])(\d+)\]")
NUMBER = re.compile(r"(?<![\w.])\d[\d,]*(?:\.\d+)?%?")


def _norm_num(s: str) -> str:
    s = s.replace(",", "").rstrip("%")
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    return s


ABBREV = re.compile(r"\b(Ms|Mr|Mrs|Dr|St|vs|e\.g|i\.e|etc|approx|No)\.$", re.I)


def split_sentences(text: str) -> List[str]:
    raw = re.split(r"(?<=[.!?])\s+(?=[A-Z(\[`*\"'])|\n+", text.strip())
    parts: List[str] = []
    for piece in raw:
        # Re-join splits after abbreviations such as "Ms. Pac-Man" or "e.g. Colab".
        if parts and ABBREV.search(parts[-1]):
            parts[-1] = parts[-1] + " " + piece
        else:
            parts.append(piece)
    return [p.strip() for p in parts if p and p.strip() and not re.fullmatch(r"(\[[SN]\d+\])+", p.strip())]


def is_insufficient(answer: str) -> bool:
    return answer.strip().upper().startswith("INSUFFICIENT EVIDENCE")


def check(answer: str, passages: Dict[str, str], prefix: str = "S") -> dict:
    """passages: {'S1': text, ...}. Returns a structured report."""
    used = [f"{p}{n}" for p, n in LABEL.findall(answer) if p == prefix]
    invalid = sorted(set(u for u in used if u not in passages))
    if is_insufficient(answer):
        return {"verdict": "insufficient_evidence", "labels_used": sorted(set(used)), "invalid_labels": invalid,
                "sentences": [], "uncited_sentences": [], "unsupported_numbers": []}
    sentences, uncited, bad_numbers = [], [], []
    for s in split_sentences(answer):
        if s.upper().startswith("NOT IN SOURCES"):
            sentences.append({"sentence": s, "labels": [], "note": "declared gap"})
            continue
        labels = [f"{p}{n}" for p, n in LABEL.findall(s) if p == prefix]
        body = LABEL.sub("", s)
        cited_text = " ".join(passages.get(l, "") for l in labels)
        cited_nums = {_norm_num(x) for x in NUMBER.findall(cited_text)}
        nums = [x for x in NUMBER.findall(body)]
        missing_nums = [x for x in nums if _norm_num(x) not in cited_nums]
        words = set(tokenize(body))
        overlap = round(len(words & set(tokenize(cited_text))) / len(words), 2) if words else 1.0
        item = {"sentence": s, "labels": labels, "word_overlap_with_cited": overlap}
        if missing_nums:
            item["numbers_not_in_cited_passages"] = missing_nums
            bad_numbers += missing_nums
        if not labels and len(words) >= 3:
            uncited.append(s)
        sentences.append(item)
    if invalid or not used:
        verdict = "unsupported_citations" if invalid else "no_citations"
    elif bad_numbers or uncited:
        verdict = "needs_review"
    else:
        verdict = "citations_check_passed"
    return {"verdict": verdict, "labels_used": sorted(set(used), key=lambda x: int(x[1:])), "invalid_labels": invalid,
            "sentences": sentences, "uncited_sentences": uncited, "unsupported_numbers": bad_numbers}
