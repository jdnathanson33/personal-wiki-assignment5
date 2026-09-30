---
title: "Networking Tracker"
description: "The Networking Tracker is a private contact tracker designed for users at Berkeley, allowing each signed-in user to maintain isolated contact lists with features for adding, editing, sorting, and filtering contacts."
type: project
sources:
  - "[[raw/assignments/networking-tracker-README.md]]"
  - "[[raw/course-slides/haas-class2.html]]"
source_ids:
  - networking-tracker-readme
  - class2-slides
source_sha256:
  - networking-tracker-readme@c218a4704709
  - class2-slides@00a0281db897
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Networking Tracker

The Networking Tracker is a private contact tracker designed for users at Berkeley, allowing each signed-in user to maintain isolated contact lists with features for adding, editing, sorting, and filtering contacts. It emphasizes security through Row Level Security within Postgres and uses a modern stack including Next.js 16, TypeScript, and Neon services.

## Key details

- User data isolation is achieved via Row Level Security inside Postgres, where the database filters rows based on the caller's identity extracted from a signed JWT, preventing users from seeing other users' data even if they bypass the application. ([[raw/assignments/networking-tracker-README.md#Berkeley Networking Tracker|§ Berkeley Networking Tracker]])
- Accounts are managed using Email + password sign-up, sign-in, and sign-out via Neon Managed Better Auth, with sessions held in an `HttpOnly`, signed cookie. ([[raw/assignments/networking-tracker-README.md#Features|§ Features]])
- Contacts can be added with fields for name, company, role, where met, notes, and priority, with priority constrained to `high`, `medium`, or `low` in three independent places. ([[raw/assignments/networking-tracker-README.md#Features|§ Features]])
- The technology stack includes Next.js 16 (App Router) and TypeScript for separating frontend and backend, Tailwind CSS v4 with Radix UI primitives for styling, and Zod for validation. ([[raw/assignments/networking-tracker-README.md#Technology stack and why|§ Technology stack and why]])
- Security relies on Row Level Security on the `contacts` table with four separate policies, ensuring `user_id` defaults to `auth.user_id()` and that `UPDATE` policies use `WITH CHECK` to prevent reassignment of rows. ([[raw/assignments/networking-tracker-README.md#Features|§ Features]])
- Testing involves `Vitest` to run the real route handler with the database mocked, verifying validation contracts (25 tests) and API contract order of operations (5 tests), which confirms that inserted rows do not contain a `user_id` from the client. ([[raw/assignments/networking-tracker-README.md#What the tests verify|§ What the tests verify]])
- The application is hosted on Vercel, which provides first-class Next.js support and a public HTTPS URL with zero configuration. ([[raw/assignments/networking-tracker-README.md#Technology stack and why|§ Technology stack and why]])

## Related notes

- [[Fundamentals of Agentic AI]] — course map
- [[Row Level Security]] — how the app isolates each user's rows
- [[Authentication and Sessions]] — how sign-in reaches the database
- [[Secrets and Environment Variables]] — which values stay server-only
- [[Testing and CI]] — the 30 automated tests
- [[Cloud Deployment]] — deployed on Vercel
- [[Class 2 - Software Systems]] — the class this assignment came from

## Sources

- [[raw/assignments/networking-tracker-README.md|Networking Tracker README]] — Berkeley Networking Tracker, Features, Technology stack and why, What the tests verify, Known limitations and what I would improve next
- [[raw/course-slides/haas-class2.html|Class 2 slides (Software Systems)]] — The Assignment · [public page](https://haas-ai-classes-fall-26.vercel.app/class2.html)
