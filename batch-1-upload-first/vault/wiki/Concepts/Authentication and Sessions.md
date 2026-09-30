---
title: "Authentication and Sessions"
description: "Authentication is crucial because without it, anyone can access any user's data, and it answers the question of whether a user is who they claim to be."
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

# Authentication and Sessions

Authentication is crucial because without it, anyone can access any user's data, and it answers the question of whether a user is who they claim to be. This process involves a specific flow where the browser signs in, a session cookie is set, and a JWT is used to verify identity with the database.

## Key details

- Without authentication, anyone can access anyone’s data, and the app has no idea who is making a request ([Class 2 slides (Software Systems), slide 37: Why Authentication Matters](https://haas-ai-classes-fall-26.vercel.app/class2.html#/why-authentication-matters)).
- Authentication answers the question: “Are you who you say you are?” ([Class 2 slides (Software Systems), slide 37: Why Authentication Matters](https://haas-ai-classes-fall-26.vercel.app/class2.html#/why-authentication-matters)).
- Building a prototype without authentication means every user can see every other user’s data, which is the #1 mistake in vibecoded apps ([Class 2 slides (Software Systems), slide 37: Why Authentication Matters](https://haas-ai-classes-fall-26.vercel.app/class2.html#/why-authentication-matters)).
- The user signs in by posting to `/api/auth/sign-in/email` on the app's own origin ([[raw/assignments/networking-tracker-README.md#How identity gets from the browser to Postgres|§ How identity gets from the browser to Postgres]]).
- This route proxies to Neon Managed Better Auth using the server-only cookie secret, setting an `HttpOnly`, `Secure`, signed session cookie that JavaScript cannot read ([[raw/assignments/networking-tracker-README.md#How identity gets from the browser to Postgres|§ How identity gets from the browser to Postgres]]).
- When the backend needs to query data, it exchanges the session for a short-lived JWT via `auth.token()` ([[raw/assignments/networking-tracker-README.md#How identity gets from the browser to Postgres|§ How identity gets from the browser to Postgres]]).
- The JWT travels to the Neon Data API as a `Bearer` token, and Neon verifies its signature against Neon Auth's JWKS rather than taking the app's word for who the user is ([[raw/assignments/networking-tracker-README.md#How identity gets from the browser to Postgres|§ How identity gets from the browser to Postgres]]).
- Inside Postgres, `auth.user_id()` returns the verified `sub` claim ([[raw/assignments/networking-tracker-README.md#How identity gets from the browser to Postgres|§ How identity gets from the browser to Postgres]]).
- The app never tells the database who the user is; it hands over a token the database checks for itself ([[raw/assignments/networking-tracker-README.md#How identity gets from the browser to Postgres|§ How identity gets from the browser to Postgres]]).

## Related notes

- [[Class 2 - Software Systems]] — taught here
- [[Row Level Security]] — the database uses the verified identity to filter rows
- [[Secrets and Environment Variables]] — the cookie secret must stay server-only
- [[Networking Tracker]] — implemented with Neon Managed Better Auth

## Sources

- [[raw/course-slides/haas-class2.html|Class 2 slides (Software Systems)]] — Why Authentication Matters, Ways to Prove Identity and Control Access · [public page](https://haas-ai-classes-fall-26.vercel.app/class2.html)
- [[raw/assignments/networking-tracker-README.md|Networking Tracker README]] — How identity gets from the browser to Postgres
