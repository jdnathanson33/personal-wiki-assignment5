> **Rehearsal run with internet ON** (model still local). Not the graded offline evidence; kept to show what changed.

# Ask-mode evidence card: T4

**Question:** What grade did I receive on the networking tracker assignment?

| Field | Value |
|---|---|
| Mode | ask (standalone; no chat history, no persona) |
| Execution | local |
| Model | `gemma4:e2b-it-qat` (4.6B, Q4_0, digest `07ea59a47401`) |
| Embedding model | `embeddinggemma` |
| Runtime | ollama 0.35.0 |
| Internet at run time | **ONLINE** |
| Timestamp | 2026-09-29T21:03:12 |

## Expected (written before running)

- Type: unanswerable (plausible but not in the wiki)
- Expected behavior: INSUFFICIENT EVIDENCE. No source states a grade; the README only has a 'Grading evidence' section, which is a tempting but wrong match.
- Expected source(s): —

## Retrieved passages (hybrid (bm25 + embeddinggemma, RRF), scope `raw`, top 8)

| Label | Source path | Location | BM25 | Cosine | Matched terms |
|---|---|---|---|---|---|
| S1 | `vault/raw/course-slides/haas-class2.html` | slide 46: The Assignment (part: Cloud Platforms) | 8.204 | 0.5019 | assignment, network, tracker |
| S2 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Grading evidence | 6.996 | 0.444 | network, tracker |
| S3 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Grading evidence > 1. Automated test output | 6.371 | 0.4519 | network, tracker |
| S4 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Grading evidence > Reproduce it yourself | 5.728 | 0.4582 | network, tracker |
| S5 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Table of contents | 6.022 | 0.3983 | network, tracker |
| S6 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Grading evidence > 7. Mobile layout | 6.315 | 0.3786 | network, tracker |
| S7 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Local setup | 6.134 | 0.3826 | network, tracker |
| S8 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Testing | 7.319 | 0.3482 | network, tracker |

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

<details><summary>S4 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Grading evidence > Reproduce it yourself</summary>

> The two seeded accounts below are disposable, exist only for grading, and hold nothing real:
> 
> | | Email | Password | Owns |
> | --- | --- | --- | --- |
> | **User A** | `alice.tester@example.com` | `AliceTest2026!` | contacts `1`–`5` |
> | **User B** | `bob.tester@example.com` | `BobTest2026!` | contact `7` |
> 
> Open the [live app](https://berkeley-networking-tracker-jd-mba.vercel.app) in two private browser windows, sign in as A in one and B in the other, and confirm neither can see the other's list. To repeat the direct-database attack from §6b, sign in as B, open the browser console, and run:
> 
> ```js
> const { token } = await (await fetch("/api/auth/token")).json();
> const DATA_API = "https://ep-sweet-butterfly-aronf3em.apirest.c-4.us-west-2.aws.neon.tech/neondb/rest/v1";
> await (await fetch(DATA_API + "/contacts?id=eq.1&select=*", {
>   headers: { Authorization: "Bearer " + token }
> })).json();   // → []  — contact 1 exists and belongs to A, but B cannot see it
> ```

</details>

<details><summary>S5 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Table of contents</summary>

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

<details><summary>S6 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Grading evidence > 7. Mobile layout</summary>

> ![Mobile layout](docs/screenshots/05-mobile.png)
> 
> Below the `md` breakpoint the table is replaced by cards, because a five-column table on a 390px screen is not usable. The dialog also becomes a bottom sheet with its own scroll region rather than a centred modal that overflows the viewport.

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

<details><summary>S8 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Testing</summary>

> ```bash
> npm test
> ```

</details>

## Actual Gemma answer

```text
INSUFFICIENT EVIDENCE: The provided passages do not state the grade received on the networking tracker assignment.
```

## Citations

- (none)

## Automatic citation check

- Verdict: **insufficient_evidence**

## Timing

26.43 s wall · model load 0.0 s · prompt 1493 tokens in 24.63 s · answer 22 tokens at 12.66 tokens/s

## Assessment (human, after opening the cited passages)

_Pending review._
