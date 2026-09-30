---
title: "Deep Q-Networks"
description: "Deep Q-Networks (DQN) use a neural network to estimate action values, replacing the traditional Q-table, allowing the agent to handle vast state spaces by processing input frames."
type: concept
sources:
  - "[[raw/course-slides/haas-class3.html]]"
  - "[[raw/assignments/pacman-dqn-README.md]]"
source_ids:
  - class3-slides
  - pacman-dqn-readme
source_sha256:
  - class3-slides@0468e12c46ef
  - pacman-dqn-readme@9a9a849ffbe3
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Deep Q-Networks

Deep Q-Networks (DQN) use a neural network to estimate action values, replacing the traditional Q-table, allowing the agent to handle vast state spaces by processing input frames. This method utilizes components like frame stacking, experience replay, and a target network to stabilize training and improve learning efficiency.

## Key details

- DQN uses a neural network in place of the Q-table to estimate $Q(s,a)$ based on input frames ([Class 3 slides (Machine Learning Foundations), slide 68: A Q-Table Cannot List Every Game Screen](https://haas-ai-classes-fall-26.vercel.app/class3.html#/a-q-table-cannot-list-every-game-screen)).
- Pac-Man DQN observes the last four game screens, shrunk to 84 × 84 grayscale, to determine movement ([[raw/assignments/pacman-dqn-README.md#How the agent works, in plain language|§ How the agent works, in plain language]]).
- The agent selects one of 9 joystick moves (no-op, up, right, left, down, and four diagonals), holding each choice for 4 game frames ([[raw/assignments/pacman-dqn-README.md#How the agent works, in plain language|§ How the agent works, in plain language]]).
- Rewards are clipped to be between −1 and +1 during training, meaning the agent learns "points or no points" ([[raw/assignments/pacman-dqn-README.md#How the agent works, in plain language|§ How the agent works, in plain language]]).
- Experience replay samples past transitions to reduce correlation and reuse experience ([Class 3 slides (Machine Learning Foundations), slide 82: Why DQN Uses Replay and a Target Network](https://haas-ai-classes-fall-26.vercel.app/class3.html#/why-dqn-uses-replay-and-a-target-network)).
- A target network provides a slower-changing target for value updates ([Class 3 slides (Machine Learning Foundations), slide 82: Why DQN Uses Replay and a Target Network](https://haas-ai-classes-fall-26.vercel.app/class3.html#/why-dqn-uses-replay-and-a-target-network)).
- Evaluation is small and noisy, and the agent can be unstable, with performance varying significantly across games ([[raw/assignments/pacman-dqn-README.md#One limitation|§ One limitation]]).

## Related notes

- [[Reinforcement Learning]] — the broader setting
- [[Pac-Man DQN Agent]] — my DQN run
- [[Neural Networks]] — the Q-function is a neural network

## Sources

- [[raw/course-slides/haas-class3.html|Class 3 slides (Machine Learning Foundations)]] — A Q-Table Cannot List Every Game Screen, Why DQN Uses Replay and a Target Network · [public page](https://haas-ai-classes-fall-26.vercel.app/class3.html)
- [[raw/assignments/pacman-dqn-README.md|Pac-Man DQN README]] — How the agent works, in plain language, One limitation
