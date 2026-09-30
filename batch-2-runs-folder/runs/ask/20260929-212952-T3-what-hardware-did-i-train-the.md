# Ask-mode evidence card (OFFLINE run): T3

**Question:** What hardware did I train the Pac-Man agent and the nanoGPT models on?

| Field | Value |
|---|---|
| Mode | ask (standalone; no chat history, no persona) |
| Execution | local |
| Model | `gemma4:e2b-it-qat` (4.6B, Q4_0, digest `07ea59a47401`) |
| Embedding model | `embeddinggemma` |
| Runtime | ollama 0.35.0 |
| Internet at run time | **offline** |
| Timestamp | 2026-09-29T21:29:01 |

## Expected (written before running)

- Type: connects two sources
- Expected behavior: Both ran on a cloud Linux machine with 2 CPU cores and no GPU (Pac-Man README: Cloud Linux VM, PyTorch on CPU; nanoGPT README: Cloud Linux container, x86-64, Python 3.11.15, PyTorch 2.14.0). Citations to both READMEs.
- Expected source(s): `vault/raw/assignments/pacman-dqn-README.md`, `vault/raw/assignments/custom-llm-README.md`
- Expected passage: “cloud linux vm, 2 cpu cores”
- Expected passage: “cloud linux container, x86-64, 2 cpu cores”

## Retrieved passages (hybrid (bm25 + embeddinggemma, RRF), scope `raw`, top 10)

| Label | Source path | Location | BM25 | Cosine | Matched terms |
|---|---|---|---|---|---|
| S1 | `vault/raw/course-slides/haas-class3.html` | slide 70: Train an Agent to Play Ms. Pac-Man (part: End Project: Pac-Man DQN) | 15.186 | 0.4901 | agent, man, pac, train |
| S2 | `vault/raw/course-slides/haas-class3.html` | slide 83: Pac-Man Notebook Setup (part: Optional Self-Study) | 14.212 | 0.4786 | agent, hardware, man, pac, train |
| S3 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > Actual training budget (training_summary.json) | 12.144 | 0.5322 | hardware, man, pac, train |
| S4 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) | 14.235 | 0.4591 | agent, man, pac, train |
| S5 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > My three settings | 10.985 | 0.4751 | agent, man, pac, train |
| S6 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > How the agent works, in plain language | 12.786 | 0.4328 | agent, man, pac, train |
| S7 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened | 12.802 | 0.4255 | agent, man, model, pac, train |
| S8 | `vault/raw/assignments/custom-llm-README.md` | Class 4: Building a Custom LLM (nanoGPT, word tokens) | 7.264 | 0.5601 | model, nanogpt, train |
| S9 | `vault/raw/assignments/custom-llm-README.md` | Class 4: Building a Custom LLM (nanoGPT, word tokens) > 2. The runs | 7.789 | 0.4806 | hardware, nanogpt, train |

<details><summary>S1 — vault/raw/course-slides/haas-class3.html — slide 70: Train an Agent to Play Ms. Pac-Man (part: End Project: Pac-Man DQN)</summary>

> Train an Agent to Play Ms. Pac-Man
> 
> Open the Pac-Man project on GitHub →
> 
> Open the notebook in Google Colab →
> 
> Run it in Google Colab, or clone the project for Jupyter or VS Code.
> 
> - Choose exploration, episodes, and learning rate.
> 
> - Select Run All to train the ready-made agent.
> 
> - Watch gameplay and compare the before/after scores.
> 
> Using Claude Code or Codex? The notebook tells it to ask for your three choices before training.
> 
> The notebook is self-contained and installs its dependencies. Exploration is a fixed random-action probability after a short warm-up. Start with five episodes to check setup; longer training does not guarantee good play. The public GitHub repository is the canonical project source, and the Colab link opens its main-branch notebook directly.

</details>

<details><summary>S2 — vault/raw/course-slides/haas-class3.html — slide 83: Pac-Man Notebook Setup (part: Optional Self-Study)</summary>

> Pac-Man Notebook Setup
> 
> Download the notebook → · Setup and publishing guide
> 
> - Colab: File → Upload notebook. Select a GPU under Runtime → Change runtime type if available.
> 
> - Local: open the notebook in Jupyter or VS Code and select a Python kernel.
> 
> - Choose your exploration, episodes, and learning rate, then Run All.
> 
> - Start with five episodes to check setup. Download the results ZIP when finished.
> 
> The notebook handles setup, training, GIFs, plots, checkpoints, and evaluation. Read the code to connect each step to the RL concepts.
> 
> Optional: Build an agent from scratch with AI.
> 
> ALE setup reference checked during revision: https://ale.farama.org/getting-started/ Current ale-py packages include ROMs; avoid mixing obsolete AutoROM instructions with a modern install. Hardware availability is not a guarantee that the selected operations are supported or that training will be fast.

</details>

<details><summary>S3 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > Actual training budget (training_summary.json)</summary>

> | | |
> |---|---|
> | Status | completed (not interrupted) |
> | Completed episodes | 300 / 300 |
> | Decisions | 173,434 |
> | Learning updates | 43,109 |
> | Elapsed time | 1,996 s (≈ 33 min, including periodic demos) |
> | Hardware | Cloud Linux VM, 2 CPU cores, **no GPU** (PyTorch on CPU) |
> | Software | Python 3.11.15, torch 2.14.0, gymnasium 1.3.0, ale-py 0.11.2 (full list in `config.json`) |
> 
> Per-episode log: [`training.csv`](results/training.csv). Checkpoint demo scores: [`demo_scores.json`](results/demo_scores.json). Baseline: [`baseline.json`](results/baseline.json).
> 
> **Checkpoints:** the `.pt` playback checkpoints (untrained, every 25 episodes, and final `trained.pt`; about 6.8 MB each) are kept out of the repo files and attached to the GitHub release [**v1-final-run**](https://github.com/jdnathanson33/pacman-dqn-assignment2/releases/tag/v1-final-run). A copy of all 14 checkpoints is also kept locally, outside the repo.

</details>

<details><summary>S4 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI)</summary>

> I trained the course's Deep Q-Network (DQN) on Atari Ms. Pac-Man. I changed only three settings: exploration, episodes, and learning rate. The untrained and trained agents were scored on the same five evaluation games.
> 
> **Result:** the mean evaluation score went from **492.0 → 604.0 (+112.0)**. Most of that gain comes from one strong game (1,420); three of the five games scored lower after training. So this run shows limited learning, not a clear improvement.

</details>

<details><summary>S5 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > My three settings</summary>

> | Setting | Value | Why |
> |---|---|---|
> | Exploration | **0.10** | This is close to the final exploration level in standard DQN. The agent still tries new routes, but training play (10% random) stays close to evaluation play (5% random). The default of 0.20 wastes many lives on random moves. |
> | Episodes | **300** | A real training budget that fit in about 33 minutes on CPU. It also produces 12 intermediate GIFs and checkpoints. |
> | Learning rate | **0.0001** | The standard, stable Adam learning rate for DQN (and the notebook's reference value). I kept it so the run would not diverge. |
> 
> All other settings were left at the notebook's fixed values. Evaluation was unchanged: seeds 101/202/303/404/505, 5% exploration, and a limit of 3,000 decisions per game. See [`config.json`](results/config.json).

</details>

<details><summary>S6 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > How the agent works, in plain language</summary>

> - **Observations:** the agent sees the **last four game screens**, shrunk to 84 × 84 grayscale. Four frames instead of one let it tell which way Ms. Pac-Man and the ghosts are moving.
> - **Actions:** it picks one of **9 joystick moves**: no-op, up, right, left, down, and the four diagonals. Each choice is held for 4 game frames.
> - **Rewards:** **game points** from pellets, power pellets, eaten ghosts, and fruit. During training, each reward is clipped to between −1 and +1, so the agent only learns "points or no points." The scores reported above are the real game scores.
> - **Learning:** the network estimates how much future reward each move will bring. It stores recent experience in a replay memory and learns from random batches of it. It usually picks the move with the highest estimate, and a random move 10% of the time.

</details>

<details><summary>S7 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened</summary>

> …agent reaches more rewarding situations, its value targets get larger and change more. It shows that lower loss is not the same thing as better play.
> 
> - **The periodic single-game demo (seed 101) did not improve steadily.** Scores by episode: 25 → 920, 50 → 860, 75 → 840, 100 → 700, 125 → 1,250, 150 → 530, 175 → 460, 200 → 170, 225 → 610, 250 → 270, 275 → 530, 300 → 310. The agent's quality swung from one checkpoint to the next. The episode-125 checkpoint looked stronger on this one game than the final model.
> 
> - **Gameplay:** in the first 20 seconds, the untrained and best trained GIFs look similar. Both collect pellets along corridors and lose a life to a ghost fairly early. The trained agent did not visibly avoid ghosts. Trained games were also shorter on average: 535 decisions vs. 589 before.

</details>

<details><summary>S8 — vault/raw/assignments/custom-llm-README.md — Class 4: Building a Custom LLM (nanoGPT, word tokens)</summary>

> **JD Nathanson · Fundamentals of Agentic AI · Berkeley Haas, Fall 2026**
> 
> I trained two tiny word-level nanoGPT models from scratch (2 blocks, 4 heads, 64-number embeddings, 48-token context). Both use the same settings; only the corpus changes.
> 
> 1. **Starter:** the supplied classroom corpus only.
> 2. **Expanded:** the classroom corpus plus my own teaching files for two extension-eval categories, **opposites** and **spatial relations**.
> 
> Both models ran the fixed 48-case language eval suite before and after training. I chat with the expanded model through the supplied terminal interface. This is a tiny model that continues short sentences. It is not a general assistant, and nothing below should be read as "it understands language."

</details>

<details><summary>S9 — vault/raw/assignments/custom-llm-README.md — Class 4: Building a Custom LLM (nanoGPT, word tokens) > 2. The runs</summary>

> | | Experiment 1: starter | Experiment 2: expanded |
> 
> |---|---|---|
> 
> | Run ID | `20260923T061024_781755Z` | `20260923T061247_852296Z` |
> 
> | Completed steps | 3,000 / 3,000 (not interrupted) | 3,000 / 3,000 (not interrupted) |
> 
> | Training time | 24.3 s | 29.5 s |
> 
> | Hardware | Cloud Linux container, x86-64, 2 CPU cores, no GPU. Python 3.11.15, PyTorch 2.14.0 | same |
> 
> | Parameters | 111,872 | 126,080 (the embedding table grows with the vocabulary) |
> 
> | Unique passages (after dedup) | 4,592 (6,360 generated − 160 reserved eval passages − 1,608 duplicates) | 9,767 (4,592 classroom + **5,175 new**) |
> 
> | Train / validation split | 4,132 / 460 (90/10 by passage, seed 42) | 8,790 / 977 |
> 
> | Vocabulary (incl. `<UNK>` `<BOS>` `<EOS>`) | 136 (133 types, all retained) | 358 (355 types, all retained; under the 509 cap) |
> 
> | Training / held-out unknown-token rate | 0.00% / 0.00% | 0.00% / 0.00% |

</details>

## Actual Gemma answer

```text
The Pac-Man agent was trained on a Cloud Linux VM with 2 CPU cores and no GPU, using PyTorch on CPU [S3]. The nanoGPT models were trained on a Cloud Linux container with x86-64 architecture, 2 CPU cores, and no GPU, using Python 3.11.15 and PyTorch 2.14.0 [S9].
```

## Citations

- [S3] → `vault/raw/assignments/pacman-dqn-README.md` — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > Actual training budget (training_summary.json)
- [S9] → `vault/raw/assignments/custom-llm-README.md` — Class 4: Building a Custom LLM (nanoGPT, word tokens) > 2. The runs

## Automatic citation check

- Verdict: **citations_check_passed**
- “The Pac-Man agent was trained on a Cloud Linux VM with 2 CPU cores and no GPU, using PyTorch on CPU [S3].” → ['S3'], word overlap 0.62
- “The nanoGPT models were trained on a Cloud Linux container with x86-64 architecture, 2 CPU cores, and no GPU, using Python 3.11.15 and PyTor” → ['S9'], word overlap 0.78

## Timing

50.43 s wall · model load 0.0 s · prompt 2780 tokens in 43.77 s · answer 84 tokens at 12.74 tokens/s

## Assessment (human, after opening the cited passages)

**PASS after a documented fix.** Both expected passages were retrieved: Pac-Man § Actual training budget at S3, and nanoGPT § 2. The runs at S9. The answer's two claims match those rows exactly: Cloud Linux VM, 2 CPU cores, no GPU, PyTorch on CPU (S3); Cloud Linux container, x86-64, 2 CPU cores, no GPU, Python 3.11.15, PyTorch 2.14.0 (S9). **Earlier failure:** in the first online rehearsal the nanoGPT passage was not retrieved. It ranked outside the top 8, and Gemma answered the nanoGPT half with unrelated corpus details (runs/ask/20260929-210311-T3-…). Fix: link URLs in README tables are stripped before scoring, and a per-file cap stops one file taking every slot. Both fixes are in `wiki_harness/retrieval.py`.

_Reviewed by JD + Claude after opening each cited passage in `vault/raw/`._
