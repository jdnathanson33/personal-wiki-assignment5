---
title: "Cloud Deployment"
description: "Cloud deployment involves moving a tested version of code into an environment, which requires managing different environments and planning for rollbacks."
type: concept
sources:
  - "[[raw/course-slides/haas-class2.html]]"
  - "[[raw/assignments/networking-tracker-README.md]]"
source_ids:
  - class2-slides
  - networking-tracker-readme
source_sha256:
  - class2-slides@00a0281db897
  - networking-tracker-readme@c218a4704709
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Cloud Deployment

Cloud deployment involves moving a tested version of code into an environment, which requires managing different environments and planning for rollbacks. The Class 2 assignment named Next.js + Supabase + Vercel; my Networking Tracker was deployed on Vercel with Neon Postgres and Neon Auth.

## Key details

- The cloud is defined as someone else’s computers in a data center, allowing users to rent computing power instead of buying and maintaining servers ([Class 2 slides (Software Systems), slide 41: What is “The Cloud”?](https://haas-ai-classes-fall-26.vercel.app/class2.html#/what-is-the-cloud)).
- Deployment is the process of moving a tested version into an environment ([Class 2 slides (Software Systems), slide 59: Environments Are Intentionally Different Places](https://haas-ai-classes-fall-26.vercel.app/class2.html#/environments-are-intentionally-different-places)).
- Environments are intentionally different places, with Development using local fake/local data and Production using real users and real credentials ([Class 2 slides (Software Systems), slide 59: Environments Are Intentionally Different Places](https://haas-ai-classes-fall-26.vercel.app/class2.html#/environments-are-intentionally-different-places)).
- Secrets should be stored in server-only environment settings for production, and the backend should read secrets at runtime, never exposing them to the frontend ([Class 2 slides (Software Systems), slide 45: Keep Secrets Out of Your Code](https://haas-ai-classes-fall-26.vercel.app/class2.html#/keep-secrets-out-of-your-code)).
- On Vercel, deploying involves adding a new project by importing the repository and accepting auto-detected Next.js settings ([[raw/assignments/networking-tracker-README.md#Deployment|§ Deployment]]).
- Rollback on Vercel is achieved by promoting a previous deployment, which is described as a one-click action ([Class 2 slides (Software Systems), slide 60: Rollback: The Undo Button You Design in Advance](https://haas-ai-classes-fall-26.vercel.app/class2.html#/rollback-the-undo-button-you-design-in-advance)).
- For the networking tracker assignment, deployment involves pushing the repository to GitHub, adding environment variables (like `NEXT_PUBLIC_NEON_AUTH_URL`) in Vercel settings, and applying the schema SQL ([[raw/assignments/networking-tracker-README.md#Deployment|§ Deployment]]).

## Related notes

- [[Class 2 - Software Systems]] — taught here
- [[Networking Tracker]] — deployed on Vercel
- [[Testing and CI]] — tests as a release gate
- [[Localhost and Ports]] — local vs deployed

## Sources

- [[raw/course-slides/haas-class2.html|Class 2 slides (Software Systems)]] — What is “The Cloud”?, Deploying Makes Your App Available to Users, Regression Tests Catch Distant Breakage, Keep Secrets Out of Your Code, The Assignment, Definition of Done: Your Rubric, Congratulations — You Are Now AI Engineers, Next Class · [public page](https://haas-ai-classes-fall-26.vercel.app/class2.html)
- [[raw/assignments/networking-tracker-README.md|Networking Tracker README]] — Deployment
