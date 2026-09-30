---
title: "Tiny nanoGPT Model"
description: "The Tiny nanoGPT Model refers to two word-level models trained from scratch using the nanoGPT framework, with identical settings; only the training corpus changed."
type: project
sources:
  - "[[raw/assignments/custom-llm-README.md]]"
source_ids:
  - custom-llm-readme
source_sha256:
  - custom-llm-readme@532515c6591e
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Tiny nanoGPT Model

The Tiny nanoGPT Model refers to two word-level models trained from scratch using the nanoGPT framework, with identical settings; only the training corpus changed. Both were scored on the same fixed 48-case language eval suite, and the README stresses that the results should not be read as the model understanding language.

## Key details

- Both tiny word-level nanoGPT models were trained from scratch with 2 blocks, 4 heads, 64-number embeddings, and a 48-token context ([[raw/assignments/custom-llm-README.md#Class 4: Building a Custom LLM (nanoGPT, word tokens)|§ Class 4: Building a Custom LLM (nanoGPT, word tokens)]]).
- The two models used the same settings, with only the corpus differing between the Starter (classroom corpus only) and Expanded (classroom corpus plus teaching files for opposites and spatial relations) versions ([[raw/assignments/custom-llm-README.md#Class 4: Building a Custom LLM (nanoGPT, word tokens)|§ Class 4: Building a Custom LLM (nanoGPT, word tokens)]]).
- The training steps for both models were set to 3,000 ([[raw/assignments/custom-llm-README.md#1. My choices and prediction|§ 1. My choices and prediction]]).
- The Starter model achieved 19 correct out of 48 cases (39.6% correct) after training, while the Expanded model achieved 29 correct out of 48 cases (60.4% correct) ([[raw/assignments/custom-llm-README.md#Four-row comparison (48 fixed cases)|§ Four-row comparison (48 fixed cases)]]).
- The Expanded model had a vocabulary of 358 (355 types, under the 509 cap), compared to 136 for the Starter model ([[raw/assignments/custom-llm-README.md#2. The runs|§ 2. The runs]]).
- The train/validation split was 4,132 / 460 passages for the starter run and 8,790 / 977 for the expanded run (90/10 by passage, seed 42) ([[raw/assignments/custom-llm-README.md#2. The runs|§ 2. The runs]]).
- The chat interface allows interaction with the expanded model, which is noted as a tiny model that continues short sentences and is not a general assistant ([[raw/assignments/custom-llm-README.md#Class 4: Building a Custom LLM (nanoGPT, word tokens)|§ Class 4: Building a Custom LLM (nanoGPT, word tokens)]]).

## Related notes

- [[Fundamentals of Agentic AI]] — course map
- [[Tokens and Embeddings]] — traced token ids and embedding vectors
- [[Transformer Attention]] — the model's 2 transformer blocks
- [[Sampling Temperature]] — temperature comparison in the notebook
- [[Training Loss Curves]] — loss evidence for both runs
- [[Evaluation Design]] — 48 fixed eval cases, public development tests
- [[Class 4 - Deep Learning and Transformers]] — the class this assignment came from

## Sources

- [[raw/assignments/custom-llm-README.md|nanoGPT README]] — Class 4: Building a Custom LLM (nanoGPT, word tokens), Four-row comparison (48 fixed cases), 1. My choices and prediction, 2. The runs, 8. Chat interface, 10. One limitation and my next experiment
