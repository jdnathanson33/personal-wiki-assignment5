---
title: "Transformer Attention"
description: "Transformer Attention is a mechanism that allows a model to combine information from available token positions, replacing the sequential processing of RNNs."
type: concept
sources:
  - "[[raw/course-slides/haas-class4.html]]"
source_ids:
  - class4-slides
source_sha256:
  - class4-slides@6091b9482247
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Transformer Attention

Transformer Attention is a mechanism that allows a model to combine information from available token positions, replacing the sequential processing of RNNs. It enables attention to connect directly to earlier positions within the context window, allowing a word's representation to change based on the surrounding context.

## Key details

- Attention combines information from the token positions available to the current position ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 47: Attention Changes the Question](https://haas-ai-classes-fall-26.vercel.app/class4.html#/attention-changes-the-question)).
- Attention can connect directly to earlier positions within the context window ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 47: Attention Changes the Question](https://haas-ai-classes-fall-26.vercel.app/class4.html#/attention-changes-the-question)).
- A word's starting embedding is shared, but its representation changes as the network combines it with available context ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 50: Why This Matters: Same Word, Different Meaning](https://haas-ai-classes-fall-26.vercel.app/class4.html#/why-this-matters-same-word-different-meaning)).
- Attention updates the embedding for a token by pulling it toward a meaning based on its context (e.g., "American shrew" pulls "mole" toward the animal direction) ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 51: Attention Updates Meaning](https://haas-ai-classes-fall-26.vercel.app/class4.html#/attention-updates-meaning)).
- In a GPT-style model, a position can attend to itself and earlier positions, while future positions are masked out ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 48: Attention: Which Tokens Can It Use?](https://haas-ai-classes-fall-26.vercel.app/class4.html#/attention-every-word-looks-at-every-other-word)).
- Training can process many positions in parallel while respecting a causal mask, and text generation still proceeds one token at a time ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 47: Attention Changes the Question](https://haas-ai-classes-fall-26.vercel.app/class4.html#/attention-changes-the-question)).
- Attention allows a word to draw on useful context many sentences earlier, connecting positions directly without following a pronoun chain one mention at a time ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 49: Attention Can Connect Distant Words](https://haas-ai-classes-fall-26.vercel.app/class4.html#/attention-on-a-book-page)).

## Related notes

- [[Class 4 - Deep Learning and Transformers]] — taught here
- [[Tokens and Embeddings]] — attention works on token vectors
- [[Tiny nanoGPT Model]] — 2 transformer blocks, 4 heads
- [[Context Windows]] — attention cost grows with context

## Sources

- [[raw/course-slides/haas-class4.html|Class 4 slides (Deep Learning, Embeddings & Transformers)]] — The Problem with Order, RNNs: Adding Memory, The Bottleneck Problem, “Attention Is All You Need” (2017), Attention Changes the Question, Attention: Which Tokens Can It Use?, Attention Can Connect Distant Words, Why This Matters: Same Word, Different Meaning · [public page](https://haas-ai-classes-fall-26.vercel.app/class4.html)
