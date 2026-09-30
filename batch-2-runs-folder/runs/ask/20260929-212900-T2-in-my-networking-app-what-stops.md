# Ask-mode evidence card (OFFLINE run): T2

**Question:** In my networking app, what stops a signed-in user from handing one of their own contacts over to a different account?

| Field | Value |
|---|---|
| Mode | ask (standalone; no chat history, no persona) |
| Execution | local |
| Model | `gemma4:e2b-it-qat` (4.6B, Q4_0, digest `07ea59a47401`) |
| Embedding model | `embeddinggemma` |
| Runtime | ollama 0.35.0 |
| Internet at run time | **offline** |
| Timestamp | 2026-09-29T21:28:06 |

## Expected (written before running)

- Type: reworded, one source
- Expected behavior: Explain that the UPDATE policy (contacts_update_own) has a WITH CHECK clause that evaluates the row after the update and rejects it if user_id no longer equals auth.user_id(). The question avoids the source's words (RLS, policy, WITH CHECK, reassign), so it tests retrieval on paraphrase.
- Expected source(s): `vault/raw/assignments/networking-tracker-README.md`
- Expected passage: “`with check` evaluates the post-update row”

## Retrieved passages (hybrid (bm25 + embeddinggemma, RRF), scope `raw`, top 10)

| Label | Source path | Location | BM25 | Cosine | Matched terms |
|---|---|---|---|---|---|
| S1 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Grading evidence > Reproduce it yourself | 20.025 | 0.4299 | account, app, contact, network, one, sign, user |
| S2 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Grading evidence > 6. Two-account privacy test | 19.133 | 0.4278 | account, contact, network, one, sign, user |
| S3 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Grading evidence > 3. Sign-in and sign-out | 17.051 | 0.4472 | app, contact, network, sign |
| S4 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Known limitations and what I would improve next | 19.043 | 0.3771 | account, app, contact, hand, network, one, stop, user |
| S5 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker | 16.199 | 0.4232 | app, contact, network, sign, user |
| S6 | `vault/raw/assignments/networking-tracker-README.md` | Berkeley Networking Tracker > Authentication and RLS ownership > The four policies | 19.557 | 0.343 | contact, different, hand, network, one, sign, stop, user |
| S7 | `vault/raw/course-slides/haas-class2.html` | slide 46: The Assignment (part: Cloud Platforms) | 16.399 | 0.2655 | app, contact, network, one, sign, user |
| S8 | `vault/raw/course-slides/haas-class2.html` | slide 37: Why Authentication Matters (part: Authentication) | 8.173 | 0.2932 | app, one, user |
| S9 | `vault/raw/course-slides/haas-class1.html` | slide 101: Ports: Apartment Numbers for One Address (part: Localhost: Running Software on Your Own Machine) | 7.886 | 0.2572 | different, one, stop |
| S10 | `vault/raw/course-slides/haas-class2.html` | slide 47: Definition of Done: Your Rubric (part: Cloud Platforms) | 16.573 | 0.1645 | account, app, contact, one, sign, user |

<details><summary>S1 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Grading evidence > Reproduce it yourself</summary>

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

<details><summary>S2 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker > Grading evidence > 6. Two-account privacy test</summary>

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

<details><summary>S5 — vault/raw/assignments/networking-tracker-README.md — Berkeley Networking Tracker</summary>

> A private contact tracker for the people you want to stay connected with at Berkeley. Each signed-in user gets their own list — add someone with their company, role, where you met, free-form notes, and a high/medium/low priority, then sort and filter to find them again. The interesting part is not the CRUD; it's that a user's rows are isolated from every other user's by **Row Level Security inside Postgres itself**, not by a `WHERE` clause in application code. The database extracts the caller's identity from a signed JWT and filters rows before any query returns, so even a caller who bypasses this app entirely and hits the public Data API directly can only ever see their own data.
> 
> **Live app: https://berkeley-networking-tracker-jd-mba.vercel.app**
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

<details><summary>S7 — vault/raw/course-slides/haas-class2.html — slide 46: The Assignment (part: Cloud Platforms)</summary>

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

<details><summary>S8 — vault/raw/course-slides/haas-class2.html — slide 37: Why Authentication Matters (part: Authentication)</summary>

> Why Authentication Matters
> 
> Without authentication, anyone can access anyone’s data. Your app has no idea who is making a request.
> 
> Authentication answers one question: “Are you who you say you are?”
> 
> Important
> 
> If you build a prototype with no auth, every user can see every other user’s data. This is the #1 mistake in vibecoded apps.

</details>

<details><summary>S9 — vault/raw/course-slides/haas-class1.html — slide 101: Ports: Apartment Numbers for One Address (part: Localhost: Running Software on Your Own Machine)</summary>

> Ports: Apartment Numbers for One Address
> 
> One computer runs many programs at once. The port says which one you are talking to.
> 
> Address
> 
> Who usually lives there
> 
> localhost:8000
> 
> Python’s built-in web server
> 
> localhost:3000
> 
> A Node / React / Next.js dev server
> 
> localhost:5432
> 
> A PostgreSQL database
> 
> localhost:11434
> 
> Ollama, running an LLM on your own machine
> 
> The address is the building; the port is the apartment. Address already in use means someone is already home — use a different port, or stop the program that’s squatting there.

</details>

<details><summary>S10 — vault/raw/course-slides/haas-class2.html — slide 47: Definition of Done: Your Rubric (part: Cloud Platforms)</summary>

> Definition of Done: Your Rubric
> 
> Submit one public GitHub repository URL. Put the live URL and every evidence item below in its README.
> 
> Check
> 
> Evidence
> 
> The app is live on a public URL
> 
> README: live URL
> 
> A user can sign in and sign out
> 
> README: screenshot or recording
> 
> You can add, view, edit, delete a contact and it survives refresh
> 
> README: screenshot or recording
> 
> User A cannot see or change User B’s contacts
> 
> README: two-account test evidence
> 
> One invalid input fails safely (empty name, bad priority)
> 
> README: error screenshot
> 
> At least one automated test passes
> 
> README: test output
> 
> Secret keys are in server-only environment settings, not frontend code
> 
> README: publishable versus secret-key explanation
> 
> You can explain the schema and RLS ownership rule
> 
> README: schema and user_id ownership rule
> 
> Tip
> 
> The security, test, and explanation rows are the difference between “an AI built me a demo” and “I shipped software I understand.”

</details>

## Actual Gemma answer

```text
A user's rows are isolated from every other user's by Row Level Security inside Postgres itself, not by a `WHERE` clause in application code [S5]. The database extracts the caller's identity from a signed JWT and filters rows before any query returns, so even a caller who bypasses the app entirely and hits the public Data API directly can only ever see their own data [S5]. Furthermore, the `UPDATE` policy requires both `USING` and `WITH CHECK` to prevent a user from changing a row so it belongs to someone else, as `USING` alone would allow taking one's own contact and setting the `user_id` to another person's ID [S6].
```

## Citations

- [S5] → `vault/raw/assignments/networking-tracker-README.md` — Berkeley Networking Tracker
- [S6] → `vault/raw/assignments/networking-tracker-README.md` — Berkeley Networking Tracker > Authentication and RLS ownership > The four policies

## Automatic citation check

- Verdict: **citations_check_passed**
- “A user's rows are isolated from every other user's by Row Level Security inside Postgres itself, not by a `WHERE` clause in application code” → ['S5'], word overlap 1.0
- “The database extracts the caller's identity from a signed JWT and filters rows before any query returns, so even a caller who bypasses the a” → ['S5'], word overlap 1.0
- “Furthermore, the `UPDATE` policy requires both `USING` and `WITH CHECK` to prevent a user from changing a row so it belongs to someone else,” → ['S6'], word overlap 0.71

## Timing

53.68 s wall · model load 0.0 s · prompt 2695 tokens in 42.27 s · answer 147 tokens at 12.98 tokens/s

## Assessment (human, after opening the cited passages)

**PASS, with a retrieval weakness.** The question avoids the source's words. Keyword and embedding search still put the right section (§ The four policies) at **rank 6 of 10**, behind five less-relevant networking-README sections, including three “Grading evidence” passages. The answer's first two sentences are correct and come from the README intro (S5). The key claim is the third sentence: the `UPDATE` policy needs both `USING` and `WITH CHECK`, and `USING` alone would let a user set `user_id` to someone else's id. I checked it against S6, and it paraphrases that section correctly. The answer does not name the policy (`contacts_update_own`) or say that `WITH CHECK` evaluates the post-update row, so it is less precise than my expected answer. In the first rehearsal (top-8 with a 4-per-file cap) this passage was cut from the context. Raising top-k to 10 with a cap of 6 fixed that (see runs/eval retrieval checks).

_Reviewed by JD + Claude after opening each cited passage in `vault/raw/`._
