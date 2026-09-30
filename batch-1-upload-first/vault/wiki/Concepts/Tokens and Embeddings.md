---
title: "Tokens and Embeddings"
description: "Tokens are pieces into which text is broken by a tokenizer, and embeddings are learned vectors that represent words or tokens in a high-dimensional space."
type: concept
sources:
  - "[[raw/course-slides/haas-class4.html]]"
  - "[[raw/assignments/custom-llm-README.md]]"
source_ids:
  - class4-slides
  - custom-llm-readme
source_sha256:
  - class4-slides@6091b9482247
  - custom-llm-readme@532515c6591e
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Tokens and Embeddings

Tokens are pieces into which text is broken by a tokenizer, and embeddings are learned vectors that represent words or tokens in a high-dimensional space. These embeddings allow words to be compared mathematically based on their learned relationships and contexts.

## Key details

- An embedding is a learned vector (a list of numbers) that represents a word or token, and training adjusts these numbers to help the model make predictions ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 34: The Problem: Words Aren’t Numbers](https://haas-ai-classes-fall-26.vercel.app/class4.html#/the-problem-words-arent-numbers)).
- Words in similar contexts tend to have similar embeddings, and words with similar meanings cluster together in vector space ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 35: Words as Points in Space](https://haas-ai-classes-fall-26.vercel.app/class4.html#/words-as-points-in-space)).
- An embedding represents a word as a vector, and nearby vectors can capture related meanings; for example, "Dog" and "puppy" have related meanings, so their vectors are close together ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 36: Distance Reflects Meaning](https://haas-ai-classes-fall-26.vercel.app/class4.html#/distance-becomes-a-retrieval-primitive)).
- Distance between vectors measures similarity, where a smaller distance represents greater similarity, such as the distance from "dog" to "puppy" being $\sqrt{1.25}$ ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 36: Distance Reflects Meaning](https://haas-ai-classes-fall-26.vercel.app/class4.html#/distance-becomes-a-retrieval-primitive)).
- Context determines meaning, and modern models create contextual representations where the vector for a word is adjusted on the fly by the surrounding words via the attention mechanism ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 38: Context Determines Meaning](https://haas-ai-classes-fall-26.vercel.app/class4.html#/context-determines-meaning)).
- A tokenizer breaks text into pieces called tokens, and BPE (byte-pair encoding) learns which pieces to combine ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 40: How Words Become Tokens](https://haas-ai-classes-fall-26.vercel.app/class4.html#/from-words-to-tokens)).
- A token ID is a lookup index that selects a row in the model’s learned embedding table, and a single word can be represented by multiple tokens ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 40: How Words Become Tokens](https://haas-ai-classes-fall-26.vercel.app/class4.html#/from-words-to-tokens)).
- Real embedding vectors usually contain many more numbers, and different tokenizers may produce different splits and token counts for the same text ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 40: How Words Become Tokens](https://haas-ai-classes-fall-26.vercel.app/class4.html#/from-words-to-tokens)).

## Related notes

- [[Tiny nanoGPT Model]] — where I traced tokens and embeddings
- [[Transformer Attention]] — attention updates token vectors
- [[Class 4 - Deep Learning and Transformers]] — taught here
- [[Retrieval Augmented Generation]] — embeddings power vector search

## Sources

- [[raw/course-slides/haas-class4.html|Class 4 slides (Deep Learning, Embeddings & Transformers)]] — The Problem: Words Aren’t Numbers, Words as Points in Space, Distance Reflects Meaning, Context Determines Meaning, How Words Become Tokens · [public page](https://haas-ai-classes-fall-26.vercel.app/class4.html)
- [[raw/assignments/custom-llm-README.md|nanoGPT README]] — 7. Tracing the learning process with actual values
