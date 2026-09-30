---
title: "Secrets and Environment Variables"
description: "Secrets and environment variables concern the practice of keeping sensitive information out of code, detailing which environment variables are public or server-only and the rationale behind this separation."
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

# Secrets and Environment Variables

Secrets and environment variables concern the practice of keeping sensitive information out of code, detailing which environment variables are public or server-only and the rationale behind this separation. This is important because hard-coding secrets or shipping them in frontend code allows attackers to compromise accounts or access data.

## Key details

- The safe pattern for local secrets is to store them in `.env.local` ([Class 2 slides (Software Systems), slide 45: Keep Secrets Out of Your Code](https://haas-ai-classes-fall-26.vercel.app/class2.html#/keep-secrets-out-of-your-code)).
- In production, secrets should use your cloud provider’s environment settings, and the backend should read secrets at runtime ([Class 2 slides (Software Systems), slide 45: Keep Secrets Out of Your Code](https://haas-ai-classes-fall-26.vercel.app/class2.html#/keep-secrets-out-of-your-code)).
- Never commit `.env` files or put secret keys in frontend code ([Class 2 slides (Software Systems), slide 45: Keep Secrets Out of Your Code](https://haas-ai-classes-fall-26.vercel.app/class2.html#/keep-secrets-out-of-your-code)).
- Environment variables like `NEXT_PUBLIC_NEON_AUTH_URL` and `NEXT_PUBLIC_NEON_DATA_API_URL` are public by design because they are addresses, not credentials ([[raw/assignments/networking-tracker-README.md#Environment variables|§ Environment variables]]).
- `NEON_AUTH_BASE_URL` and `NEON_AUTH_COOKIE_SECRET` are not exposed to the browser ([[raw/assignments/networking-tracker-README.md#Environment variables|§ Environment variables]]).
- `DATABASE_URL` is not exposed because it is a credential that names a role and password and would bypass the Data API entirely ([[raw/assignments/networking-tracker-README.md#Environment variables|§ Environment variables]]).
- `NEON_AUTH_COOKIE_SECRET` requires a minimum of 32 characters and should be generated with `openssl rand -hex 32` ([[raw/assignments/networking-tracker-README.md#Environment variables|§ Environment variables]]).

## Related notes

- [[Networking Tracker]] — its five environment variables
- [[Git and GitHub]] — never commit secrets
- [[Cloud Deployment]] — secrets are set per environment in Vercel

## Sources

- [[raw/course-slides/haas-class2.html|Class 2 slides (Software Systems)]] — Keep Secrets Out of Your Code · [public page](https://haas-ai-classes-fall-26.vercel.app/class2.html)
- [[raw/assignments/networking-tracker-README.md|Networking Tracker README]] — Environment variables
