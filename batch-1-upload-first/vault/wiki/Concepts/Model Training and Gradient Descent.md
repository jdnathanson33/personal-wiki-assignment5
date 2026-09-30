---
title: "Model Training and Gradient Descent"
description: "Model training involves adjusting adjustable parameters of a model to fit historical examples by minimizing a loss function, often using gradient descent to iteratively improve predictions."
type: concept
sources:
  - "[[raw/course-slides/haas-class3.html]]"
source_ids:
  - class3-slides
source_sha256:
  - class3-slides@0468e12c46ef
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Model Training and Gradient Descent

Model training involves adjusting adjustable parameters of a model to fit historical examples by minimizing a loss function, often using gradient descent to iteratively improve predictions. This process starts with a poor guess and repeats updates until the loss converges, which is how a model learns from data.

## Key details

- A model has adjustable parameters, such as slope \(w\) and intercept \(b\), which are chosen during training to fit historical examples ([Class 3 slides (Machine Learning Foundations), slide 22: A Model Has Adjustable Parameters](https://haas-ai-classes-fall-26.vercel.app/class3.html#/a-model-has-adjustable-parameters)).
- Training involves choosing parameter values that fit historical examples ([Class 3 slides (Machine Learning Foundations), slide 22: A Model Has Adjustable Parameters](https://haas-ai-classes-fall-26.vercel.app/class3.html#/a-model-has-adjustable-parameters)).
- Loss measures prediction error, and training tries to reduce this average; for toy revenue data, the mean squared error is approximately 12.7 ([Class 3 slides (Machine Learning Foundations), slide 23: Loss Measures Prediction Error](https://haas-ai-classes-fall-26.vercel.app/class3.html#/loss-measures-prediction-error)).
- Training starts with predictions that miss most observations ([Class 3 slides (Machine Learning Foundations), slide 24: Training Starts With a Poor Guess](https://haas-ai-classes-fall-26.vercel.app/class3.html#/training-starts-with-a-poor-guess)).
- Adjusting the line involves changing the slope and intercept to reduce loss, which can improve the fit but may still result in missed observations ([Class 3 slides (Machine Learning Foundations), slide 25: Adjusting the Line](https://haas-ai-classes-fall-26.vercel.app/class3.html#/adjusting-the-line)).
- Repeated updates improve the fit as errors get smaller, with the loss dropping from 312 to 58 ([Class 3 slides (Machine Learning Foundations), slide 26: Repeated Updates Improve the Fit](https://haas-ai-classes-fall-26.vercel.app/class3.html#/repeated-updates-improve-the-fit)).
- Gradient descent updates parameters by predicting, measuring loss, computing the gradient, taking a small downhill step, and repeating, where the learning rate controls the step size ([Class 3 slides (Machine Learning Foundations), slide 28: Gradient Descent Updates the Parameters](https://haas-ai-classes-fall-26.vercel.app/class3.html#/gradient-descent-updates-the-parameters)).
- Training and inference use different information: training uses historical features and known answers to update parameters, while inference uses features for a new case and the fitted model's parameters ([Class 3 slides (Machine Learning Foundations), slide 33: Training and Inference Use Different Information](https://haas-ai-classes-fall-26.vercel.app/class3.html#/training-and-inference-use-different-information)).

## Related notes

- [[Class 3 - Machine Learning]] — taught here
- [[Neural Networks]] — the same loop trains deep networks
- [[Training Loss Curves]] — what loss looked like in my runs
- [[Overfitting and Generalization]] — fitting is not the same as generalizing

## Sources

- [[raw/course-slides/haas-class3.html|Class 3 slides (Machine Learning Foundations)]] — A Model Has Adjustable Parameters, Loss Measures Prediction Error, Training Starts With a Poor Guess, Adjusting the Line, Repeated Updates Improve the Fit, The Fit Converges, Gradient Descent Updates the Parameters, Try It: Fit the Line · [public page](https://haas-ai-classes-fall-26.vercel.app/class3.html)
