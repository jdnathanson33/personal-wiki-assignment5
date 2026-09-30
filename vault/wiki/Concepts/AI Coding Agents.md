---
title: "AI Coding Agents"
description: "AI Coding Agents are tools like Claude Code and OpenAI Codex that run in the terminal, capable of reading codebases, writing files, and running commands autonomously."
type: concept
sources:
  - "[[raw/course-slides/haas-class1.html]]"
  - "[[raw/course-slides/haas-class5.html]]"
source_ids:
  - class1-slides
  - class5-slides
source_sha256:
  - class1-slides@f4383cbe1ffe
  - class5-slides@a53bb050753d
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# AI Coding Agents

AI Coding Agents are tools like Claude Code and OpenAI Codex that run in the terminal, capable of reading codebases, writing files, and running commands autonomously. They are powerful but require human oversight, especially regarding code quality and accountability.

## Key details

- Claude Code and OpenAI Codex are AI agents that operate in the terminal rather than as browser chatbots ([Class 1 slides (Code & Programming Foundations), slide 113: Claude Code & OpenAI Codex](https://haas-ai-classes-fall-26.vercel.app/class1.html#/claude-code-openai-codex)).
- Both Claude Code and OpenAI Codex can read codebases, write files, run commands, and iterate autonomously ([Class 1 slides (Code & Programming Foundations), slide 113: Claude Code & OpenAI Codex](https://haas-ai-classes-fall-26.vercel.app/class1.html#/claude-code-openai-codex)).
- The CLI is considered the most powerful version of agents because it offers full filesystem access, command execution capabilities, and autonomous iteration ([Class 1 slides (Code & Programming Foundations), slide 114: Why the CLI Is the Most Powerful Version](https://haas-ai-classes-fall-26.vercel.app/class1.html#/why-the-cli-is-the-most-powerful-version)).
- YOLO Mode allows agents like Claude Code and OpenAI Codex to skip permission prompts, meaning they create files, install packages, and run commands without prior user confirmation, suitable for greenfield projects ([Class 1 slides (Code & Programming Foundations), slide 115: YOLO Mode](https://haas-ai-classes-fall-26.vercel.app/class1.html#/yolo-mode)).
- Plan Mode involves typing `/plan` in Claude Code to describe a desired build, allowing the AI to create a detailed plan for review before execution, which can then be run in YOLO mode ([Class 1 slides (Code & Programming Foundations), slide 116: Plan Mode](https://haas-ai-classes-fall-26.vercel.app/class1.html#/plan-mode)).
- When using an agent, it is important to slow down for decisions requiring context (like technology choices) or when dealing with production data, and to verify outputs by running tests ([Class 1 slides (Code & Programming Foundations), slide 117: When NOT to Reach for the Agent](https://haas-ai-classes-fall-26.vercel.app/class1.html#/when-not-to-reach-for-the-agent)).
- Before accepting an agent's diff, a checklist should be used to verify if the change matches the brief, check for unexpected files, look for secrets, and ensure tests still pass ([Class 1 slides (Code & Programming Foundations), slide 120: Before You Accept an Agent’s Diff](https://haas-ai-classes-fall-26.vercel.app/class1.html#/before-you-accept-an-agents-diff)).

## Related notes

- [[Class 1 - Code Foundations]] — introduced here
- [[Git and GitHub]] — diffs and pull requests are how agent work is reviewed
- [[Clean Code]] — what to look for in generated code
- [[Prompt Engineering]] — clear prompts improve agent output

## Sources

- [[raw/course-slides/haas-class1.html|Class 1 slides (Code & Programming Foundations)]] — Reviewing What an AI Writes, Claude Code & OpenAI Codex, Why the CLI Is the Most Powerful Version, YOLO Mode, Plan Mode, When NOT to Reach for the Agent, Plain-Language Reasoning Improves AI Output, Explain the Program Before You Run It · [public page](https://haas-ai-classes-fall-26.vercel.app/class1.html)
- [[raw/course-slides/haas-class5.html|Class 5 slides (LLM Behavior, Prompting & Retrieval)]] — Tip: Use Plan Mode · [public page](https://haas-ai-classes-fall-26.vercel.app/class5.html)
