---
title: "Git and GitHub"
description: "Git is a version control system that tracks every change to every file in a project, while GitHub is a cloud service that hosts Git repositories, enabling collaboration through features like Pull Requests."
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

# Git and GitHub

Git is a version control system that tracks every change to every file in a project, while GitHub is a cloud service that hosts Git repositories, enabling collaboration through features like Pull Requests. This system solves the problem of tracking changes, allowing users to go back in time and work on the same project simultaneously.

## Key details

- Git is a version control system that keeps a complete history of every change to every file ([Class 1 slides (Code & Programming Foundations), slide 86: What is Git?](https://haas-ai-classes-fall-26.vercel.app/class1.html#/what-is-git)).
- A commit is defined as a snapshot of a project at a specific point in time and is a named, reviewable claim about a coherent change ([Class 1 slides (Code & Programming Foundations), slide 86: What is Git?](https://haas-ai-classes-fall-26.vercel.app/class1.html#/what-is-git)).
- A branch is a parallel version of a project used for experimentation without affecting the main version ([Class 1 slides (Code & Programming Foundations), slide 86: What is Git?](https://haas-ai-classes-fall-26.vercel.app/class1.html#/what-is-git)).
- A repository (repo) is a project folder tracked by Git, containing code files, the full history of changes in the .git/ folder, and configuration files ([Class 1 slides (Code & Programming Foundations), slide 89: What is a Repository?](https://haas-ai-classes-fall-26.vercel.app/class1.html#/what-is-a-repository)).
- A diff shows exactly what has changed, with red lines indicating removals and green lines indicating additions, and this view is constantly seen in pull requests ([Class 1 slides (Code & Programming Foundations), slide 87: What a Diff Looks Like](https://haas-ai-classes-fall-26.vercel.app/class1.html#/what-a-diff-looks-like)).
- GitHub hosts Git repositories in the cloud, providing remote storage, collaboration capabilities, and features like Pull Requests and Issues ([Class 1 slides (Code & Programming Foundations), slide 90: What is GitHub?](https://haas-ai-classes-fall-26.vercel.app/class1.html#/what-is-github)).
- The Git workflow involves steps such as pulling the latest changes, creating a branch, writing code, staging changes with git add, saving a snapshot with git commit, uploading to GitHub with git push, opening a Pull Request for review, and finally merging to main ([Class 1 slides (Code & Programming Foundations), slide 93: The Git Workflow](https://haas-ai-classes-fall-26.vercel.app/class1.html#/the-git-workflow)).
- A Pull Request is a proposed change accompanied by a description, diff, review comments, automated checks, and a merge button, serving as an audit trail for changes ([Class 1 slides (Code & Programming Foundations), slide 96: Pull Requests — Where Business Meets Code](https://haas-ai-classes-fall-26.vercel.app/class1.html#/pull-requests-where-business-meets-code)).

## Related notes

- [[Class 1 - Code Foundations]] — taught here
- [[AI Coding Agents]] — agents need the same review discipline
- [[Secrets and Environment Variables]] — never commit secrets

## Sources

- [[raw/course-slides/haas-class1.html|Class 1 slides (Code & Programming Foundations)]] — The Problem: Tracking Changes, What is Git?, What a Diff Looks Like, Git Branching — Visually, What is a Repository?, What is GitHub?, Essential Git Commands, The Git Workflow · [public page](https://haas-ai-classes-fall-26.vercel.app/class1.html)
