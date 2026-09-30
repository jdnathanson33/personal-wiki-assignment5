# Ask-mode tests (offline run)

All four tests ran with **Wi-Fi off** on 2026-09-29 at 21:28–21:30 PDT, after the CLI and the Ollama server were restarted. Model: `gemma4:e2b-it-qat` (Q4_0, digest `07ea59a47401`). Embeddings: `embeddinggemma`. Runtime: Ollama 0.35.0. Execution: **local**. Every card records `internet_at_run_time: offline`.

The questions and expected passages were written in [`tests/ask_questions.json`](../tests/ask_questions.json) **before** any retrieval or model run. That file is outside `vault/`, so the harness can never retrieve the answer key.

| Test | Question | Expected passage retrieved? | Gemma answer (short) | Citations check out? | Result |
|---|---|---|---|---|---|
| [T1](../runs/ask/20260929-212806-T1-what-was-the-mean-evaluation-score.md) | Mean Pac-Man eval score before and after training? | ✅ rank 1 | “492.0 before … 604.0 after [S2]” | ✅ S2 = eval table, Mean row | **Pass** |
| [T2](../runs/ask/20260929-212900-T2-in-my-networking-app-what-stops.md) | What stops a user handing a contact to another account? (reworded) | ✅ rank 6 of 10 | RLS in Postgres [S5]; `UPDATE` needs `USING` + `WITH CHECK` so `user_id` can't be set to someone else [S6] | ✅ S5 intro, S6 § The four policies | **Pass** (weak rank) |
| [T3](../runs/ask/20260929-212952-T3-what-hardware-did-i-train-the.md) | Hardware for Pac-Man and nanoGPT? (two sources) | ✅ both (S3, S9) | Cloud Linux VM, 2 CPU cores, no GPU [S3]; cloud Linux container, x86-64, 2 CPU cores, no GPU, Py 3.11.15, PyTorch 2.14.0 [S9] | ✅ both rows match | **Pass after fix** |
| [T4](../runs/ask/20260929-213021-T4-what-grade-did-i-receive-on.md) | What grade did I get on the networking tracker? (not in wiki) | n/a (tempting “Grading evidence” passages retrieved) | `INSUFFICIENT EVIDENCE: The provided passages do not state the grade…` | n/a | **Pass** |

Each linked card contains the full retrieved passages with paths, scores, and matched terms. It also has the exact answer, the citation mapping, the automatic citation check, timing, and my written assessment after I opened each cited passage.

## What failed first, and what changed

| When | What happened | Cause | Change | Evidence |
|---|---|---|---|---|
| Rehearsal 1 (online, top-8) | **T3 half-wrong.** The nanoGPT hardware passage was not retrieved, so Gemma described the corpus instead of hardware. It did not invent hardware. | The nanoGPT “The runs” table is full of long run-folder links that diluted both keyword and embedding scores. Pac-Man passages also filled most slots. | Strip link URLs before scoring (`clean_for_index`). Cap passages per file. | [failed card](../runs/ask/20260929-210311-T3-what-hardware-did-i-train-the.md) → [fixed card](../runs/ask/20260929-211608-T3-what-hardware-did-i-train-the.md) |
| Fix check (online, cap 4/file) | T3 fixed, but **T2's key passage dropped out**: rank 6, and only 4 networking passages were allowed. | The cap was too tight when the answer lives in one long file. | `top_k` 8 → 10, cap 4 → 6, context budget 7,000 → 8,000 chars. | [retrieval check](../runs/eval/20260929-211536-retrieval-check.json) → [offline retrieval check](../runs/eval/20260929-212718-retrieval-check.json) |

Summary files: [offline eval summary](../runs/eval/20260929-213021-ask-tests.json) and [offline retrieval check](../runs/eval/20260929-212718-retrieval-check.json). The full terminal transcript is in [offline/offline-demo-20260929-212330.txt](offline/offline-demo-20260929-212330.txt).

## Honest caveats

- A passing citation check is mechanical. It confirms that labels exist, that every sentence is cited, and that numbers appear in the cited passage. I also read each cited passage myself (assessments in the cards).
- T2 depends on the tenth retrieval slot being generous. With a stricter top-k it fails. See the README's limitation section.
- The tests are few (4) and I wrote them knowing the sources, so they show the workflow works, not how accurate it is in general.
