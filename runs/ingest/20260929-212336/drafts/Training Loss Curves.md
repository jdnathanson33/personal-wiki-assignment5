---
title: "Training Loss Curves"
description: "Training loss curves in Pac-Man DQN showed that lower loss does not necessarily equate to better results, as the loss climbed in some instances while performance fluctuated."
type: concept
sources:
  - "[[raw/assignments/pacman-dqn-README.md]]"
  - "[[raw/assignments/custom-llm-README.md]]"
source_ids:
  - pacman-dqn-readme
  - custom-llm-readme
source_sha256:
  - pacman-dqn-readme@9a9a849ffbe3
  - custom-llm-readme@532515c6591e
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: false
---

# Training Loss Curves

Training loss curves in Pac-Man DQN showed that lower loss does not necessarily equate to better results, as the loss climbed in some instances while performance fluctuated. Similarly, for nanoGPT, loss flattening after an initial drop suggests a floor due to random token filling, and losses from different experiments cannot be directly compared.

## Key details

- In Pac-Man DQN, the training loss climbed from about 0.02 to about 0.10–0.16 and ended near 0.09, indicating that lower loss is not the same as better play because value targets get larger and change more as the agent reaches more rewarding situations ([[raw/assignments/pacman-dqn-README.md#What I expected vs. what happened|§ What I expected vs. what happened]]).
- For Pac-Man DQN, the periodic single-game demo showed the agent's quality swung from one checkpoint to the next, with the episode-125 checkpoint looking stronger on one game than the final model ([[raw/assignments/pacman-dqn-README.md#What I expected vs. what happened|§ What I expected vs. what happened]]).
- In Pac-Man DQN evaluation, the mean score after 300 episodes was 604.0, compared to 492.0 before training ([[raw/assignments/pacman-dqn-README.md|§ Evaluation: all five games (comparison.json)]]).
- For nanoGPT, the training-panel loss fell by about 86% by the halfway point and then flattened, which is expected because classroom sentences have slots filled at random ([[raw/assignments/custom-llm-README.md#4. Loss evidence|§ 4. Loss evidence]]).
- Validation loss in nanoGPT stayed close to training loss, which rules out heavy memorization of individual sentences, but it does not show generalization beyond the templates used ([[raw/assignments/custom-llm-README.md#4. Loss evidence|§ 4. Loss evidence]]).
- Losses from the Starter and Expanded nanoGPT experiments cannot be compared because they use different corpora and vocabularies ([[raw/assignments/custom-llm-README.md#4. Loss evidence|§ 4. Loss evidence]]).

## Related notes

- [[Pac-Man DQN Agent]] — loss rose as the agent improved a little
- [[Tiny nanoGPT Model]] — loss fell 86% then flattened
- [[Model Training and Gradient Descent]] — what loss measures
- [[Overfitting and Generalization]] — train vs validation gap

## Sources

- [[raw/assignments/pacman-dqn-README.md|Pac-Man DQN README]] — What I expected vs. what happened, Evaluation: all five games (comparison.json), Training dashboard, Gameplay (first 20 s of game time, 4× speed)
- [[raw/assignments/custom-llm-README.md|nanoGPT README]] — 4. Loss evidence
