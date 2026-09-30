> **Rehearsal run with internet ON** (model still local). Not the graded offline evidence; kept to show what changed.

# Ask-mode evidence card: T1

**Question:** What was the mean evaluation score of my Pac-Man DQN agent before and after training?

| Field | Value |
|---|---|
| Mode | ask (standalone; no chat history, no persona) |
| Execution | local |
| Model | `gemma4:e2b-it-qat` (4.6B, Q4_0, digest `07ea59a47401`) |
| Embedding model | `embeddinggemma` |
| Runtime | ollama 0.35.0 |
| Internet at run time | **ONLINE** |
| Timestamp | 2026-09-29T21:00:21 |

## Expected (written before running)

- Type: direct, one source
- Expected behavior: Answer 492.0 before and 604.0 after (+112.0), cited to the Pac-Man README.
- Expected source(s): `vault/raw/assignments/pacman-dqn-README.md`
- Expected passage: “492.0 → 604.0”

## Retrieved passages (hybrid (bm25 + embeddinggemma, RRF), scope `raw`, top 8)

| Label | Source path | Location | BM25 | Cosine | Matched terms |
|---|---|---|---|---|---|
| S1 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) | 32.864 | 0.7388 | after, agent, dqn, evaluation, man, mean, pac, score |
| S2 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened > Evaluation: all five games (comparison.json) | 25.337 | 0.6802 | after, before, dqn, evaluation, man, mean, pac |
| S3 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > Next experiment | 22.734 | 0.6658 | before, dqn, evaluation, man, mean, pac, train |
| S4 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > My three settings | 20.527 | 0.6543 | agent, dqn, evaluation, man, pac, train |
| S5 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened | 17.665 | 0.7121 | agent, dqn, man, mean, pac, train |
| S6 | `vault/raw/course-slides/haas-class3.html` | slide 71: Show What the Agent Actually Learned (part: End Project: Pac-Man DQN) | 22.204 | 0.5701 | after, agent, dqn, evaluation, man, pac, train |
| S7 | `vault/raw/course-slides/haas-class3.html` | slide 70: Train an Agent to Play Ms. Pac-Man (part: End Project: Pac-Man DQN) | 23.889 | 0.557 | after, agent, before, dqn, man, pac, train |
| S8 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened | 18.071 | 0.656 | agent, before, dqn, man, pac, train |

<details><summary>S1 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI)</summary>

> I trained the course's Deep Q-Network (DQN) on Atari Ms. Pac-Man. I changed only three settings: exploration, episodes, and learning rate. The untrained and trained agents were scored on the same five evaluation games.
> 
> **Result:** the mean evaluation score went from **492.0 → 604.0 (+112.0)**. Most of that gain comes from one strong game (1,420); three of the five games scored lower after training. So this run shows limited learning, not a clear improvement.

</details>

<details><summary>S2 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened > Evaluation: all five games (comparison.json)</summary>

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

<details><summary>S3 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > Next experiment</summary>

> **Change only the number of episodes, from 300 to 1,000**, and keep exploration at 0.10 and the learning rate at 0.0001. The 25-game average was still swinging at the end of this run (about 940 at episode 272, 670 at episode 300), and 43k updates is small for Atari. A DQN typically needs far more experience before it learns to avoid ghosts reliably. Keeping the other two settings fixed means any change in the five evaluation scores can be attributed to the training budget.

</details>

<details><summary>S4 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > My three settings</summary>

> | Setting | Value | Why |
> |---|---|---|
> | Exploration | **0.10** | This is close to the final exploration level in standard DQN. The agent still tries new routes, but training play (10% random) stays close to evaluation play (5% random). The default of 0.20 wastes many lives on random moves. |
> | Episodes | **300** | A real training budget that fit in about 33 minutes on CPU. It also produces 12 intermediate GIFs and checkpoints. |
> | Learning rate | **0.0001** | The standard, stable Adam learning rate for DQN (and the notebook's reference value). I kept it so the run would not diverge. |
> 
> All other settings were left at the notebook's fixed values. Evaluation was unchanged: seeds 101/202/303/404/505, 5% exploration, and a limit of 3,000 decisions per game. See [`config.json`](results/config.json).

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

<details><summary>S6 — vault/raw/course-slides/haas-class3.html — slide 71: Show What the Agent Actually Learned (part: End Project: Pac-Man DQN)</summary>

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

<details><summary>S7 — vault/raw/course-slides/haas-class3.html — slide 70: Train an Agent to Play Ms. Pac-Man (part: End Project: Pac-Man DQN)</summary>

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

<details><summary>S8 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened</summary>

> …agent reaches more rewarding situations, its value targets get larger and change more. It shows that lower loss is not the same thing as better play.
> 
> - **The periodic single-game demo (seed 101) did not improve steadily.** Scores by episode: 25 → 920, 50 → 860, 75 → 840, 100 → 700, 125 → 1,250, 150 → 530, 175 → 460, 200 → 170, 225 → 610, 250 → 270, 275 → 530, 300 → 310. The agent's quality swung from one checkpoint to the next. The episode-125 checkpoint looked stronger on this one game than the final model.
> 
> - **Gameplay:** in the first 20 seconds, the untrained and best trained GIFs look similar. Both collect pellets along corridors and lose a life to a ghost fairly early. The trained agent did not visibly avoid ghosts. Trained games were also shorter on average: 535 decisions vs. 589 before.

</details>

## Actual Gemma answer

```text
The mean evaluation score went from 492.0 before training to 604.0 after training [S1][S2].
```

## Citations

- [S1] → `vault/raw/assignments/pacman-dqn-README.md` — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI)
- [S2] → `vault/raw/assignments/pacman-dqn-README.md` — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) > What I expected vs. what happened > Evaluation: all five games (comparison.json)

## Automatic citation check

- Verdict: **citations_check_passed**
- “The mean evaluation score went from 492.0 before training to 604.0 after training [S1][S2].” → ['S1', 'S2'], word overlap 1.0

## Timing

69.36 s wall · model load 15.31 s · prompt 2279 tokens in 51.23 s · answer 31 tokens at 11.29 tokens/s

## Assessment (human, after opening the cited passages)

_Pending review._
