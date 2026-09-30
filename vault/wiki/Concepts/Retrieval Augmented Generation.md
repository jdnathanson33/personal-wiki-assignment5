---
title: "Retrieval Augmented Generation"
description: "Retrieval Augmented Generation (RAG) is a method that allows a Large Language Model (LLM) to access external, private data to ground its answers, addressing the limitation that an LLM's knowledge is frozen at its training data."
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

# Retrieval Augmented Generation

Retrieval Augmented Generation (RAG) is a method that allows a Large Language Model (LLM) to access external, private data to ground its answers, addressing the limitation that an LLM's knowledge is frozen at its training data. It matters because it enables the use of private knowledge without retraining the model, which grounds answers in evidence and reduces hallucinations.

## Key details

- RAG allows an LLM to answer questions based on retrieved documents rather than its internal memory ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 64: Why RAG Matters](https://haas-ai-classes-fall-26.vercel.app/class5.html#/why-rag-matters)).
- RAG grounds answers in evidence, meaning the model cites retrieved documents, such as a specific revenue figure, instead of guessing ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 64: Why RAG Matters](https://haas-ai-classes-fall-26.vercel.app/class5.html#/why-rag-matters)).
- RAG enables the use of private knowledge, like company internal documents, by retrieving and injecting it into the prompt without requiring fine-tuning or retraining ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 64: Why RAG Matters](https://haas-ai-classes-fall-26.vercel.app/class5.html#/why-rag-matters)).
- RAG is used when an LLM searches the web before answering, when a code model reads project files, when a chatbot answers from internal HR docs, or when a support tool pulls answers from a help center ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 63: You Already Use RAG](https://haas-ai-classes-fall-26.vercel.app/class5.html#/you-already-use-rag)).
- The process involves finding relevant information, giving it to the AI with the question, and using external sources, vector matching, context, and an AI answer ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 65: How RAG Works](https://haas-ai-classes-fall-26.vercel.app/class5.html#/building-a-tiny-rag-demo)).
- Chunking text splits long documents into smaller, useful passages, keeping related ideas and their context together so that the question can select relevant pieces to include in the model’s context ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 66: Chunking Text](https://haas-ai-classes-fall-26.vercel.app/class5.html#/chunking-useful-pieces)).
- Vector databases store numerical representations of text called embeddings, and vector search finds chunks near the question by comparing their vector representations, which is used to retrieve passages for the model to read ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 67: Vector Databases & Vector Search](https://haas-ai-classes-fall-26.vercel.app/class5.html#/vector-databases-search-by-meaning)).

## Related notes

- [[Class 5 - LLMs Prompting and Retrieval]] — taught here
- [[Personal Wiki Project]] — my RAG implementation
- [[Tokens and Embeddings]] — embeddings make vector search possible
- [[Hallucination]] — RAG is one defense
- [[Context Windows]] — retrieved passages must fit the context

## Sources

- [[raw/course-slides/haas-class5.html|Class 5 slides (LLM Behavior, Prompting & Retrieval)]] — There’s Still a Problem, Retrieval Augmented Generation (RAG), You Already Use RAG, Why RAG Matters, How RAG Works, Chunking Text, Vector Databases & Vector Search, AI Can Write SQL · [public page](https://haas-ai-classes-fall-26.vercel.app/class5.html)
