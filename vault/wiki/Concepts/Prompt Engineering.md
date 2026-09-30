---
title: "Prompt Engineering"
description: "Prompt Engineering involves guiding an LLM's output by adding detail, examples, constraints, and formatting requirements to steer the probability of a desired answer."
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

# Prompt Engineering

Prompt Engineering involves guiding an LLM's output by adding detail, examples, constraints, and formatting requirements to steer the probability of a desired answer. It is crucial to understand that the prompt itself functions as context, and specific prompting techniques help reduce ambiguity and improve model performance.

## Key details

- Prompting is described as guidance, where adding detail, examples, constraints, and formatting requirements shrinks the space of acceptable continuations, making the "right" answer more likely ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 21: Prompting Is Probability Steering](https://haas-ai-classes-fall-26.vercel.app/class5.html#/prompting-is-probability-steering)).
- Specific prompts work because they reduce ambiguity, leading to lower entropy in the next-token distribution and making the model less likely to wander into the wrong answer shape ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 21: Prompting Is Probability Steering](https://haas-ai-classes-fall-26.vercel.app/class5.html#/prompting-is-probability-steering)).
- Users should prompt the model like a tool rather than a colleague, recognizing that the underlying mechanism is a next-token predictor shaped by RLHF ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 22: Don’t Mistake the Mask for the Model](https://haas-ai-classes-fall-26.vercel.app/class5.html#/dont-mistake-the-mask-for-the-model)).
- Attention failure occurs when a model misses the intent of a prompt, as seen when it latches onto a specific detail like a distance question instead of the overall point ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 23: Attention Failure — The Model Answers the Wrong Question](https://haas-ai-classes-fall-26.vercel.app/class5.html#/attention-failure-the-model-answers-the-wrong-question)).
- Voice-to-Text prompts can help because speech naturally includes more context, allows users to state edge cases, and explains intent rather than just task labels ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 24: Why Voice-to-Text Prompts Can Help](https://haas-ai-classes-fall-26.vercel.app/class5.html#/why-voice-to-text-prompts-can-help)).
- LLMs do not start fresh per message; each new request bundles the conversation history, and the model answers based on this provided context ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 25: LLMs Do Not Start Fresh Per Message](https://haas-ai-classes-fall-26.vercel.app/class5.html#/llms-do-not-start-fresh-per-message)).
- Context is everything; the surrounding context, including system instructions, history, and the latest message, changes the conditional probabilities of next tokens without changing the model's learned weights ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 26: Context Is Everything](https://haas-ai-classes-fall-26.vercel.app/class5.html#/context-is-everything)).
- The prompt is context, and more relevant context gives the model less to guess; the prompt supplies background facts and the ask, and more context means more information relevant to the task ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 27: Your Prompt Is Context](https://haas-ai-classes-fall-26.vercel.app/class5.html#/prompts-are-product-interfaces)).

## Related notes

- [[Class 5 - LLMs Prompting and Retrieval]] — taught here
- [[Context Windows]] — the prompt is part of the context
- [[Fine-Tuning and LoRA]] — the other levers besides prompting
- [[Personal Wiki Project]] — persona and research rules are system prompts

## Sources

- [[raw/course-slides/haas-class5.html|Class 5 slides (LLM Behavior, Prompting & Retrieval)]] — Prompting Is Probability Steering, Don’t Mistake the Mask for the Model, Attention Failure — The Model Answers the Wrong Question, Why Voice-to-Text Prompts Can Help, LLMs Do Not Start Fresh Per Message, Context Is Everything, Your Prompt Is Context, Rambling Is a Fine First Draft · [public page](https://haas-ai-classes-fall-26.vercel.app/class5.html)
