# Ask-mode evidence card (OFFLINE run): T4

**Question:** What grade did I receive on the networking tracker assignment?

| Field | Value |
|---|---|
| Mode | ask (standalone; no chat history, no persona) |
| Execution | local |
| Model | `gemma4:e2b-it-qat` (4.6B, Q4_0, digest `07ea59a47401`) |
| Embedding model | `embeddinggemma` |
| Runtime | ollama 0.35.0 |
| Internet at run time | **offline** |
| Timestamp | 2026-09-29T21:29:52 |

## Expected (written before running)

- Type: unanswerable (plausible but not in the wiki)
- Expected behavior: INSUFFICIENT EVIDENCE. No source states a grade; the README only has a 'Grading evidence' section, which is a tempting but wrong match.
- Expected source(s): —

## Retrieved passages (hybrid (bm25 + embeddinggemma, RRF), scope `raw`, top 10)

| Label | Source path | Location | BM25 | Cosine | Matched terms |
|---|---|---|---|---|---|
| S1 | `vault/raw/course-slides/haas-class2.html` | slide 46: The Assignment (part: Cloud Platforms) | 9.036 | 0.5019 | assignment, network, tracker |
| S2 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Grading evidence | 7.454 | 0.444 | network, tracker |
| S3 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Grading evidence > 1. Automated test output | 6.741 | 0.4519 | network, tracker |
| S4 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Table of contents | 7.044 | 0.39 | network, tracker |
| S5 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Screenshots | 12.411 | 0.3402 | network, receive, tracker |
| S6 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Testing | 7.826 | 0.3482 | network, tracker |
| S7 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Local setup | 6.418 | 0.377 | network, tracker |
| S8 | `vault/raw/course-slides/haas-class2.html` | slide 6: Today’s Agenda (part: From a Program to a Product) | 6.181 | 0.3366 | assignment, network, tracker |
| S9 | `vault/raw/course-slides/haas-class4.html` | slide 75: Submit One Repository with Visible Evidence (part: Transformers) | 4.865 | 0.3259 | assignment, network |
| S10 | `vault/raw/assignments/pacman-dqn-README.md` | Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI) | 5.46 | 0.2692 | assignment, network |

<details><summary>S1 — vault/raw/course-slides/haas-class2.html — slide 46: The Assignment (part: Cloud Platforms)</summary>

> The Assignment
> 
> Important
> 
> Build a networking tracker: a website to record the people you need to network with at Berkeley.
> 
> - Sign in before using the app
> 
> - Add, view, edit, and delete your own contacts
> 
> - Keep every user’s contacts private from every other user
> 
> - Validate inputs and include at least one automated test
> 
> - Deployed live on the internet
> 
> - Submit one public GitHub repository URL with all grading evidence in its README
> 
> Stack: Next.js + Supabase + Vercel
> 
> Full assignment guide
> 
> Open Google Doc ↗
> 
> README, setup, authentication, RLS, testing, deployment, and submission evidence.

</details>

<details><summary>S2 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Grading evidence</summary>

> Every artifact below was captured against the **deployed production application**, not a local dev server.

</details>

<details><summary>S3 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Grading evidence > 1. Automated test output</summary>

> …contact and does not send user_id upstream
> 
>  ✓ tests/api-contract.test.ts > POST /api/contacts > ignores a user_id a malicious client tries to inject
> 
> Test Files  2 passed (2)
>       Tests  30 passed (30)
> ```

</details>

<details><summary>S4 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Table of contents</summary>

> - [Screenshots](#screenshots)
> - [Features](#features)
> - [Technology stack and why](#technology-stack-and-why)
> - [Architecture](#architecture)
> - [Local setup](#local-setup)
> - [Environment variables](#environment-variables)
> - [Database schema](#database-schema)
> - [Authentication and RLS ownership](#authentication-and-rls-ownership)
> - [Testing](#testing)
> - [Deployment](#deployment)
> - [Grading evidence](#grading-evidence)
> - [Known limitations and what I would improve next](#known-limitations-and-what-i-would-improve-next)
> 
> ---

</details>

<details><summary>S5 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Screenshots</summary>

> | | |
> |---|---|
> | **Sign in** — signed-out visitors never receive contact UI | **Your contacts** — sortable, filterable, searchable |
> | ![Sign in](docs/screenshots/01-sign-in.png) | ![Contact list](docs/screenshots/02-contacts-list.png) |
> | **Add a contact** — one dialog for create and edit | **Invalid input** — the server rejected it, and said why |
> | ![Add a contact](docs/screenshots/03-add-contact.png) | ![Validation error](docs/screenshots/04-validation-error.png) |
> 
> **On a phone**, the table becomes cards:
> 
> <img src="docs/screenshots/05-mobile.png" alt="Mobile card layout" width="320">
> 
> ---

</details>

<details><summary>S6 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Testing</summary>

> ```bash
> npm test
> ```

</details>

<details><summary>S7 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Local setup</summary>

> Requires Node.js 20 or newer.
> 
> ```bash
> git clone https://github.com/jdnathanson33/berkeley-networking-tracker.git
> cd berkeley-networking-tracker
> npm install
> 
> cp .env.example .env.local
> # Fill in .env.local with values from the Neon Console (see below)
> 
> npm run dev
> ```
> 
> Open <http://localhost:3000>. You will land on the sign-in page; create an account to get in.
> 
> Before the app will work against a fresh Neon project, apply the schema once:
> 
> 1. Neon Console → your project → **SQL Editor**
> 2. Paste the contents of [`db/schema.sql`](db/schema.sql) and run it
> 
> Other commands:
> 
> ```bash
> npm test          # run the automated tests once
> npm run test:watch # re-run on change
> npm run build     # production build
> npm run lint      # ESLint
> ```
> 
> ---

</details>

<details><summary>S8 — vault/raw/course-slides/haas-class2.html — slide 6: Today’s Agenda (part: From a Program to a Product)</summary>

> Today’s Agenda
> 
> - Frontend — HTML, CSS, JavaScript (live, editable, in this deck)
> 
> - Backend — servers, APIs, and the waiter metaphor
> 
> - Databases — durable shared memory, plus live SQL
> 
> - Secrets & identity — API keys, env vars, authentication
> 
> - The cloud — someone else’s computers
> 
> - Testing & deployment — from your laptop to a live URL
> 
> - Tech stacks — how the pieces get chosen
> 
> - Assignment 1 — build and deploy a networking tracker
> 
> Note
> 
> A note on pacing. Slides badged SELF-STUDY are real material, not filler — they’re the operational depth you’ll want when you actually build this. We may skip them live to protect time for the hands-on parts. They stay in the published deck; read them when the question comes up at work.

</details>

<details><summary>S9 — vault/raw/course-slides/haas-class4.html — slide 75: Submit One Repository with Visible Evidence (part: Transformers)</summary>

> …time. Explain what you expected versus what happened. Check that the notebook, plots, samples, and evidence links are visible when signed out.
> 
> A proposed next experiment is enough for the core assignment. Optional self-study: change one variable and compare, inspect another token or attention row, or follow https://github.com/karpathy/ng-video-lecture. Writing the network yourself is optional.

</details>

<details><summary>S10 — vault/raw/assignments/pacman-dqn-README.md — Ms. Pac-Man DQN — Assignment 2 (Fundamentals of Agentic AI)</summary>

> I trained the course's Deep Q-Network (DQN) on Atari Ms. Pac-Man. I changed only three settings: exploration, episodes, and learning rate. The untrained and trained agents were scored on the same five evaluation games.
> 
> **Result:** the mean evaluation score went from **492.0 → 604.0 (+112.0)**. Most of that gain comes from one strong game (1,420); three of the five games scored lower after training. So this run shows limited learning, not a clear improvement.

</details>

## Actual Gemma answer

```text
INSUFFICIENT EVIDENCE: The provided passages do not state the grade received for the networking tracker assignment.
```

## Citations

- (none)

## Automatic citation check

- Verdict: **insufficient_evidence**

## Timing

28.51 s wall · model load 0.0 s · prompt 1748 tokens in 26.9 s · answer 22 tokens at 14.14 tokens/s

## Assessment (human, after opening the cited passages)

**PASS.** No source states a grade. Retrieval surfaced the tempting “Grading evidence” sections of the networking README and the Class 2 assignment slide, and Gemma still answered exactly `INSUFFICIENT EVIDENCE: …` with no guess. Expected behavior met.

_Reviewed by JD + Claude after opening each cited passage in `vault/raw/`._
