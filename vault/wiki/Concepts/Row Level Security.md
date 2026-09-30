---
title: "Row Level Security"
description: "Row Level Security (RLS) in the Networking Tracker isolates each user's rows by implementing four policies for select, insert, update, and delete operations."
type: concept
sources:
  - "[[raw/assignments/networking-tracker-README.md]]"
source_ids:
  - networking-tracker-readme
source_sha256:
  - networking-tracker-readme@c218a4704709
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Row Level Security

Row Level Security (RLS) in the Networking Tracker isolates each user's rows by implementing four policies for select, insert, update, and delete operations. This mechanism relies on the distinction between `USING` and `WITH CHECK` clauses to control row filtering and validation during data access.

## Key details

- The `user_id` column is defined with a `default (auth.user_id())` and `not null` constraint, meaning the application never sends `user_id` on insert, and unauthenticated callers cannot insert because `auth.user_id()` returns `NULL`. ([[raw/assignments/networking-tracker-README.md#Why `user_id` is defined the way it is|§ Why user_id is defined the way it is]])
- The four policies implemented are `contacts_select_own`, `contacts_insert_own`, `contacts_update_own`, and `contacts_delete_own`. ([[raw/assignments/networking-tracker-README.md#The four policies|§ The four policies]])
- The `USING` clause filters rows that already exist, determining which rows may be read, updated, or deleted. ([[raw/assignments/networking-tracker-README.md#The four policies|§ The four policies]])
- The `WITH CHECK` clause validates rows as they will be after a write operation to ensure the result still belongs to the user. ([[raw/assignments/networking-tracker-README.md#The four policies|§ The four policies]])
- `UPDATE` policies require both `USING` and `WITH CHECK` to prevent a user from changing a row so it belongs to someone else. ([[raw/assignments/networking-tracker-README.md#The four policies|§ The four policies]])
- `INSERT` policies only use `WITH CHECK` because there is no pre-existing row to filter. ([[raw/assignments/networking-tracker-README.md#The four policies|§ The four policies]])
- `SELECT` and `DELETE` policies only use `USING` because they do not produce a new row. ([[raw/assignments/networking-tracker-README.md#The four policies|§ The four policies]])
- `GRANT` determines if the `authenticated` role can issue the statement, while RLS decides which rows are returned. ([[raw/assignments/networking-tracker-README.md#The four policies|§ The four policies]])
- `FORCE ROW LEVEL SECURITY` is used to remove the default exemption where table owners bypass RLS, ensuring nothing runs unfiltered. ([[raw/assignments/networking-tracker-README.md#The four policies|§ The four policies]])

## Related notes

- [[Networking Tracker]] — where I applied it
- [[Authentication and Sessions]] — RLS depends on a verified JWT
- [[Databases and SQL]] — RLS is a Postgres feature

## Sources

- [[raw/assignments/networking-tracker-README.md|Networking Tracker README]] — Why user_id is defined the way it is, The four policies
