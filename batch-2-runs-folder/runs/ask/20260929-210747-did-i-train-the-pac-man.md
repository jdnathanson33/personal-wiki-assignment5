> **Rehearsal run with internet ON** (model still local). Not the graded offline evidence; kept to show what changed.

# Ask-mode evidence card

**Question:** Did I train the Pac-Man agent on a GPU?

| Field | Value |
|---|---|
| Mode | ask (standalone; no chat history, no persona) |
| Execution | local |
| Model | `gemma4:e2b-it-qat` (4.6B, Q4_0, digest `07ea59a47401`) |
| Embedding model | `embeddinggemma` |
| Runtime | ollama 0.35.0 |
| Internet at run time | **ONLINE** |
| Timestamp | 2026-09-29T21:06:59 |

## Retrieved passages (hybrid (bm25 + embeddinggemma, RRF), scope `raw`, top 8)

| Label | Source path | Location | BM25 | Cosine | Matched terms |
|---|---|---|---|---|---|
| S1 | `vault/raw/course-slides/haas-class3.html` | slide 70: Train an Agent to Play Ms. Pac-Man (part: End Project: Pac-Man DQN) | 15.487 | 0.5639 | agent, man, pac, train |
| S2 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) | 14.514 | 0.553 | agent, man, pac, train |
| S3 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > How the agent works, in plain language | 13.121 | 0.54 | agent, man, pac, train |
| S4 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > Actual training budget (training_summary.json) | 12.215 | 0.5844 | gpu, man, pac, train |
| S5 | `vault/raw/course-slides/haas-class3.html` | slide 83: Pac-Man Notebook Setup (part: Optional Self-Study) | 14.95 | 0.5284 | agent, gpu, man, pac, train |
| S6 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > How to run | 12.935 | 0.5284 | gpu, man, pac |
| S7 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > My three settings | 11.254 | 0.5345 | agent, man, pac, train |
| S8 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened | 12.433 | 0.5087 | agent, man, pac, train |

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

<details><summary>S2 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI)</summary>

> I trained the course's Deep Q-Network (DQN) on Atari Ms. Pac-Man. I changed only three settings: exploration, episodes, and learning rate. The untrained and trained agents were scored on the same five evaluation games.
> 
> **Result:** the mean evaluation score went from **492.0 → 604.0 (+112.0)**. Most of that gain comes from one strong game (1,420); three of the five games scored lower after training. So this run shows limited learning, not a clear improvement.

</details>

<details><summary>S3 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > How the agent works, in plain language</summary>

> - **Observations:** the agent sees the **last four game screens**, shrunk to 84 × 84 grayscale. Four frames instead of one let it tell which way Ms. Pac-Man and the ghosts are moving.
> - **Actions:** it picks one of **9 joystick moves**: no-op, up, right, left, down, and the four diagonals. Each choice is held for 4 game frames.
> - **Rewards:** **game points** from pellets, power pellets, eaten ghosts, and fruit. During training, each reward is clipped to between −1 and +1, so the agent only learns "points or no points." The scores reported above are the real game scores.
> - **Learning:** the network estimates how much future reward each move will bring. It stores recent experience in a replay memory and learns from random batches of it. It usually picks the move with the highest estimate, and a random move 10% of the time.

</details>

<details><summary>S4 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > Actual training budget (training_summary.json)</summary>

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

<details><summary>S5 — vault/raw/course-slides/haas-class3.html — slide 83: Pac-Man Notebook Setup (part: Optional Self-Study)</summary>

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

<details><summary>S6 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > How to run</summary>

> 1. Open [`pacman_dqn.ipynb`](pacman_dqn.ipynb) in Google Colab (Runtime → Change runtime type → GPU), or locally in Jupyter or VS Code with a Python 3.11–3.13 kernel. Keep `pacman_player.py` in the same folder as the notebook.
> 2. The three settings are in section 1. Choose **Run All**; the notebook installs its own packages.
> 3. Each run writes a new folder under `pacman_runs/` and a ZIP of that folder. The evidence from my run is in [`results/`](results/).
> 
> The notebook in this repo is the **executed final run**, with all outputs visible.

</details>

<details><summary>S7 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > My three settings</summary>

> | Setting | Value | Why |
> |---|---|---|
> | Exploration | **0.10** | This is close to the final exploration level in standard DQN. The agent still tries new routes, but training play (10% random) stays close to evaluation play (5% random). The default of 0.20 wastes many lives on random moves. |
> | Episodes | **300** | A real training budget that fit in about 33 minutes on CPU. It also produces 12 intermediate GIFs and checkpoints. |
> | Learning rate | **0.0001** | The standard, stable Adam learning rate for DQN (and the notebook's reference value). I kept it so the run would not diverge. |
> 
> All other settings were left at the notebook's fixed values. Evaluation was unchanged: seeds 101/202/303/404/505, 5% exploration, and a limit of 3,000 decisions per game. See [`config.json`](results/config.json).

</details>

<details><summary>S8 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened</summary>

> …agent reaches more rewarding situations, its value targets get larger and change more. It shows that lower loss is not the same thing as better play.
> 
> - **The periodic single-game demo (seed 101) did not improve steadily.** Scores by episode: 25 → 920, 50 → 860, 75 → 840, 100 → 700, 125 → 1,250, 150 → 530, 175 → 460, 200 → 170, 225 → 610, 250 → 270, 275 → 530, 300 → 310. The agent's quality swung from one checkpoint to the next. The episode-125 checkpoint looked stronger on this one game than the final model.
> 
> - **Gameplay:** in the first 20 seconds, the untrained and best trained GIFs look similar. Both collect pellets along corridors and lose a life to a ghost fairly early. The trained agent did not visibly avoid ghosts. Trained games were also shorter on average: 535 decisions vs. 589 before.

</details>

## Actual Gemma answer

```text
The training was performed on a Cloud Linux VM with 2 CPU cores and no GPU [S4]. However, the Pac-Man Notebook Setup mentions the option to select a GPU under Runtime in Google Colab [S5].
```

## Citations

- [S4] → `vault/raw/assignments/pacman-dqn-README.md` — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > Actual training budget (training_summary.json)
- [S5] → `vault/raw/course-slides/haas-class3.html` — slide 83: Pac-Man Notebook Setup (part: Optional Self-Study)

## Automatic citation check

- Verdict: **citations_check_passed**
- “The training was performed on a Cloud Linux VM with 2 CPU cores and no GPU [S4].” → ['S4'], word overlap 0.78
- “However, the Pac-Man Notebook Setup mentions the option to select a GPU under Runtime in Google Colab [S5].” → ['S5'], word overlap 0.67

## Timing

47.74 s wall · model load 0.0 s · prompt 2305 tokens in 43.19 s · answer 47 tokens at 10.55 tokens/s

## Assessment (human, after opening the cited passages)

_Pending review._
