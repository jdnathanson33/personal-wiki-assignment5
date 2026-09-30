---
title: "Precision and Recall"
description: "Precision and Recall are metrics used to count different types of mistakes made by a model, which is important because accuracy alone can hide errors depending on the cost associated with different types of errors."
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

# Precision and Recall

Precision and Recall are metrics used to count different types of mistakes made by a model, which is important because accuracy alone can hide errors depending on the cost associated with different types of errors. These metrics help in understanding the trade-offs between false positives and false negatives.

## Key details

- True Positives (TP) occur when the model correctly predicts the positive class, such as catching spam ([Class 3 slides (Machine Learning Foundations), slide 51: True Positives and False Alarms](https://haas-ai-classes-fall-26.vercel.app/class3.html#/true-positives-and-false-alarms)).
- False Negatives (FN) occur when the model misses a positive case, such as a missed spam email ([Class 3 slides (Machine Learning Foundations), slide 51: True Positives and False Alarms](https://haas-ai-classes-fall-26.vercel.app/class3.html#/true-positives-and-false-alarms)).
- False Positives (FP) occur when the model incorrectly predicts the positive class, such as a job offer going to spam ([Class 3 slides (Machine Learning Foundations), slide 51: True Positives and False Alarms](https://haas-ai-classes-fall-26.vercel.app/class3.html#/true-positives-and-false-alarms)).
- Precision is calculated as the ratio of true positives to the total number of flagged predictions ([Class 3 slides (Machine Learning Foundations), slide 53: Precision and Recall Count Different Mistakes](https://haas-ai-classes-fall-26.vercel.app/class3.html#/precision-and-recall-count-different-mistakes)).
- Recall is calculated as the ratio of true positives to the total number of actual positive cases ([Class 3 slides (Machine Learning Foundations), slide 53: Precision and Recall Count Different Mistakes](https://haas-ai-classes-fall-26.vercel.app/class3.html#/precision-and-recall-count-different-mistakes)).
- A false positive can hide an important message for a spam filter, while a missed positive can carry a different cost for fraud detection ([Class 3 slides (Machine Learning Foundations), slide 51: True Positives and False Alarms](https://haas-ai-classes-fall-26.vercel.app/class3.html#/true-positives-and-false-alarms)).
- A decision policy must be made based on the model output, such as deciding what action to take for a high fraud score ([Class 3 slides (Machine Learning Foundations), slide 55: A Prediction Still Needs a Decision Policy](https://haas-ai-classes-fall-26.vercel.app/class3.html#/a-prediction-still-needs-a-decision-policy)).

## Related notes

- [[Class 3 - Machine Learning]] — taught here
- [[Evaluation Design]] — choosing what to measure
- [[Overfitting and Generalization]] — evaluate on held-out data

## Sources

- [[raw/course-slides/haas-class3.html|Class 3 slides (Machine Learning Foundations)]] — True Positives and False Alarms, Accuracy Can Hide the Error You Care About, Precision and Recall Count Different Mistakes, Try It: Choose a Renewal Threshold, A Prediction Still Needs a Decision Policy · [public page](https://haas-ai-classes-fall-26.vercel.app/class3.html)
