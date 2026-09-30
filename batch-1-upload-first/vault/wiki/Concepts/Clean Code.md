---
title: "Clean Code"
description: "Clean Code focuses on readability and maintainability by emphasizing principles like guard clauses, named constants, single-responsibility functions, and splitting projects by responsibility."
type: concept
sources:
  - "[[raw/course-slides/haas-class1.html]]"
source_ids:
  - class1-slides
source_sha256:
  - class1-slides@f4383cbe1ffe
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Clean Code

Clean Code focuses on readability and maintainability by emphasizing principles like guard clauses, named constants, single-responsibility functions, and splitting projects by responsibility. These practices ensure that code is easier for teammates and AI agents to read and modify, which is crucial because code is read far more often than it is written.

## Key details

- Readability is important because code is read dozens of times by teammates and AI agents after being written ([Class 1 slides (Code & Programming Foundations), slide 65: Code Is Read Far More Than It Is Written](https://haas-ai-classes-fall-26.vercel.app/class1.html#/code-is-read-far-more-than-it-is-written)).
- The WTF-per-Minute Metric is a social metric measuring the gap between what the code does and what a reader expected it to do, which can only be measured by a second human ([Class 1 slides (Code & Programming Foundations), slide 66: The WTF-per-Minute Metric](https://haas-ai-classes-fall-26.vercel.app/class1.html#/the-wtf-per-minute-metric)).
- Spaghetti Code is dangerous because it forces the reader to ask questions about variables, constants, nesting, and logic, leading to future bugs ([Class 1 slides (Code & Programming Foundations), slide 68: What Made That Hard](https://haas-ai-classes-fall-26.vercel.app/class1.html#/what-made-that-hard)).
- Guard Clauses beat nesting because handling exceptional cases first allows the rest of the function to represent the normal path, avoiding deep nesting ([Class 1 slides (Code & Programming Foundations), slide 70: Guard Clauses Beat Nesting](https://haas-ai-classes-fall-26.vercel.app/class1.html#/guard-clauses-beat-nesting)).
- Magic Numbers should be replaced with named constants (e.g., COLLECTIONS_CUTOFF_DAYS) so that each number explicitly states what it represents, making changes clearer ([Class 1 slides (Code & Programming Foundations), slide 71: Magic Numbers Have Names](https://haas-ai-classes-fall-26.vercel.app/class1.html#/magic-numbers-have-names)).
- One Function, One Job means splitting functions so that a function performs only one task, allowing for easier testing and reuse ([Class 1 slides (Code & Programming Foundations), slide 72: One Function, One Job](https://haas-ai-classes-fall-26.vercel.app/class1.html#/one-function-one-job)).
- Comments should explain why a decision was made (a record of a decision) rather than restating what the code already shows, as good names remove the need for "what" comments ([Class 1 slides (Code & Programming Foundations), slide 73: Comments Explain Why, Not What](https://haas-ai-classes-fall-26.vercel.app/class1.html#/comments-explain-why-not-what)).
- A project is best treated as a folder rather than a single file, as opening a folder allows agents to understand the layout and follow imports across files ([Class 1 slides (Code & Programming Foundations), slide 75: A Project Is a Folder, Not a File](https://haas-ai-classes-fall-26.vercel.app/class1.html#/a-project-is-a-folder-not-a-file)).
- Splitting by Responsibility means organizing files so that each file answers one kind of question, making it easier to pinpoint where a change belongs ([Class 1 slides (Code & Programming Foundations), slide 76: Splitting by Responsibility](https://haas-ai-classes-fall-26.vercel.app/class1.html#/splitting-by-responsibility)).

## Related notes

- [[Class 1 - Code Foundations]] — taught here
- [[AI Coding Agents]] — reviewing what an AI writes
- [[Testing and CI]] — tests make refactoring safe

## Sources

- [[raw/course-slides/haas-class1.html|Class 1 slides (Code & Programming Foundations)]] — Code Is Read Far More Than It Is Written, The WTF-per-Minute Metric, Spaghetti Code, What Made That Hard, The Same Logic, Cleaned Up, Guard Clauses Beat Nesting, Magic Numbers Have Names, One Function, One Job · [public page](https://haas-ai-classes-fall-26.vercel.app/class1.html)
