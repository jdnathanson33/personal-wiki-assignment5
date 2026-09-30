# Ask-mode evidence card

**Question:** What exploration, episodes, and learning rate did I use for the Pac-Man DQN?

| Field | Value |
|---|---|
| Mode | ask (standalone; no chat history, no persona) |
| Execution | local |
| Model | `gemma4:e2b-it-qat` (4.6B, Q4_0, digest `07ea59a47401`) |
| Embedding model | `embeddinggemma` |
| Runtime | ollama 0.35.0 |
| Internet at run time | **offline** |
| Timestamp | 2026-09-29T21:33:24 |

## Retrieved passages (hybrid (bm25 + embeddinggemma, RRF), scope `raw`, top 10)

| Label | Source path | Location | BM25 | Cosine | Matched terms |
|---|---|---|---|---|---|
| S1 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > My three settings | 26.032 | 0.7457 | dqn, episod, exploration, learn, man, pac, rate |
| S2 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) | 26.824 | 0.6396 | dqn, episod, exploration, learn, man, pac, rate |
| S3 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > Next experiment | 25.32 | 0.7007 | dqn, episod, exploration, learn, man, pac, rate |
| S4 | `vault/raw/course-slides/haas-class3.html` | slide 70: Train an Agent to Play Ms. Pac-Man (part: End Project: Pac-Man DQN) | 24.912 | 0.6047 | dqn, episod, exploration, learn, man, pac, rate |
| S5 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened | 20.261 | 0.6323 | dqn, episod, exploration, learn, man, pac, rate |
| S6 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened > Gameplay (first 20 s of game time, 4× speed) | 18.005 | 0.5794 | dqn, episod, man, pac |
| S7 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened > Evaluation: all five games (comparison.json) | 17.164 | 0.5763 | dqn, episod, man, pac |
| S8 | `vault/raw/course-slides/haas-class3.html` | slide 83: Pac-Man Notebook Setup (part: Optional Self-Study) | 18.551 | 0.5082 | episod, exploration, learn, man, pac, rate |
| S9 | `vault/raw/course-slides/haas-class3.html` | slide 71: Show What the Agent Actually Learned (part: End Project: Pac-Man DQN) | 15.919 | 0.5611 | dqn, episod, learn, man, pac |
| S10 | `vault/raw/course-slides/haas-class3.html` | slide 68: A Q-Table Cannot List Every Game Screen (part: Reinforcement Learning) | 13.078 | 0.5003 | dqn, learn, man, pac |

<details><summary>S1 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > My three settings</summary>

> | Setting | Value | Why |
> |---|---|---|
> | Exploration | **0.10** | This is close to the final exploration level in standard DQN. The agent still tries new routes, but training play (10% random) stays close to evaluation play (5% random). The default of 0.20 wastes many lives on random moves. |
> | Episodes | **300** | A real training budget that fit in about 33 minutes on CPU. It also produces 12 intermediate GIFs and checkpoints. |
> | Learning rate | **0.0001** | The standard, stable Adam learning rate for DQN (and the notebook's reference value). I kept it so the run would not diverge. |
> 
> All other settings were left at the notebook's fixed values. Evaluation was unchanged: seeds 101/202/303/404/505, 5% exploration, and a limit of 3,000 decisions per game. See [`config.json`](results/config.json).

</details>

<details><summary>S2 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI)</summary>

> I trained the course's Deep Q-Network (DQN) on Atari Ms. Pac-Man. I changed only three settings: exploration, episodes, and learning rate. The untrained and trained agents were scored on the same five evaluation games.
> 
> **Result:** the mean evaluation score went from **492.0 → 604.0 (+112.0)**. Most of that gain comes from one strong game (1,420); three of the five games scored lower after training. So this run shows limited learning, not a clear improvement.

</details>

<details><summary>S3 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > Next experiment</summary>

> **Change only the number of episodes, from 300 to 1,000**, and keep exploration at 0.10 and the learning rate at 0.0001. The 25-game average was still swinging at the end of this run (about 940 at episode 272, 670 at episode 300), and 43k updates is small for Atari. A DQN typically needs far more experience before it learns to avoid ghosts reliably. Keeping the other two settings fixed means any change in the five evaluation scores can be attributed to the training budget.

</details>

<details><summary>S4 — vault/raw/course-slides/haas-class3.html — slide 70: Train an Agent to Play Ms. Pac-Man (part: End Project: Pac-Man DQN)</summary>

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

<details><summary>S5 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened</summary>

> **Expected:** a modest improvement. With low exploration and a stable learning rate, I expected the agent to learn to clear more pellets than the untrained network. I did not expect expert play from 300 games with a 5,000-decision replay memory.
> 
> **Observed:**
> 
> - **Training scores improved a little, and noisily.** The 25-game average rose from about 500 (episode 25) to about 860 (episode 75). It then slipped back to roughly 540–690 between episodes 175 and 250, peaked again near 940 around episode 272, and finished at about 670.
> 
> - **Best single training game:** 4,310 at episode 272.
> 
> - **50-episode means:** 546 → 777 → 743 → 636 → 594 → 796.
> 
> - **Loss went up, not down.** It climbed from about 0.02 to about 0.10–0.16 and ended near 0.09. This is common in DQN: as the agent reaches more rewarding situations, its value targets get larger and change more. It shows that lower loss is not the same thing as better play.

</details>

<details><summary>S6 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened > Gameplay (first 20 s of game time, 4× speed)</summary>

> | Untrained | Best trained game (of 5) |
> |---|---|
> | ![untrained](results/demos/episode_0000.gif) | ![best trained](results/demos/final_best.gif) |
> 
> Intermediate samples (seed 101, one every 25 episodes):
> 
> | 25 | 50 | 75 | 100 |
> |---|---|---|---|
> | ![](results/demos/episode_0025.gif) | ![](results/demos/episode_0050.gif) | ![](results/demos/episode_0075.gif) | ![](results/demos/episode_0100.gif) |
> | **125** | **150** | **175** | **200** |
> | ![](results/demos/episode_0125.gif) | ![](results/demos/episode_0150.gif) | ![](results/demos/episode_0175.gif) | ![](results/demos/episode_0200.gif) |
> | **225** | **250** | **275** | **300** |
> | ![](results/demos/episode_0225.gif) | ![](results/demos/episode_0250.gif) | ![](results/demos/episode_0275.gif) | ![](results/demos/episode_0300.gif) |

</details>

<details><summary>S7 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened > Evaluation: all five games (comparison.json)</summary>

> | Game (seed) | Before (untrained) | After (300 episodes) |
> |---|---:|---:|
> | 1 (101) | 350 | 310 |
> | 2 (202) | 500 | 410 |
> | 3 (303) | 320 | **1,420** |
> | 4 (404) | 800 | 290 |
> | 5 (505) | 490 | 590 |
> | **Mean** | **492.0** | **604.0** |
> 
> No game reached the time limit, before or after. Every game ended at game over.

</details>

<details><summary>S8 — vault/raw/course-slides/haas-class3.html — slide 83: Pac-Man Notebook Setup (part: Optional Self-Study)</summary>

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

<details><summary>S9 — vault/raw/course-slides/haas-class3.html — slide 71: Show What the Agent Actually Learned (part: End Project: Pac-Man DQN)</summary>

> Show What the Agent Actually Learned
> 
> Pac-Man project on GitHub → · Open in Google Colab → · Assignment instructions (Google Doc) →
> 
> Your repository should include:
> 
> - Your notebook and the three hyperparameters you chose.
> 
> - An untrained GIF, later checkpoints, and your best gameplay GIF.
> 
> - A training plot and a comparison of five evaluation games with the untrained baseline, using the same evaluation settings.
> 
> - A short explanation of the state, actions, reward, and one observed limitation.
> 
> Lower DQN loss does not guarantee better play. Learning speed varies; report what happened, including failed runs.
> 
> Submit your GitHub repository →
> 
> Retain the existing submission destination and core screenshot/GIF deliverables. Evaluation is needed to support any claim of improvement; the best GIF alone is selective evidence. Several games give a small comparison, not a robust research estimate. Do not promise competent play after 300 episodes or a particular laptop runtime. Source for DQN mechanism: https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf

</details>

<details><summary>S10 — vault/raw/course-slides/haas-class3.html — slide 68: A Q-Table Cannot List Every Game Screen (part: Reinforcement Learning)</summary>

> A Q-Table Cannot List Every Game Screen
> 
> Small Grid World
> 
> Pac-Man from pixels
> 
> 9 states × 4 actions = 36 values
> 
> Vast numbers of possible screen configurations
> 
> Store each value in a table
> 
> Learn a function that estimates values
> 
> Look up \(Q(s,a)\)
> 
> Input frames → neural network → one Q-value per action
> 
> Deep Q-Network (DQN) uses a neural network in place of the Q-table.
> 
> The RL objective stays the same. The way we represent action values changes.
> 
> Pac-Man is observed through images, which do not directly contain all state information. Stacking frames helps reveal movement. DQN uses replayed transitions and a target network to stabilize training. Source: https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf

</details>

## Actual Gemma answer

```text
The exploration rate used was 0.10 [S1]. The number of episodes used was 300 [S1]. The learning rate used was 0.0001 [S1].
```

## Citations

- [S1] → `vault/raw/assignments/pacman-dqn-README.md` — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > My three settings

## Automatic citation check

- Verdict: **citations_check_passed**
- “The exploration rate used was 0.10 [S1].” → ['S1'], word overlap 0.75
- “The number of episodes used was 300 [S1].” → ['S1'], word overlap 0.5
- “The learning rate used was 0.0001 [S1].” → ['S1'], word overlap 0.75

## Timing

46.77 s wall · model load 0.0 s · prompt 2805 tokens in 43.28 s · answer 45 tokens at 13.12 tokens/s

## Assessment (human, after opening the cited passages)

_Pending review._
