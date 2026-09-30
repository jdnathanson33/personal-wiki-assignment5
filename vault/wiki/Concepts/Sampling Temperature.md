---
title: "Sampling Temperature"
description: "Sampling Temperature controls how random the output is by dividing the next-token scores before applying softmax, affecting the variety of generated text."
type: concept
sources:
  - "[[raw/course-slides/haas-class5.html]]"
  - "[[raw/assignments/custom-llm-README.md]]"
source_ids:
  - class5-slides
  - custom-llm-readme
source_sha256:
  - class5-slides@a53bb050753d
  - custom-llm-readme@532515c6591e
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Sampling Temperature

Sampling Temperature controls how random the output is by dividing the next-token scores before applying softmax, affecting the variety of generated text. Lower temperatures favor more likely continuations, while higher temperatures explore more possibilities and raise variance.

## Key details

- Temperature is a setting in every API call that controls how "random" the output is ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 13: Temperature: The Creativity Dial](https://haas-ai-classes-fall-26.vercel.app/class5.html#/temperature-the-creativity-dial)).
- Lower temperature settings, such as 0.3, cause the probability distribution to sharpen, leading to fewer surprises and keeping the model on its most probable path.
- Higher temperature settings, such as 1.2, flatten the distribution, causing rarer words to appear more often.
- At temperature 0.3, the model produces samples like "the report about the item explains the price in detail .".
- At temperature 0.8, the model produces samples like "the report about the car explains the journey in detail .".
- At temperature 1.2, the model produces samples like "ivy learned that the opposite of slow is fast .".
- The model is confident enough that at temperatures 0.8 and 1.2, the seeded draw picked identical samples.

## Related notes

- [[Tiny nanoGPT Model]] — temperature comparison
- [[Prompt Engineering]] — prompts and temperature both steer the distribution
- [[Hallucination]] — sampling can produce fluent wrong text

## Sources

- [[raw/course-slides/haas-class5.html|Class 5 slides (LLM Behavior, Prompting & Retrieval)]] — Slide 2 of 2: LLMs Are Probabilistic, Temperature: The Creativity Dial · [public page](https://haas-ai-classes-fall-26.vercel.app/class5.html)
- [[raw/assignments/custom-llm-README.md|nanoGPT README]] — 7. Tracing the learning process with actual values
