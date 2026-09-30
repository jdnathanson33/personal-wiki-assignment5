# Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI)

I trained the course's Deep Q-Network (DQN) on Atari Ms. Pac-Man. I changed only three settings: exploration, episodes, and learning rate. The untrained and trained agents were scored on the same five evaluation games.

**Result:** the mean evaluation score went from **492.0 → 604.0 (+112.0)**. Most of that gain comes from one strong game (1,420); three of the five games scored lower after training. So this run shows limited learning, not a clear improvement.

## How to run

1. Open [`pacman_dqn.ipynb`](pacman_dqn.ipynb) in Google Colab (Runtime → Change runtime type → GPU), or locally in Jupyter or VS Code with a Python 3.11–3.13 kernel. Keep `pacman_player.py` in the same folder as the notebook.
2. The three settings are in section 1. Choose **Run All**; the notebook installs its own packages.
3. Each run writes a new folder under `pacman_runs/` and a ZIP of that folder. The evidence from my run is in [`results/`](results/).

The notebook in this repo is the **executed final run**, with all outputs visible.

## My three settings

| Setting | Value | Why |
|---|---|---|
| Exploration | **0.10** | This is close to the final exploration level in standard DQN. The agent still tries new routes, but training play (10% random) stays close to evaluation play (5% random). The default of 0.20 wastes many lives on random moves. |
| Episodes | **300** | A real training budget that fit in about 33 minutes on CPU. It also produces 12 intermediate GIFs and checkpoints. |
| Learning rate | **0.0001** | The standard, stable Adam learning rate for DQN (and the notebook's reference value). I kept it so the run would not diverge. |

All other settings were left at the notebook's fixed values. Evaluation was unchanged: seeds 101/202/303/404/505, 5% exploration, and a limit of 3,000 decisions per game. See [`config.json`](results/config.json).

## What I expected vs. what happened

**Expected:** a modest improvement. With low exploration and a stable learning rate, I expected the agent to learn to clear more pellets than the untrained network. I did not expect expert play from 300 games with a 5,000-decision replay memory.

**Observed:**

- **Training scores improved a little, and noisily.** The 25-game average rose from about 500 (episode 25) to about 860 (episode 75). It then slipped back to roughly 540–690 between episodes 175 and 250, peaked again near 940 around episode 272, and finished at about 670.
- **Best single training game:** 4,310 at episode 272.
- **50-episode means:** 546 → 777 → 743 → 636 → 594 → 796.
- **Loss went up, not down.** It climbed from about 0.02 to about 0.10–0.16 and ended near 0.09. This is common in DQN: as the agent reaches more rewarding situations, its value targets get larger and change more. It shows that lower loss is not the same thing as better play.
- **The periodic single-game demo (seed 101) did not improve steadily.** Scores by episode: 25 → 920, 50 → 860, 75 → 840, 100 → 700, 125 → 1,250, 150 → 530, 175 → 460, 200 → 170, 225 → 610, 250 → 270, 275 → 530, 300 → 310. The agent's quality swung from one checkpoint to the next. The episode-125 checkpoint looked stronger on this one game than the final model.
- **Gameplay:** in the first 20 seconds, the untrained and best trained GIFs look similar. Both collect pellets along corridors and lose a life to a ghost fairly early. The trained agent did not visibly avoid ghosts. Trained games were also shorter on average: 535 decisions vs. 589 before.

### Evaluation: all five games ([`comparison.json`](results/comparison.json))

| Game (seed) | Before (untrained) | After (300 episodes) |
|---|---:|---:|
| 1 (101) | 350 | 310 |
| 2 (202) | 500 | 410 |
| 3 (303) | 320 | **1,420** |
| 4 (404) | 800 | 290 |
| 5 (505) | 490 | 590 |
| **Mean** | **492.0** | **604.0** |

No game reached the time limit, before or after. Every game ended at game over.

### Training dashboard

![Training dashboard](results/training_dashboard.png)

### Gameplay (first 20 s of game time, 4× speed)

| Untrained | Best trained game (of 5) |
|---|---|
| ![untrained](results/demos/episode_0000.gif) | ![best trained](results/demos/final_best.gif) |

Intermediate samples (seed 101, one every 25 episodes):

| 25 | 50 | 75 | 100 |
|---|---|---|---|
| ![](results/demos/episode_0025.gif) | ![](results/demos/episode_0050.gif) | ![](results/demos/episode_0075.gif) | ![](results/demos/episode_0100.gif) |
| **125** | **150** | **175** | **200** |
| ![](results/demos/episode_0125.gif) | ![](results/demos/episode_0150.gif) | ![](results/demos/episode_0175.gif) | ![](results/demos/episode_0200.gif) |
| **225** | **250** | **275** | **300** |
| ![](results/demos/episode_0225.gif) | ![](results/demos/episode_0250.gif) | ![](results/demos/episode_0275.gif) | ![](results/demos/episode_0300.gif) |

## Actual training budget ([`training_summary.json`](results/training_summary.json))

| | |
|---|---|
| Status | completed (not interrupted) |
| Completed episodes | 300 / 300 |
| Decisions | 173,434 |
| Learning updates | 43,109 |
| Elapsed time | 1,996 s (≈ 33 min, including periodic demos) |
| Hardware | Cloud Linux VM, 2 CPU cores, **no GPU** (PyTorch on CPU) |
| Software | Python 3.11.15, torch 2.14.0, gymnasium 1.3.0, ale-py 0.11.2 (full list in `config.json`) |

Per-episode log: [`training.csv`](results/training.csv). Checkpoint demo scores: [`demo_scores.json`](results/demo_scores.json). Baseline: [`baseline.json`](results/baseline.json).

**Checkpoints:** the `.pt` playback checkpoints (untrained, every 25 episodes, and final `trained.pt`; about 6.8 MB each) are kept out of the repo files and attached to the GitHub release [**v1-final-run**](https://github.com/jdnathanson33/pacman-dqn-assignment2/releases/tag/v1-final-run). A copy of all 14 checkpoints is also kept locally, outside the repo.

## How the agent works, in plain language

- **Observations:** the agent sees the **last four game screens**, shrunk to 84 × 84 grayscale. Four frames instead of one let it tell which way Ms. Pac-Man and the ghosts are moving.
- **Actions:** it picks one of **9 joystick moves**: no-op, up, right, left, down, and the four diagonals. Each choice is held for 4 game frames.
- **Rewards:** **game points** from pellets, power pellets, eaten ghosts, and fruit. During training, each reward is clipped to between −1 and +1, so the agent only learns "points or no points." The scores reported above are the real game scores.
- **Learning:** the network estimates how much future reward each move will bring. It stores recent experience in a replay memory and learns from random batches of it. It usually picks the move with the highest estimate, and a random move 10% of the time.

## One limitation

**Evaluation is small and noisy, and the agent is unstable.** Five games cannot separate real learning from luck. The +112 improvement comes almost entirely from one game (seed 303), and three of five games got worse. The periodic demos swung from 1,250 to 170 across checkpoints. Reward clipping adds to the problem: the agent can't tell a 10-point pellet from a 200-point ghost. It also has no life-loss penalty, so it has little reason to learn to avoid ghosts. That matches the GIFs, where both agents die early.

## Next experiment

**Change only the number of episodes, from 300 to 1,000**, and keep exploration at 0.10 and the learning rate at 0.0001. The 25-game average was still swinging at the end of this run (about 940 at episode 272, 670 at episode 300), and 43k updates is small for Atari. A DQN typically needs far more experience before it learns to avoid ghosts reliably. Keeping the other two settings fixed means any change in the five evaluation scores can be attributed to the training budget.
