---
title: "Databases and SQL"
description: "Databases organize records by defining a place for every record, where a database acts as an organized warehouse, and tables store facts while relationships connect them."
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

# Databases and SQL

Databases organize records by defining a place for every record, where a database acts as an organized warehouse, and tables store facts while relationships connect them. SQL is the language used to query this data, and the structure of these databases is crucial for application memory and data modeling.

## Key details

- A database is conceptualized as an organized warehouse where every kind of record has a defined place and a reliable way to find it ([Class 2 slides (Software Systems), slide 26: A Database Organizes Records](https://haas-ai-classes-fall-26.vercel.app/class2.html#/a-database-organizes-records)).
- A table stores facts, and rows follow the same columns, while different entities reside in separate tables ([Class 2 slides (Software Systems), slide 27: Tables Store Facts. Relationships Connect Them.](https://haas-ai-classes-fall-26.vercel.app/class2.html#/tables-represent-entities)).
- Relationships connect rows through IDs, and together the tables and their links form the data model, which is a map for design before coding ([Class 2 slides (Software Systems), slide 27: Tables Store Facts. Relationships Connect Them.](https://haas-ai-classes-fall-26.vercel.app/class2.html#/tables-represent-entities)).
- SQL (Structured Query Language) is the method used to ask a database for data, allowing operations like selecting all users, filtering by role, counting users by role, and sorting by name ([Class 2 slides (Software Systems), slide 29: SQL — Talking to Databases](https://haas-ai-classes-fall-26.vercel.app/class2.html#/sql-talking-to-databases)).
- For large-data work, the data stack suggests pushing filtering, joining, sorting, and aggregating work down the stack to the database layer ([Class 2 slides (Software Systems), slide 30: Push Big Data Work Down the Stack](https://haas-ai-classes-fall-26.vercel.app/class2.html#/push-big-data-work-down-the-stack)).
- The `public.contacts` table in the Networking Tracker schema includes columns such as `id` (a primary key), `user_id` (a `text` column that is `not null` and defaults to `auth.user_id()`), `name`, `company`, `role`, `where_met`, `notes`, `priority`, `created_at`, and `updated_at` ([[raw/assignments/networking-tracker-README.md#`public.contacts`|§ public.contacts]]).
- The `user_id` column is defined as `not null` because an unauthenticated caller cannot insert a row, and it defaults to `auth.user_id()` to ensure every row has an owner ([[raw/assignments/networking-tracker-README.md#Why `user_id` is defined the way it is|§ Why user_id is defined the way it is]]).

## Related notes

- [[Class 2 - Software Systems]] — taught here
- [[Row Level Security]] — Postgres enforces row ownership
- [[Networking Tracker]] — uses Neon Postgres
- [[APIs and HTTP]] — the API sits in front of the database

## Sources

- [[raw/course-slides/haas-class2.html|Class 2 slides (Software Systems)]] — A Database Organizes Records, Tables Store Facts. Relationships Connect Them., Spotify Uses All Three Relationship Types, SQL — Talking to Databases, Push Big Data Work Down the Stack, Live App: Class 2 Signups, What Is a Tech Stack?, Three Practical Stack Recommendations · [public page](https://haas-ai-classes-fall-26.vercel.app/class2.html)
- [[raw/assignments/networking-tracker-README.md|Networking Tracker README]] — Database schema, public.contacts, Why user_id is defined the way it is
