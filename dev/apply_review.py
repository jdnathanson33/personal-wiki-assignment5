"""Apply my human review of the Gemma-drafted notes (run once after the first ingest).

1. Link repair: two README headings contain Markdown links, which break Obsidian heading links.
   Those links now point at the file and use the plain heading text (the ingest code was fixed too).
2. Content corrections: every statement I found wrong or misleading after reading each note
   against its source sections. Each change is logged in evidence/wiki-review.md.
3. Every note gets `reviewed: true`, so a later re-ingest keeps these checked notes and saves any
   new Gemma draft to runs/ingest/<time>/drafts/ instead of overwriting them.
Original sources in vault/raw are not touched."""
import re, sys
from datetime import date
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
W = ROOT / "vault" / "wiki"

LINK_FIXES = [  # (broken markup, repaired markup)
 ("[[raw/assignments/pacman-dqn-README.md#Actual training budget ([`training_summary.json`](results/training_summary.json))|§ Actual training budget ([training_summary.json](results/training_summary.json))]]",
  "[[raw/assignments/pacman-dqn-README.md|§ Actual training budget (training_summary.json)]]"),
 ("[[raw/assignments/pacman-dqn-README.md#Evaluation: all five games ([`comparison.json`](results/comparison.json))|§ Evaluation: all five games ([comparison.json](results/comparison.json))]]",
  "[[raw/assignments/pacman-dqn-README.md|§ Evaluation: all five games (comparison.json)]]"),
 ("Evaluation: all five games ([comparison.json](results/comparison.json))", "Evaluation: all five games (comparison.json)"),
 ("Actual training budget ([training_summary.json](results/training_summary.json))", "Actual training budget (training_summary.json)"),
]

FIXES = [  # (note, old text, new text, why)
 ("Projects/Tiny nanoGPT Model.md",
  "which are used to evaluate language understanding based on corpus size. These models are characterized by specific settings and are tested against a fixed 48-case language evaluation suite.",
  "with identical settings; only the training corpus changed. Both were scored on the same fixed 48-case language eval suite, and the README stresses that the results should not be read as the model understanding language.",
  "Draft claimed the models evaluate 'language understanding based on corpus size'; the README explicitly says not to read results as understanding."),
 ("Projects/Tiny nanoGPT Model.md",
  "The training split for both experiments was 4,132 / 460 passages (90/10 by passage, seed 42)",
  "The train/validation split was 4,132 / 460 passages for the starter run and 8,790 / 977 for the expanded run (90/10 by passage, seed 42)",
  "Wrong: 4,132/460 applies only to the starter run; the expanded run was 8,790/977 (README §2 The runs)."),
 ("Concepts/Evaluation Design.md",
  "To test the impact of training budget, the number of episodes was changed from 300 to 1,000 while keeping exploration at 0.10 and the learning rate at 0.0001",
  "The proposed next experiment (not yet run) changes only the number of episodes, from 300 to 1,000, and keeps exploration at 0.10 and the learning rate at 0.0001, so any change in the five evaluation scores can be attributed to the training budget",
  "Draft stated the 1,000-episode run as done; the README describes it as the next experiment."),
 ("Concepts/Evaluation Design.md",
  "This process is used to determine necessary changes to the model's training parameters.",
  "In both projects the evaluation was small or public, so the results show limited evidence, and each README proposes a better-controlled next experiment.",
  "Vague claim not stated in the sources."),
 ("Concepts/Training Loss Curves.md",
  "Similarly, for nanoGPT, loss flattening indicates that the model has reached a point where further loss reduction is not possible, and losses from different experiments cannot be directly compared.",
  "For nanoGPT, loss fell quickly and then flattened at a floor above zero, because the template slots are filled at random; losses from the two experiments cannot be compared.",
  "Overstated ('further reduction is not possible'); README explains the floor comes from randomly filled template slots."),
 ("Concepts/Cloud Deployment.md",
  "This process is demonstrated by deploying a full-stack web app using a stack like Next.js, Supabase, and Vercel.",
  "The Class 2 assignment named Next.js + Supabase + Vercel; my Networking Tracker was deployed on Vercel with Neon Postgres and Neon Auth.",
  "Implied I deployed with Supabase; my README shows Neon + Vercel (Supabase is the class slide's suggested stack)."),
 ("Concepts/Context Windows.md",
  "which can hold content equivalent to the entire Lord of the Rings trilogy",
  "enough to hold two copies of the Lord of the Rings trilogy (about 500,000 tokens each)",
  "Slide says 1M tokens holds two copies of the ~500,000-token trilogy."),
 ("Course/Class 3 - Machine Learning.md",
  "- The process of AI history involves checking whether learning generalizes",
  "- The first half of the class covers AI history and the landscape and checks whether learning generalizes",
  "Garbled merge of two agenda items on the 'Today's Route' slide."),
 ("Course/Class 3 - Machine Learning.md",
  "- The route for AI history includes",
  "- The class route includes",
  "Same slide: the route is the class agenda, not 'AI history'."),
 ("Course/Class 5 - LLMs Prompting and Retrieval.md",
  "Fine-tuning and RLHF are processes labs perform to make a base model an assistant, impacting design choices like \"Anthropic values\"",
  "Fine-tuning, RLHF, and alignment are what labs do under the hood, so ideas like \"Anthropic values\" or \"OpenAI personality\" become real design choices rather than magic",
  "Reworded to match the slide's meaning."),
 ("Course/Fundamentals of Agentic AI.md",
  "This course covers the fundamentals of Agentic AI across seven classes, starting with code and programming, moving through software systems, machine learning foundations, deep learning, and finally focusing on LLM behavior, prompting, and retrieval. The curriculum is structured to build practical skills, culminating in building working AI workflows.",
  "Fundamentals of Agentic AI is a seven-class course; this wiki covers the first five, which move from code and programming through software systems, machine learning, and deep learning to LLM behavior, prompting, and retrieval. Each class ends in a hands-on assignment that I documented in my own repository.",
  "Draft implied the LLM class is the final class; the slides only cover five of seven classes."),
 ("Projects/Personal Wiki Project.md",
  "must consist of 3+ original notes",
  "must be built from 3+ original sources",
  "Slide says '3+ originals' (sources), not notes."),
]

def set_description(text):
    body = text.split("\n---\n", 1)[1]
    summary = body.split("# ", 1)[1].split("\n", 2)[2].strip().split("\n")[0]
    first = re.split(r"(?<=[.!?])\s", summary, maxsplit=1)[0].replace('"', "'")
    return re.sub(r'^description: ".*"$', f'description: "{first}"', text, count=1, flags=re.M)

log = ["# Wiki review log", "",
       f"I read every Gemma-drafted note against the source sections it was built from ({date.today()}). "
       "Below is every correction. Notes not listed were accurate. After this review every note has `reviewed: true`.",
       "", "## Link repairs", "",
       "- Two Pac-Man README headings contain Markdown links (`[comparison.json](...)`), which break Obsidian heading links. "
       "Affected notes now link to the file with the plain heading text. The ingest code was fixed so this doesn't recur.",
       "", "## Content corrections", "", "| Note | Problem in the Gemma draft | Correction |", "|---|---|---|"]
missing = []
for p in sorted(W.rglob("*.md")):
    t = p.read_text()
    for a, b in LINK_FIXES:
        t = t.replace(a, b)
    rel = p.relative_to(W).as_posix()
    for note, old, new, why in FIXES:
        if note == rel:
            if old not in t:
                missing.append((note, old[:60]))
                continue
            t = t.replace(old, new)
            log.append(f"| [[{p.stem}]] | {why} | “{new[:160]}{'…' if len(new) > 160 else ''}” |")
    t = set_description(t)
    t = re.sub(r"^reviewed: (true|false)$", "reviewed: true", t, flags=re.M)
    if "review_note:" not in t:
        t = t.replace("reviewed: true\n", f'reviewed: true\nreview_note: "Checked against sources by JD + Claude on {date.today()}; see evidence/wiki-review.md"\n', 1)
    p.write_text(t)
(ROOT / "evidence").mkdir(exist_ok=True)
(ROOT / "evidence" / "wiki-review.md").write_text("\n".join(log) + "\n")
print("not applied:", missing or "none")
