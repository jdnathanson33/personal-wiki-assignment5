---
title: "Fine-Tuning and LoRA"
description: "Fine-tuning and LoRA are methods used to adapt pretrained models, with fine-tuning permanently reshaping the model's distribution by changing its weights, while LoRA involves training a small add-on matrix (adapter) to nudge the model's behavior, offering a cheaper alternative to full fine-tuning."
type: concept
sources:
  - "[[raw/course-slides/haas-class5.html]]"
source_ids:
  - class5-slides
source_sha256:
  - class5-slides@a53bb050753d
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Fine-Tuning and LoRA

Fine-tuning and LoRA are methods used to adapt pretrained models, with fine-tuning permanently reshaping the model's distribution by changing its weights, while LoRA involves training a small add-on matrix (adapter) to nudge the model's behavior, offering a cheaper alternative to full fine-tuning. This distinction is relevant when deciding between prompting, LoRA, and fine-tuning based on cost and desired changes.

## Key details

- Fine-tuning shifts which tokens the model considers likely because the weights change, leading to completely different predictions with the same prompt ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 15: Fine-Tuning Reshapes the Distribution](https://haas-ai-classes-fall-26.vercel.app/class5.html#/fine-tuning-reshapes-the-distribution)).
- Fine-tuning is expensive and permanent because it changes the model’s weights ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 15: Fine-Tuning Reshapes the Distribution](https://haas-ai-classes-fall-26.vercel.app/class5.html#/fine-tuning-reshapes-the-distribution)).
- Prompting is cheap and temporary because it steers the same frozen model ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 15: Fine-Tuning Reshapes the Distribution](https://haas-ai-classes-fall-26.vercel.app/class5.html#/fine-tuning-reshapes-the-distribution)).
- RLHF involves a three-stage post-training process: Pretraining (unsupervised), SFT (Supervised Fine-Tuning), and RLHF (Reinforcement Learning from Human Feedback) ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 16: RLHF — How Models Learn to Be Helpful](https://haas-ai-classes-fall-26.vercel.app/class5.html#/rlhf-how-models-learn-to-be-helpful)).
- Prompting changes the instructions and examples supplied for a request, while fine-tuning changes the model ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 18: Three Levers, Three Jobs](https://haas-ai-classes-fall-26.vercel.app/class5.html#/the-three-levers-visually)).
- LoRA (Low-Rank Adaptation) trains a tiny add-on matrix (an “adapter”) instead of updating billions of weights, making it approximately 100 times cheaper than fine-tuning ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 19: Prompting vs LoRA vs Fine-Tuning — The Decision Table](https://haas-ai-classes-fall-26.vercel.app/class5.html#/prompting-vs-lora-vs-fine-tuning-the-decision-table)).
- Prompting is reversible and costs ~$0, whereas LoRA costs $100s–$10Ks and allows swapping adapters ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 19: Prompting vs LoRA vs Fine-Tuning — The Decision Table](https://haas-ai-classes-fall-26.vercel.app/class5.html#/prompting-vs-lora-vs-fine-tuning-the-decision-table)).
- Full fine-tuning costs $10Ks–$1Ms and is irreversible, whereas prompting is renting and LoRA is a lease with an exit clause ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 19: Prompting vs LoRA vs Fine-Tuning — The Decision Table](https://haas-ai-classes-fall-26.vercel.app/class5.html#/prompting-vs-lora-vs-fine-tuning-the-decision-table)).

## Related notes

- [[Class 5 - LLMs Prompting and Retrieval]] — taught here
- [[Prompt Engineering]] — the cheaper lever
- [[Retrieval Augmented Generation]] — RAG adds knowledge without retraining

## Sources

- [[raw/course-slides/haas-class5.html|Class 5 slides (LLM Behavior, Prompting & Retrieval)]] — Fine-Tuning Reshapes the Distribution, RLHF — How Models Learn to Be Helpful, …But It’s Super Expensive, Three Levers, Three Jobs, Prompting vs LoRA vs Fine-Tuning — The Decision Table · [public page](https://haas-ai-classes-fall-26.vercel.app/class5.html)
