---
title: "APIs and HTTP"
description: "APIs function as agreements between systems, defining what callers can send and rely on receiving, while HTTP methods communicate the intent of those interactions."
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

# APIs and HTTP

APIs function as agreements between systems, defining what callers can send and rely on receiving, while HTTP methods communicate the intent of those interactions. This interaction is typically structured using JSON for data exchange and is governed by status codes that summarize the outcome of the request.

## Key details

- APIs are described using the Waiter Metaphor where the Waiter acts as the API, the kitchen is the backend, and the fridge is the database ([Class 2 slides (Software Systems), slide 18: APIs: The Waiter Metaphor](https://haas-ai-classes-fall-26.vercel.app/class2.html#/apis-the-waiter-metaphor)).
- An API serves as an Agreement Between Systems, specifying what callers can send and what they can rely on receiving, with version contracts deliberately used to prevent breaking consumers ([Class 2 slides (Software Systems), slide 19: An API is an Agreement Between Systems](https://haas-ai-classes-fall-26.vercel.app/class2.html#/an-api-is-an-agreement-between-systems)).
- HTTP methods communicate intent: GET is for reading data, POST is for creating data, PUT is for updating data, and DELETE is for removing data, with PATCH allowing changes to part of a resource ([Class 2 slides (Software Systems), slide 20: HTTP Methods](https://haas-ai-classes-fall-26.vercel.app/class2.html#/http-methods)).
- JSON (JavaScript Object Notation) is the language of APIs, providing a simple text format for sending data between machines ([Class 2 slides (Software Systems), slide 21: JSON — The Language of APIs](https://haas-ai-classes-fall-26.vercel.app/class2.html#/json-the-language-of-apis)).
- Never trust incoming API requests; the backend must validate types, ranges, permissions, and allowed fields because untrusted input could lead to privilege escalation or identity takeover ([Class 2 slides (Software Systems), slide 24: Never Trust Incoming API Requests](https://haas-ai-classes-fall-26.vercel.app/class2.html#/never-trust-incoming-api-requests)).
- Status codes are part of the contract, where 2xx indicates success, 4xx indicates the caller sent a bad request, and 5xx indicates the server failed ([Class 2 slides (Software Systems), slide 51: Status Codes Are Part of the Contract](https://haas-ai-classes-fall-26.vercel.app/class2.html#/status-codes-are-part-of-the-contract)).
- An HTTP Request is structured text containing the method, path, host, authorization, content type, and a body payload ([Class 2 slides (Software Systems), slide 52: Anatomy of an HTTP Request](https://haas-ai-classes-fall-26.vercel.app/class2.html#/anatomy-of-an-http-request)).
- The process of updating a contact's priority involves the browser sending a PATCH request, which is validated against schemas, and the database performing ownership checks before executing the update ([[raw/assignments/networking-tracker-README.md#Request flow, in words|§ Request flow, in words]]).

## Related notes

- [[Class 2 - Software Systems]] — taught here
- [[Networking Tracker]] — its /api routes follow this pattern
- [[Authentication and Sessions]] — requests carry the session
- [[Databases and SQL]] — the backend talks to the database

## Sources

- [[raw/course-slides/haas-class2.html|Class 2 slides (Software Systems)]] — APIs: The Waiter Metaphor, An API is an Agreement Between Systems, HTTP Methods, JSON — The Language of APIs, Never Trust Incoming API Requests, Status Codes Are Part of the Contract, Anatomy of an HTTP Request · [public page](https://haas-ai-classes-fall-26.vercel.app/class2.html)
- [[raw/assignments/networking-tracker-README.md|Networking Tracker README]] — Request flow, in words
