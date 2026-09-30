---
title: "Training Loss Curves"
description: "Training loss curves in Pac-Man DQN showed that lower loss does not equate to better results, as loss can increase while performance fluctuates."
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
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Training Loss Curves

Training loss curves in Pac-Man DQN showed that lower loss does not equate to better results, as loss can increase while performance fluctuates. For nanoGPT, loss fell quickly and then flattened at a floor above zero, because the template slots are filled at random; losses from the two experiments cannot be compared.

## Key details

- In Pac-Man DQN, the training loss climbed from about 0.02 to about 0.10–0.16 and ended near 0.09, demonstrating that lower loss is not the same as better play ([[raw/assignments/pacman-dqn-README.md#What I expected vs. what happened|§ What I expected vs. what happened]]).
- For Pac-Man DQN, the periodic single-game demo showed the agent's quality swung from one checkpoint to the next, with the episode-125 checkpoint looking stronger on one game than the final model ([[raw/assignments/pacman-dqn-README.md#What I expected vs. what happened|§ What I expected vs. what happened]]).
- In nanoGPT, the training-panel loss fell by about 86% by the halfway point and then flattened, which is expected because classroom sentences have slots filled at random ([[raw/assignments/custom-llm-README.md#4. Loss evidence|§ 4. Loss evidence]]).
- For nanoGPT, validation loss stayed close to training loss, suggesting that heavy memorization of individual sentences is not occurring ([[raw/assignments/custom-llm-README.md#4. Loss evidence|§ 4. Loss evidence]]).
- The losses from the two nanoGPT experiments cannot be compared because they use different corpora and vocabularies ([[raw/assignments/custom-llm-README.md#4. Loss evidence|§ 4. Loss evidence]]).
- The 3× learning rate in nanoGPT gave no visible instability at the three measurement points ([[raw/assignments/custom-llm-README.md#4. Loss evidence|§ 4. Loss evidence]]).

## Related notes

- [[Pac-Man DQN Agent]] — loss rose as the agent improved a little
- [[Tiny nanoGPT Model]] — loss fell 86% then flattened
- [[Model Training and Gradient Descent]] — what loss measures
- [[Overfitting and Generalization]] — train vs validation gap

## Sources

- [[raw/assignments/pacman-dqn-README.md|Pac-Man DQN README]] — What I expected vs. what happened, Evaluation: all five games (comparison.json), Training dashboard, Gameplay (first 20 s of game time, 4× speed)
- [[raw/assignments/custom-llm-README.md|nanoGPT README]] — 4. Loss evidence
