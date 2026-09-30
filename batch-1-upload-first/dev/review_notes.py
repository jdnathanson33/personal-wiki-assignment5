"""Review aid: for each bullet in each generated note, compare it with the source sections the
note was built from. Flags numbers that don't appear in those sections and low word overlap.
Output is for the human reviewer; it does not change any note."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from wiki_harness.config import load_settings
from wiki_harness.sources import load_sections
from wiki_harness.ingest import _select_sections
from wiki_harness.retrieval import tokenize
from wiki_harness.citations import NUMBER, _norm_num

s = load_settings()
plan = json.load(open(s.plan))
out = []
for n in plan["notes"]:
    p = s.wiki / n["folder"] / f"{n['title']}.md"
    if not p.exists():
        continue
    src = ""
    for so in n["sources"]:
        _, secs = load_sections(s.vault / so["path"])
        src += " ".join(x.text for x in _select_sections(secs, so["sections"]))
    src_tok, src_nums = set(tokenize(src)), {_norm_num(x) for x in NUMBER.findall(src)}
    text = p.read_text()
    body = text.split("## Related notes")[0].split("\n---\n", 1)[-1]
    for line in body.splitlines():
        if not (line.startswith("- ") or (line and not line.startswith(("#", "---")) and ":" not in line[:15])):
            continue
        claim = re.sub(r"\(\[\[.*?\]\]\)|\(\[.*?\]\(.*?\)\)", "", line)
        claim = re.sub(r"\[\[.*?\|(.*?)\]\]", r"\1", claim)
        w = set(tokenize(claim))
        if len(w) < 4:
            continue
        ov = len(w & src_tok) / len(w)
        nums = [x for x in NUMBER.findall(claim) if _norm_num(x) not in src_nums]
        missing = sorted(w - src_tok)
        if ov < 0.72 or nums:
            out.append(f"{n['title']} | overlap {ov:.2f} | nums {nums} | new words {missing[:10]}\n    {claim.strip()[:220]}")
print("\n".join(out)); print(len(out), "flagged")
