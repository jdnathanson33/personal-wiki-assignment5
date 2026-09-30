---
title: "Pac-Man DQN Agent"
description: "The Pac-Man DQN Agent was trained on Atari Ms. Pac-Man using three specific settings: exploration at 0.10, 300 episodes, and a learning rate of 0.0001."
type: project
sources:
  - "[[raw/assignments/pacman-dqn-README.md]]"
source_ids:
  - pacman-dqn-readme
source_sha256:
  - pacman-dqn-readme@9a9a849ffbe3
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Pac-Man DQN Agent

The Pac-Man DQN Agent was trained on Atari Ms. Pac-Man using three specific settings: exploration at 0.10, 300 episodes, and a learning rate of 0.0001. This run showed a mean evaluation score increase from 492.0 to 604.0, but the learning was described as limited and noisy.

## Key details

- The training budget consisted of 300 episodes, which took approximately 1,996 s (about 33 min, including periodic demos) and resulted in 173,434 decisions ([[raw/assignments/pacman-dqn-README.md|§ Actual training budget (training_summary.json)]]).
- The exploration setting was set to 0.10, which is close to the final exploration level in standard DQN, allowing the agent to try new routes while maintaining 10% random training play ([[raw/assignments/pacman-dqn-README.md#My three settings|§ My three settings]]).
- The learning rate was set to 0.0001, which is the standard, stable Adam learning rate for DQN ([[raw/assignments/pacman-dqn-README.md#My three settings|§ My three settings]]).
- The mean evaluation score went from 492.0 (untrained) to 604.0 (trained) across five evaluation games ([[raw/assignments/pacman-dqn-README.md#Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI)|§ Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI)]]; [[raw/assignments/pacman-dqn-README.md|§ Evaluation: all five games (comparison.json)]]).
- A limitation noted is that evaluation is small and noisy, as the +112.0 improvement came almost entirely from one game (seed 303), and three games scored lower after training ([[raw/assignments/pacman-dqn-README.md#One limitation|§ One limitation]]).
- The next experiment planned is to change only the number of episodes from 300 to 1,000, keeping exploration at 0.10 and the learning rate at 0.0001 ([[raw/assignments/pacman-dqn-README.md#Next experiment|§ Next experiment]]).

## Related notes

- [[Fundamentals of Agentic AI]] — course map
- [[Deep Q-Networks]] — the algorithm the agent uses
- [[Reinforcement Learning]] — the learning setting
- [[Training Loss Curves]] — loss went up while play barely improved
- [[Evaluation Design]] — five games were too few to separate learning from luck
- [[Class 3 - Machine Learning]] — the class this assignment came from

## Sources

- [[raw/assignments/pacman-dqn-README.md|Pac-Man DQN README]] — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI), My three settings, What I expected vs. what happened, Evaluation: all five games (comparison.json), Training dashboard, Gameplay (first 20 s of game time, 4× speed), Actual training budget (training_summary.json), One limitation
