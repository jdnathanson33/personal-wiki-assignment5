---
title: "Personal Wiki Project"
description: "The Personal Wiki Project is a Class 5 assignment requiring the development of a personal wiki powered by a local model, retrieval, and chat/ask/search modes."
type: project
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

# Personal Wiki Project

The Personal Wiki Project is a Class 5 assignment requiring the development of a personal wiki powered by a local model, retrieval, and chat/ask/search modes. This project involves building a wiki from personal notes using local Gemma and RAG, and creating a CLI to interact with the system.

## Key details

- The personal wiki must be built from 3+ original sources with readable note names, topic groups, and meaningful links in Obsidian ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 70: Build Your Personal Wiki](https://haas-ai-classes-fall-26.vercel.app/class5.html#/assignment-4-personal-wiki-with-local-gemma-rag)).
- The personal CLI should allow users to chat to brainstorm, ask for cited answers, and search original passages ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 70: Build Your Personal Wiki](https://haas-ai-classes-fall-26.vercel.app/class5.html#/assignment-4-personal-wiki-with-local-gemma-rag)).
- The system must support a chat function that acts as a personal assistant with conversation context and retrieval when needed ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 70: Build Your Personal Wiki](https://haas-ai-classes-fall-26.vercel.app/class5.html#/assignment-4-personal-wiki-with-local-gemma-rag)).
- The 'ask' function provides standalone factual answers with evidence and citations, or states if evidence is missing ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 70: Build Your Personal Wiki](https://haas-ai-classes-fall-26.vercel.app/class5.html#/assignment-4-personal-wiki-with-local-gemma-rag)).
- The search function returns original passages and source locations without generating an answer ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 70: Build Your Personal Wiki](https://haas-ai-classes-fall-26.vercel.app/class5.html#/assignment-4-personal-wiki-with-local-gemma-rag)).
- The project requires testing with 3 answerable questions and 1 unsupported question, plus chat and search checks ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 70: Build Your Personal Wiki](https://haas-ai-classes-fall-26.vercel.app/class5.html#/assignment-4-personal-wiki-with-local-gemma-rag)).
- The project must be runnable offline by disconnecting the internet and restarting the CLI to record ingestion and tests ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 70: Build Your Personal Wiki](https://haas-ai-classes-fall-26.vercel.app/class5.html#/assignment-4-personal-wiki-with-local-gemma-rag)).
- The README must explain setup, model and runtime choice, device specs, measured memory and response time, architecture, test results, and one limitation with a proposed improvement ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 70: Build Your Personal Wiki](https://haas-ai-classes-fall-26.vercel.app/class5.html#/assignment-4-personal-wiki-with-local-gemma-rag)).

## Related notes

- [[Fundamentals of Agentic AI]] — course map
- [[Retrieval Augmented Generation]] — ask mode is a RAG workflow
- [[Local Open Models]] — runs Gemma locally
- [[Context Windows]] — passages must fit the context window
- [[Hallucination]] — citations and insufficient-evidence answers are the defense
- [[Class 5 - LLMs Prompting and Retrieval]] — the class this assignment came from

## Sources

- [[raw/course-slides/haas-class5.html|Class 5 slides (LLM Behavior, Prompting & Retrieval)]] — Open Models & Running Locally, Build Your Personal Wiki · [public page](https://haas-ai-classes-fall-26.vercel.app/class5.html)
