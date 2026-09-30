---
title: "Overfitting and Generalization"
description: "Overfitting and generalization relate to how a model fits training data, where overfitting occurs when a model fits training details that do not generalize, and bias and variance describe the systematic error and model flexibility, respectively."
type: concept
sources:
  - "[[raw/course-slides/haas-class3.html]]"
  - "[[raw/assignments/custom-llm-README.md]]"
source_ids:
  - class3-slides
  - custom-llm-readme
source_sha256:
  - class3-slides@0468e12c46ef
  - custom-llm-readme@532515c6591e
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Overfitting and Generalization

Overfitting and generalization relate to how a model fits training data, where overfitting occurs when a model fits training details that do not generalize, and bias and variance describe the systematic error and model flexibility, respectively. This concept is important when using test sets, validation data, and baselines to guide model development and ensure future predictions are reliable.

## Key details

- Overfitting occurs when a model fits training details that do not carry over ([Class 3 slides (Machine Learning Foundations), slide 42: Overfitting Fits Noise Along With Signal](https://haas-ai-classes-fall-26.vercel.app/class3.html#/overfitting-fits-noise-along-with-signal)).
- Underfitting is when the model is too limited to capture the pattern ([Class 3 slides (Machine Learning Foundations), slide 42: Overfitting Fits Noise Along With Signal](https://haas-ai-classes-fall-26.vercel.app/class3.html#/overfitting-fits-noise-along-with-signal)).
- Bias is defined as the systematic error from simplifying assumptions, while variance is how much the fitted model changes with the training sample ([Class 3 slides (Machine Learning Foundations), slide 43: Bias and Variance](https://haas-ai-classes-fall-26.vercel.app/class3.html#/bias-and-variance)).
- Validation data can be used to choose settings and can guide development, but the final test set should remain untouched until choices are fixed ([Class 3 slides (Machine Learning Foundations), slide 40: Keep a Test Set Outside Development](https://haas-ai-classes-fall-26.vercel.app/class3.html#/keep-a-test-set-outside-development); [Class 3 slides (Machine Learning Foundations), slide 41: Separate Fitting, Choosing, and Testing](https://haas-ai-classes-fall-26.vercel.app/class3.html#/separate-fitting-choosing-and-testing)).
- For future predictions, training should be done on older cases, validation on later ones, and testing on the newest held-out period ([Class 3 slides (Machine Learning Foundations), slide 41: Separate Fitting, Choosing, and Testing](https://haas-ai-classes-fall-26.vercel.app/class3.html#/separate-fitting-choosing-and-testing)).
- The loss from the two experiments (Starter and Expanded) cannot be compared because they use different corpora and vocabularies ([[raw/assignments/custom-llm-README.md#4. Loss evidence|§ 4. Loss evidence]]).
- Validation loss staying close to training loss rules out heavy memorization of individual sentences, but it does not show generalization beyond the same templates ([[raw/assignments/custom-llm-README.md#4. Loss evidence|§ 4. Loss evidence]]).

## Related notes

- [[Class 3 - Machine Learning]] — taught here
- [[Evaluation Design]] — how I evaluated my own models
- [[Training Loss Curves]] — train vs validation loss
- [[Tiny nanoGPT Model]] — validation used the same templates

## Sources

- [[raw/course-slides/haas-class3.html|Class 3 slides (Machine Learning Foundations)]] — Keep a Test Set Outside Development, Separate Fitting, Choosing, and Testing, Overfitting Fits Noise Along With Signal, Bias and Variance, Compare Against a Simple Baseline · [public page](https://haas-ai-classes-fall-26.vercel.app/class3.html)
- [[raw/assignments/custom-llm-README.md|nanoGPT README]] — 4. Loss evidence
