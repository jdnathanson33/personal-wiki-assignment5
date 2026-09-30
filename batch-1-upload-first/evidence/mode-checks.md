# Chat / search / ask mode checks (offline run)

All of these ran with **Wi-Fi off** on 2026-09-29, 21:30–21:34 PDT (`internet: offline` in every header). They come from a script ([`tests/mode_checks_chat.txt`](../tests/mode_checks_chat.txt)) so they are repeatable. Each line is typed into the chat exactly as a user would type it.

Full transcripts: [chat transcript](../runs/chat/20260929-213021-chat.md) · [terminal transcript](offline/offline-demo-20260929-212330.txt) · [separation ask card](../runs/ask/20260929-213323-did-i-train-the-pac-man.md)

| # | Check | What I typed | What the harness did | What Gemma said (short) | Result |
|---|---|---|---|---|---|
| 1 | Capabilities, no lookup | `what can you help me with?` | **No lookup** (“question about the assistant itself”) | Lists study plans, explanations, drafting, reworking replies | ✅ No “insufficient evidence”, no unrelated citations. It skipped mentioning `/notes` and the wiki this time (the rehearsal run did). |
| 2 | Capabilities, no lookup | `what can we do?` | **No lookup** | Four options including note lookups with `/notes` | ✅ |
| 3 | Draft that needs notes | `Draft a 5-step study plan for reviewing reinforcement learning … using my Pac-Man project` | **Notes lookup**: 4 passages [N1–N4] (Class 3 note, Class 3 slides 70 and 72) | 5-step plan citing [N1]–[N4] | ✅ Cited claims match the slides. Plan steps are suggestions. |
| 4 | Follow-up uses conversation | `make that shorter` | **No lookup** (“follow-up on the conversation”); history sent | The same 5 steps, condensed, citations kept | ✅ (fixed: in rehearsal 1 it shortened the *notes* instead of the plan) |
| 5 | Save is explicit | `/save` | Wrote `outputs/drafts/…make-that-shorter.md`, labelled “chat draft (generated; NOT a source)” | — | ✅ Drafts stay out of `vault/` and out of retrieval |
| 6 | A claim made only in chat | `/clear`, then `My favorite model is the 26B MoE and I trained Pac-Man on a GPU.` | Notes lookup (Pac-Man note, README intro, slides) | Restated my claim, then summarized the real run settings with citations | ⚠️ **Limitation**: it did not correct the GPU claim, even though the persona tells it to |
| 7 | Search shows originals only | `./wiki search "hardware used to train the agent" -k 4` | Retrieval only; header says “no text generation” | 4 passages with path, location, scores. #4 is the README § Actual training budget | ✅ No generated answer |
| 8 | Ask ignores chat | `./wiki ask "Did I train the Pac-Man agent on a GPU?"` | New process; no chat history, no persona; retrieves from `vault/raw` only | “…Cloud Linux VM with 2 CPU cores and no GPU [S3]. The notebook setup allows users to select a GPU … in Google Colab [S5].” | ✅ The chat claim was **not** treated as evidence; the answer contradicts it with a citation |

## Notes on check 8's automatic verdict

The saved card says `needs_review; 1 uncited sentence`. That was a **bug in my citation checker**, not in the answer. The sentence splitter broke “Atari **Ms.** Pac-Man” at “Ms.”, so the fragment looked uncited. I fixed the splitter (it now re-joins common abbreviations) and re-ran the checker on the saved answer. The verdict is now `citations_check_passed`. The saved card is left as it was produced.

## Why chat didn't push back (check 6)

The E2B model follows the persona's tone well but ignores the rule “if JD states something the notes contradict, say so.” The retrieved passages here did not include the README's hardware table (the Pac-Man note and README intro ranked higher), so the contradicting evidence wasn't even in front of the model. Ask mode handles this correctly because it retrieves for a question rather than for a statement. A possible improvement: when a chat message contains a factual claim about a project, run an ask-style retrieval on the claim and show the result as a “Check:” line.
