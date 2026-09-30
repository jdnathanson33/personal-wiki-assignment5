---
title: "Local Open Models"
description: "Local Open Models refer to open-weight models that can be run on a student's own hardware, which involves considerations for licensing, local inference setup, and memory calculations."
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

# Local Open Models

Local Open Models refer to open-weight models that can be run on a student's own hardware, which involves considerations for licensing, local inference setup, and memory calculations. This topic is relevant as it addresses the deployment and operational aspects of open models.

## Key details

- Open weights, open source, and local deployment describe different properties of a model. ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 56: Open Models & Running Locally](https://haas-ai-classes-fall-26.vercel.app/class5.html#/open-models-and-local-memory))
- Local inference means the model computation runs on the student’s own hardware. ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 56: Open Models & Running Locally](https://haas-ai-classes-fall-26.vercel.app/class5.html#/open-models-and-local-memory))
- For offline operation, one must download the compatible model and runtime first, select the local model, and ensure tools, embedding models, and other workflow dependencies are local too. ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 56: Open Models & Running Locally](https://haas-ai-classes-fall-26.vercel.app/class5.html#/open-models-and-local-memory))
- Memory calculations use decimal GB and nominal parameter counts: number of parameters × bits per weight ÷ 8. For example, 8 billion weights at 16 bits occupy about 16 GB and at 4 bits about 4 GB before overhead. ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 56: Open Models & Running Locally](https://haas-ai-classes-fall-26.vercel.app/class5.html#/open-models-and-local-memory))
- For full GPU residency, a 32B model’s nominal 16 GB of 4-bit weights leaves no room on a 16 GB GPU for overhead and context. ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 56: Open Models & Running Locally](https://haas-ai-classes-fall-26.vercel.app/class5.html#/open-models-and-local-memory))
- CPU-only inference can work with sufficient system RAM but may be slower. ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 56: Open Models & Running Locally](https://haas-ai-classes-fall-26.vercel.app/class5.html#/open-models-and-local-memory))

## Related notes

- [[Class 5 - LLMs Prompting and Retrieval]] — taught here
- [[Personal Wiki Project]] — runs Gemma locally
- [[Localhost and Ports]] — the model server listens on localhost

## Sources

- [[raw/course-slides/haas-class5.html|Class 5 slides (LLM Behavior, Prompting & Retrieval)]] — The Biggest Shift Since GPT, What Are “Thinking” Models?, Model Tiers, Open Models & Running Locally · [public page](https://haas-ai-classes-fall-26.vercel.app/class5.html)
