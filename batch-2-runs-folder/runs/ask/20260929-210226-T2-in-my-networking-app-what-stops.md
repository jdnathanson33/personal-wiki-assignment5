> **Rehearsal run with internet ON** (model still local). Not the graded offline evidence; kept to show what changed.

# Ask-mode evidence card: T2

**Question:** In my networking app, what stops a signed-in user from handing one of their own contacts over to a different account?

| Field | Value |
|---|---|
| Mode | ask (standalone; no chat history, no persona) |
| Execution | local |
| Model | `gemma4:e2b-it-qat` (4.6B, Q4_0, digest `07ea59a47401`) |
| Embedding model | `embeddinggemma` |
| Runtime | ollama 0.35.0 |
| Internet at run time | **ONLINE** |
| Timestamp | 2026-09-29T21:01:31 |

## Expected (written before running)

- Type: reworded, one source
- Expected behavior: Explain that the UPDATE policy (contacts_update_own) has a WITH CHECK clause that evaluates the row after the update and rejects it if user_id no longer equals auth.user_id(). The question avoids the source's words (RLS, policy, WITH CHECK, reassign), so it tests retrieval on paraphrase.
- Expected source(s): `vault/raw/assignments/networking-tracker-README.md`
- Expected passage: “`with check` evaluates the post-update row”

## Retrieved passages (hybrid (bm25 + embeddinggemma, RRF), scope `raw`, top 8)

| Label | Source path | Location | BM25 | Cosine | Matched terms |
|---|---|---|---|---|---|
| S1 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Grading evidence > 6. Two-account privacy test | 19.501 | 0.4278 | account, contact, network, one, sign, user |
| S2 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Grading evidence > Reproduce it yourself | 19.632 | 0.4277 | account, app, contact, network, one, sign, user |
| S3 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Grading evidence > 3. Sign-in and sign-out | 17.01 | 0.4609 | app, contact, network, sign |
| S4 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Known limitations and what I would improve next | 19.686 | 0.3771 | account, app, contact, hand, network, one, stop, user |
| S5 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Architecture > Request flow, in words | 17.192 | 0.3786 | contact, network, one, sign, stop, user |
| S6 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Authentication and RLS ownership > The four policies | 20.202 | 0.343 | contact, different, hand, network, one, sign, stop, user |
| S7 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker | 16.45 | 0.4158 | app, contact, network, sign, user |

<details><summary>S1 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Grading evidence > 6. Two-account privacy test</summary>

> Two accounts on the production deployment:
> 
> | Account | Email | Owns |
> | --- | --- | --- |
> | **User A** | `alice.tester@example.com` | contacts `1`–`5` |
> | **User B** | `bob.tester@example.com` | contact `7` |
> 
> **6a. Through the application API, signed in as User B:**
> 
> ```console
> GET    /api/contacts             → 200  {"contacts":[]}          A's five rows are invisible
> GET    /api/contacts?sort=name   → 200  {"contacts":[]}          no ordering trick reveals them
> PATCH  /api/contacts/1           → 404  "That contact doesn't exist, or isn't yours."
> DELETE /api/contacts/1           → 404  "That contact doesn't exist, or isn't yours."
> PATCH  /api/contacts/1  {"user_id":"bob"}
>                                  → 400  field not accepted by the update schema
> POST   /api/contacts             → 201  B's own row, stamped with B's user_id
> GET    /api/contacts             → 200  exactly one row: B's own
> ```
> 
> **6b. Bypassing the application entirely.** This is the test that matters, because the Data API URL is public and a determined user can call it straight from the browser console. Here is User B's own JWT, sent directly to Neon with no application code in the request path:

</details>

<details><summary>S2 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Grading evidence > Reproduce it yourself</summary>

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

<details><summary>S3 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Grading evidence > 3. Sign-in and sign-out</summary>

> ![Sign in](docs/screenshots/01-sign-in.png)
> 
> Signed out, the app never renders contact UI at all. `app/page.tsx` is a Server Component that calls `getSessionUser()` and redirects before returning markup, and the API refuses independently:
> 
> ```console
> POST /api/auth/sign-out          → 200  {"success":true}
> GET  /api/contacts  (no session) → 401  {"error":"You need to be signed in."}
> ```

</details>

<details><summary>S4 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Known limitations and what I would improve next</summary>

> …at runtime.** It exists for applying the schema. Keeping an unused credential in the template is a small smell.
> 
> **What I would do next, in order**
> 
> 1. **A Playwright end-to-end test for the two-account privacy case**, run in CI. Right now the most important security property is verified by hand, which means it can silently regress. This is the highest-value gap.
> 2. **Turn on email verification**, and add password reset.
> 3. **Pagination plus a proper full-text search index**, so the app degrades gracefully as a network grows.
> 4. **Optimistic updates with rollback on failure**, so the list feels instant.
> 5. **A "last contacted" date and a follow-up reminder**, which is the feature that would actually change behaviour — a tracker you don't get nudged by is a tracker you stop opening.
> 6. **A `contact_interactions` child table** so you can log each conversation rather than appending to one notes field. It would carry the same four RLS policies, keyed off the parent's `user_id`.

</details>

<details><summary>S5 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Architecture > Request flow, in words</summary>

> Take "JD edits a contact's priority to `low`."
> 
> 1. The browser sends `PATCH /api/contacts/42` with `{"priority":"low"}` and the session cookie.
> 2. The route handler calls `getSessionUser()`. The cookie is signed with a server-only secret; a forged one fails verification and the request stops at `401`.
> 3. The payload goes through `contactUpdateSchema`. `"low"` is in the enum, so it passes. `"urgent"` would stop here at `400` with the message *"Priority must be one of: high, medium, low."*
> 4. The handler calls `auth.token()` to get JD's JWT, then issues `UPDATE contacts SET priority='low' WHERE id=42` through the Data API with that token attached.
> 5. Postgres verifies the token, resolves `auth.user_id()` to JD's user id, and — because of the `contacts_update_own` policy — actually runs `... WHERE id=42 AND user_id = auth.user_id()`.
> 6. If row 42 belongs to somebody else, zero rows match. The handler sees an empty result and returns `404`. **No code checked ownership. The database did.**
> 
> ---

</details>

<details><summary>S6 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Authentication and RLS ownership > The four policies</summary>

> …exist**: which rows may I read, update, or delete?
> - `WITH CHECK` validates **rows as they will be after the write**: is the result still mine?
> 
> `UPDATE` needs both, and this is the subtle one. `USING` alone would stop you editing someone else's contact, but would happily let you take your *own* contact and set `user_id` to another person's id — handing them a row, or planting one in their list. `WITH CHECK` evaluates the post-update row and rejects it, because after that change `auth.user_id() = user_id` is false. That is exactly the requirement *"update policies prevent a user from changing a row so it belongs to someone else."*
> 
> `INSERT` has only `WITH CHECK` because there is no pre-existing row to filter. `SELECT` and `DELETE` have only `USING` because they do not produce a new row.
> 
> **Grants and RLS are two different gates, and you need both.** `GRANT` decides whether the `authenticated` role may issue the statement at all; RLS decides which rows come back. The schema grants `select, insert, update, delete` on `contacts` to `authenticated` and revokes everything from `anonymous`, so a signed-out caller is refused before RLS is even consulted.

</details>

<details><summary>S7 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker</summary>

> A private contact tracker for the people you want to stay connected with at Berkeley. Each signed-in user gets their own list — add someone with their company, role, where you met, free-form notes, and a high/medium/low priority, then sort and filter to find them again. The interesting part is not the CRUD; it's that a user's rows are isolated from every other user's by **Row Level Security inside Postgres itself**, not by a `WHERE` clause in application code. The database extracts the caller's identity from a signed JWT and filters rows before any query returns, so even a caller who bypasses this app entirely and hits the public Data API directly can only ever see their own data.
> 
> **Live app: https://berkeley-networking-tracker-jd-mba.vercel.app**
> 
> ---

</details>

## Actual Gemma answer

```text
A signed-in user is stopped from handing a contact over to a different account because of Row Level Security (RLS) inside Postgres itself [S7]. The database extracts the caller's identity from a signed JWT and filters rows before any query returns, ensuring a caller can only see their own data even if they bypass the application entirely [S7]. Furthermore, the `UPDATE` policy requires both `USING` and `WITH CHECK` to prevent a user from changing a row so it belongs to someone else [S6].
```

## Citations

- [S6] → `vault/raw/assignments/networking-tracker-README.md` — Berkeley Networking Tracker > Authentication and RLS ownership > The four policies
- [S7] → `vault/raw/assignments/networking-tracker-README.md` — Berkeley Networking Tracker

## Automatic citation check

- Verdict: **citations_check_passed**
- “A signed-in user is stopped from handing a contact over to a different account because of Row Level Security (RLS) inside Postgres itself [S” → ['S7'], word overlap 0.6
- “The database extracts the caller's identity from a signed JWT and filters rows before any query returns, ensuring a caller can only see thei” → ['S7'], word overlap 0.89
- “Furthermore, the `UPDATE` policy requires both `USING` and `WITH CHECK` to prevent a user from changing a row so it belongs to someone else ” → ['S6'], word overlap 0.83

## Timing

54.27 s wall · model load 0.0 s · prompt 2287 tokens in 44.85 s · answer 108 tokens at 11.6 tokens/s

## Assessment (human, after opening the cited passages)

_Pending review._
