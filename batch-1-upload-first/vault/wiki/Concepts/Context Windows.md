---
title: "Context Windows"
description: "Context windows define the maximum amount of information, measured in tokens, a model can hold at once, which directly impacts its capacity for processing and memory."
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

# Context Windows

Context windows define the maximum amount of information, measured in tokens, a model can hold at once, which directly impacts its capacity for processing and memory. Understanding context windows is crucial because they relate to limitations like context rot, the need for compression, and the strategy of placing stable rules in durable locations.

## Key details

- A context window is the maximum space a model can hold simultaneously, shared by user messages and the model's replies ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 33: What Is a Context Window?](https://haas-ai-classes-fall-26.vercel.app/class5.html#/what-is-a-context-window)).
- The context window capacity is measured in tokens, and earlier messages remain in context, meaning the bar does not reset between turns ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 33: What Is a Context Window?](https://haas-ai-classes-fall-26.vercel.app/class5.html#/what-is-a-context-window)).
- State-of-the-art models like Claude Opus have a context window of 1 million tokens, enough to hold two copies of the Lord of the Rings trilogy (about 500,000 tokens each) ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 34: How Big Is a Context Window?](https://haas-ai-classes-fall-26.vercel.app/class5.html#/how-big-is-a-context-window)).
- Larger context windows allow the model to reason over larger inputs such as entire codebases or full documents at once ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 34: How Big Is a Context Window?](https://haas-ai-classes-fall-26.vercel.app/class5.html#/how-big-is-a-context-window)).
- Increasing context size raises cost and latency, and the model only sees the active context, lacking durable memory unless information is resent ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 35: Bigger Context Is Not a Free Solution](https://haas-ai-classes-fall-26.vercel.app/class5.html#/bigger-context-is-not-a-free-solution)).
- Context rot occurs as prompts become cluttered, potentially causing the model to miss, misweight, or contradict existing material, and long chats can become confused ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 36: Context Rot Is Real](https://haas-ai-classes-fall-26.vercel.app/class5.html#/context-rot-is-real)).
- When the window fills, compaction is a lossy summarization process that summarizes old conversation into a compact block to free up space ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 37: But Context Fills Up — Enter Compression](https://haas-ai-classes-fall-26.vercel.app/class5.html#/but-context-fills-up-enter-compression)).
- System instructions and durable project files are better places for stable rules than long casual conversations because they survive compaction and new chats ([Class 5 slides (LLM Behavior, Prompting & Retrieval), slide 38: Put Stable Rules in Stable Places](https://haas-ai-classes-fall-26.vercel.app/class5.html#/put-stable-rules-in-stable-places)).

## Related notes

- [[Class 5 - LLMs Prompting and Retrieval]] — taught here
- [[Prompt Engineering]] — what goes into the context
- [[Retrieval Augmented Generation]] — select relevant passages instead of sending everything

## Sources

- [[raw/course-slides/haas-class5.html|Class 5 slides (LLM Behavior, Prompting & Retrieval)]] — What Is a Context Window?, How Big Is a Context Window?, Bigger Context Is Not a Free Solution, Context Rot Is Real, But Context Fills Up — Enter Compression, Put Stable Rules in Stable Places, Why Everyone Talks About Tokens · [public page](https://haas-ai-classes-fall-26.vercel.app/class5.html)
