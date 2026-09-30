---
title: "Class 5 - LLMs Prompting and Retrieval"
description: "This class covers LLM behavior, focusing on prompting techniques, context management, fine-tuning, and retrieval methods like RAG."
type: course
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

# Class 5 - LLMs Prompting and Retrieval

This class covers LLM behavior, focusing on prompting techniques, context management, fine-tuning, and retrieval methods like RAG. It emphasizes practical application for building AI workflows rather than deep ML engineering, addressing concepts like hallucination and the role of different model behaviors.

## Key details

- Prompting is used to steer the probability distribution, potentially with or without thinking mode, to achieve useful answers initially ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 5: What This Class Gives You](https://haas-ai-classes-fall-26.vercel.app/class5.html#/what-this-class-gives-you)).
- Context management addresses why models forget, the role of compaction, and how this limits AI features ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 5: What This Class Gives You](https://haas-ai-classes-fall-26.vercel.app/class5.html#/what-this-class-gives-you)).
- Fine-tuning, RLHF, and alignment are what labs do under the hood, so ideas like "Anthropic values" or "OpenAI personality" become real design choices rather than magic ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 5: What This Class Gives You](https://haas-ai-classes-fall-26.vercel.app/class5.html#/what-this-class-gives-you)).
- Retrieval Augmented Generation (RAG) allows bolting company data onto a general model without retraining, contrasting with the model's frozen training data ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 5: What This Class Gives You](https://haas-ai-classes-fall-26.vercel.app/class5.html#/what-this-class-gives-you); [Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 62: Retrieval Augmented Generation (RAG)](https://haas-ai-classes-fall-26.vercel.app/class5.html#/retrieval-augmented-generation-rag)).
- Prompt engineering involves techniques such as using .md files, system prompts, and CLAUDE.md, following a "golden rule" ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 6: Agenda](https://haas-ai-classes-fall-26.vercel.app/class5.html#/agenda)).
- Thinking models are used when a model plans before generating a response ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 6: Agenda](https://haas-ai-classes-fall-26.vercel.app/class5.html#/agenda)).
- Hallucination can be mitigated by RAG retrieving evidence and citing sources, or by using higher thinking modes, though higher modes increase computation costs ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 59: Four Defenses](https://haas-ai-classes-fall-26.vercel.app/class5.html#/four-defenses)).
- Fine-tuning changes the model, while prompting changes instructions and examples, and retrieval finds relevant material as context without updating model weights ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 18: Three Levers, Three Jobs](https://haas-ai-classes-fall-26.vercel.app/class5.html#/the-three-levers-visually)).

## Related notes

- [[Fundamentals of Agentic AI]] — course map
- [[Prompt Engineering]] — covered in this class
- [[Context Windows]] — covered in this class
- [[Fine-Tuning and LoRA]] — covered in this class
- [[Hallucination]] — covered in this class
- [[Retrieval Augmented Generation]] — covered in this class
- [[Local Open Models]] — covered in this class
- [[Personal Wiki Project]] — the assignment for this class
- [[Class 4 - Deep Learning and Transformers]] — previous class

## Sources

- [[raw/course-slides/haas-class5.html|Class 5 slides (LLM Behavior, Prompting & Retrieval)]] — What This Class Gives You, Agenda, Three Levers, Three Jobs, The Golden Rule of Prompting, Four Defenses, Retrieval Augmented Generation (RAG), Build Your Personal Wiki · [public page](https://haas-ai-classes-fall-26.vercel.app/class5.html)
