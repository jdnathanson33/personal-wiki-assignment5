---
title: "Hallucination"
description: "Hallucination occurs because fluent systems are designed to reward plausible continuation rather than guaranteeing source access or truth verification."
type: concept
sources:
  - "[[raw/course-slides/haas-class5.html]]"
  - "[[raw/course-slides/haas-class4.html]]"
source_ids:
  - class5-slides
  - class4-slides
source_sha256:
  - class5-slides@a53bb050753d
  - class4-slides@6091b9482247
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Hallucination

Hallucination occurs because fluent systems are designed to reward plausible continuation rather than guaranteeing source access or truth verification. This is a system property where plausibility without evidence is the failure mode, and it can arise from normal generation processes.

## Key details

- An LLM contains learned statistical structure in its parameters and does not consult a verified, current, cited database unless provided one ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 10: “It Knows” Is a Risky Shorthand](https://haas-ai-classes-fall-26.vercel.app/class5.html#/it-knows-is-a-risky-shorthand)).
- The next-token objective rewards plausible continuation and does not guarantee source access, truth verification, or current information ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 58: Why Fluent Systems Can Be Wrong](https://haas-ai-classes-fall-26.vercel.app/class5.html#/why-fluent-systems-can-be-wrong)).
- Probability is not truth; the chart scores possible next tokens, not whether a claim is correct ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 58: Why Fluent Systems Can Be Wrong](https://haas-ai-classes-fall-26.vercel.app/class5.html#/why-fluent-systems-can-be-wrong)).
- Plausibility without evidence is the failure mode, and grounding the answer in checkable evidence is necessary ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 58: Why Fluent Systems Can Be Wrong](https://haas-ai-classes-fall-26.vercel.app/class5.html#/why-fluent-systems-can-be-wrong)).
- Retrieval can bring in irrelevant or incorrect material, and a generated citation can be fabricated or fail to support its claim ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 59: Four Defenses](https://haas-ai-classes-fall-26.vercel.app/class5.html#/four-defenses)).
- Higher thinking modes can improve reasoning but can still produce an incorrect answer and do not create missing source evidence ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 59: Four Defenses](https://haas-ai-classes-fall-26.vercel.app/class5.html#/four-defenses)).
- Lower temperatures concentrate the sampling distribution toward already-likely tokens, which can cause a likely false claim to become more consistently repeated but is not a general factual-accuracy guarantee ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 59: Four Defenses](https://haas-ai-classes-fall-26.vercel.app/class5.html#/four-defenses)).

## Related notes

- [[Class 5 - LLMs Prompting and Retrieval]] — taught here
- [[Retrieval Augmented Generation]] — grounding answers in sources
- [[Sampling Temperature]] — sampling adds variety and risk

## Sources

- [[raw/course-slides/haas-class5.html|Class 5 slides (LLM Behavior, Prompting & Retrieval)]] — “It Knows” Is a Risky Shorthand, Why Fluent Systems Can Be Wrong, Four Defenses · [public page](https://haas-ai-classes-fall-26.vercel.app/class5.html)
- [[raw/course-slides/haas-class4.html|Class 4 slides (Deep Learning, Embeddings & Transformers)]] — A Fluent Answer Is Still a Prediction · [public page](https://haas-ai-classes-fall-26.vercel.app/class4.html)
