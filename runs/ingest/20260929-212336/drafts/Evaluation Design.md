---
title: "Evaluation Design"
description: "Evaluation design in this work involves testing models using fixed seeds and evaluation suites, analyzing results from small noisy samples, and considering changes based on observed limitations."
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

# Evaluation Design

Evaluation design in this work involves testing models using fixed seeds and evaluation suites, analyzing results from small noisy samples, and considering changes based on observed limitations. This process is applied across different domains, such as reinforcement learning and language modeling, to assess performance.

## Key details

- For Pac-Man DQN, evaluation involved comparing performance across five games with different seeds, showing a mean improvement from 492.0 to 604.0 after 300 episodes ([[raw/assignments/pacman-dqn-README.md|§ Evaluation: all five games (comparison.json)]]).
- Evaluation in the Pac-Man DQN context was limited because the samples were small and noisy, meaning five games could not reliably distinguish real learning from luck ([[raw/assignments/pacman-dqn-README.md#One limitation|§ One limitation]]).
- To test the impact of training budget, the number of episodes was changed from 300 to 1,000 while keeping exploration at 0.10 and the learning rate at 0.0001, noting that 43k updates was small for Atari ([[raw/assignments/pacman-dqn-README.md#Next experiment|§ Next experiment]]).
- For nanoGPT, public development tests were used to choose extension categories, and the results showed that trained models achieved 29 correct out of 29 scorable cases ([[raw/assignments/custom-llm-README.md#Four-row comparison (48 fixed cases)|§ Four-row comparison (48 fixed cases)]]).
- A limitation observed in nanoGPT was that the model's knowledge was tied to template slots, as new frames interfered with old ones, causing free text to blend contrast frames into sentences ([[raw/assignments/custom-llm-README.md#10. One limitation and my next experiment|§ 10. One limitation and my next experiment]]).
- A proposed next experiment for nanoGPT involves adding a held-out set of new spatial and opposites prompts and using 3 seeds per corpus to test if gains are a real pattern or due to a lucky run ([[raw/assignments/custom-llm-README.md#10. One limitation and my next experiment|§ 10. One limitation and my next experiment]]).

## Related notes

- [[Pac-Man DQN Agent]] — five-game evaluation
- [[Tiny nanoGPT Model]] — 48-case eval suite
- [[Precision and Recall]] — choosing the metric
- [[Overfitting and Generalization]] — keep test data separate

## Sources

- [[raw/assignments/pacman-dqn-README.md|Pac-Man DQN README]] — Evaluation: all five games (comparison.json), One limitation, Next experiment
- [[raw/assignments/custom-llm-README.md|nanoGPT README]] — Four-row comparison (48 fixed cases), 10. One limitation and my next experiment
