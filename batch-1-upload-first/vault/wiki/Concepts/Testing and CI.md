---
title: "Testing and CI"
description: "Testing and CI in JD's work focuses on treating tests as executable promises, using CI/CD as a release gate, and employing strategies like regression tests and the test pyramid."
type: concept
sources:
  - "[[raw/course-slides/haas-class1.html]]"
  - "[[raw/course-slides/haas-class2.html]]"
  - "[[raw/assignments/networking-tracker-README.md]]"
source_ids:
  - class1-slides
  - class2-slides
  - networking-tracker-readme
source_sha256:
  - class1-slides@f4383cbe1ffe
  - class2-slides@00a0281db897
  - networking-tracker-readme@c218a4704709
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Testing and CI

Testing and CI in JD's work focuses on treating tests as executable promises, using CI/CD as a release gate, and employing strategies like regression tests and the test pyramid. This approach is demonstrated through specific test suites and validation contracts.

## Key details

- Tests turn examples into executable promises, such as writing an example as a test if a policy dictates a 15% strategic customer discount ([Class 1 slides (Code & Programming Foundations), slide 44: Tests Turn Examples into Executable Promises](https://haas-ai-classes-fall-26.vercel.app/class1.html#/tests-turn-examples-into-executable-promises)).
- Regression tests catch distant breakage by rerunning the full suite after every change, catching failures far from the modified code ([Class 2 slides (Software Systems), slide 44: Regression Tests Catch Distant Breakage](https://haas-ai-classes-fall-26.vercel.app/class2.html#/regression-tests-catch-distant-breakage)).
- The Test Pyramid suggests many fast unit tests for small decisions, fewer integration checks for system boundaries, and a few end-to-end checks for the user's real path ([Class 2 slides (Software Systems), slide 58: The Test Pyramid, in Plain English](https://haas-ai-classes-fall-26.vercel.app/class2.html#/the-test-pyramid-in-plain-english)).
- Unit tests run in milliseconds and pinpoint failures, while end-to-end tests take minutes and only indicate "something broke somewhere" ([Class 2 slides (Software Systems), slide 58: The Test Pyramid, in Plain English](https://haas-ai-classes-fall-26.vercel.app/class2.html#/the-test-pyramid-in-plain-english)).
- The `tests/validation.test.ts` file contains 25 tests verifying rules such as rejecting empty or whitespace-only names, trimming valid names, and rejecting invalid priority values like `urgent`, `HIGH`, `""`, `1`, `critical`, and a missing value ([[raw/assignments/networking-tracker-README.md#What the tests verify|§ What the tests verify]]).
- The `tests/api-contract.test.ts` file contains 5 tests asserting the order of operations for the `POST /api/contacts` handler, including checks for signed-out users, empty names, invalid priorities, and ensuring no `user_id` is sent upstream for a valid contact ([[raw/assignments/networking-tracker-README.md#What the tests verify|§ What the tests verify]]).
- The latest run of tests shows 30 tests passed in total, consisting of 25 from `tests/validation.test.ts` and 5 from `tests/api-contract.test.ts` ([[raw/assignments/networking-tracker-README.md#What the tests verify|§ What the tests verify]]).

## Related notes

- [[Networking Tracker]] — 25 validation + 5 route-contract tests
- [[Cloud Deployment]] — tests gate releases
- [[Clean Code]] — tests make changes safe

## Sources

- [[raw/course-slides/haas-class1.html|Class 1 slides (Code & Programming Foundations)]] — Tests Turn Examples into Executable Promises · [public page](https://haas-ai-classes-fall-26.vercel.app/class1.html)
- [[raw/course-slides/haas-class2.html|Class 2 slides (Software Systems)]] — Regression Tests Catch Distant Breakage, The Test Pyramid, in Plain English · [public page](https://haas-ai-classes-fall-26.vercel.app/class2.html)
- [[raw/assignments/networking-tracker-README.md|Networking Tracker README]] — What the tests verify
