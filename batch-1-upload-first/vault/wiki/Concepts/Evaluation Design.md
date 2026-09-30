---
title: "Evaluation Design"
description: "Evaluation design involves using fixed seeds and evaluation suites, testing with small noisy samples, and utilizing public development tests to assess model performance."
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

# Evaluation Design

Evaluation design involves using fixed seeds and evaluation suites, testing with small noisy samples, and utilizing public development tests to assess model performance. In both projects the evaluation was small or public, so the results show limited evidence, and each README proposes a better-controlled next experiment.

## Key details

- For Pac-Man DQN, evaluation involved comparing results across five games with different seeds, showing a mean improvement from 492.0 to 604.0 after 300 episodes ([[raw/assignments/pacman-dqn-README.md|§ Evaluation: all five games (comparison.json)]]).
- Evaluation is limited because the samples are small and noisy, and the agent is unstable, meaning five games cannot reliably distinguish real learning from luck ([[raw/assignments/pacman-dqn-README.md#One limitation|§ One limitation]]).
- The proposed next experiment (not yet run) changes only the number of episodes, from 300 to 1,000, and keeps exploration at 0.10 and the learning rate at 0.0001, so any change in the five evaluation scores can be attributed to the training budget ([[raw/assignments/pacman-dqn-README.md#Next experiment|§ Next experiment]]).
- Public development tests were used for nanoGPT, and these tests were read to select extension categories, meaning they do not represent an unseen final benchmark ([[raw/assignments/custom-llm-README.md#Four-row comparison (48 fixed cases)|§ Four-row comparison (48 fixed cases)]]).
- For nanoGPT, the model's knowledge is tied to template slots, and new frames interfere with old ones, as seen in chat replies blending contrast frames into sentences ([[raw/assignments/custom-llm-README.md#10. One limitation and my next experiment|§ 10. One limitation and my next experiment]]).
- A next experiment for nanoGPT involves adding a held-out set of new spatial and opposites prompts and running with 3 seeds per corpus to check if gains are a real pattern ([[raw/assignments/custom-llm-README.md#10. One limitation and my next experiment|§ 10. One limitation and my next experiment]]).

## Related notes

- [[Pac-Man DQN Agent]] — five-game evaluation
- [[Tiny nanoGPT Model]] — 48-case eval suite
- [[Precision and Recall]] — choosing the metric
- [[Overfitting and Generalization]] — keep test data separate

## Sources

- [[raw/assignments/pacman-dqn-README.md|Pac-Man DQN README]] — Evaluation: all five games (comparison.json), One limitation, Next experiment
- [[raw/assignments/custom-llm-README.md|nanoGPT README]] — Four-row comparison (48 fixed cases), 10. One limitation and my next experiment
