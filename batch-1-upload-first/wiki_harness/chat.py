"""`wiki chat`: the personal assistant ("Margin").

What the harness does on every turn:
  1. Handle slash commands (/notes, /nonotes, /search, /save, /clear, /history, /help, /exit).
  2. Decide whether this turn needs JD's notes (decide_retrieval). Capability
     questions, greetings, and follow-ups like "make that shorter" do NOT trigger
     a lookup; questions about the course or his projects do.
  3. Build the prompt: persona.md (voice + real capabilities) as the system
     message, the recent conversation (trimmed to a turn and character budget),
     and - only if retrieval ran - the numbered note passages [N1..].
  4. Stream the local Gemma reply, check [N#] labels, and append the turn to
     the saved transcript in runs/chat/.
Chat history is conversation context, never evidence: `wiki ask` does not read it.
"""
from __future__ import annotations

import re
import sys
from typing import Callable, List, Optional

from . import citations, records
from .config import Settings, read_instruction
from .ollama_client import ModelUnavailable, OllamaClient
from .retrieval import Index

META = re.compile(r"\b(what can (you|we|i)\b|what do you do|help me with|who are you|what are you|your (commands|capabilities)"
                  r"|how do (i|you) use (you|this)|what are your)", re.I)
GREETING = re.compile(r"^\s*(hi|hello|hey|thanks|thank you|ok|okay|cool|great|good morning|bye)\b[\s!.?]*$", re.I)
FOLLOW_UP = re.compile(r"^\s*(make (it|that|this)|turn (it|that|this)|now |again|shorter|longer|shorten|condense|"
                       r"simplify|rephrase|reword|rewrite (it|that|this)|expand (on )?(it|that|this)|more (formal|casual|concise)|"
                       r"less |add |remove |cut )|\b(make|turn) (that|it|this) (shorter|longer|into)", re.I)
NOTE_HINT = re.compile(r"\b(my|our|i|me)\b.*\b(notes?|wiki|assignments?|projects?|runs?|results?|tracker|agent|model)\b|"
                       r"\b(class ?[1-7]|slides?|lecture|course|assignment ?\d|syllabus|networking tracker|pac-?man|dqn|"
                       r"nanogpt|rls|row level security|neon|vercel|reward|epsilon|embedding|tokeni[sz]|temperature|"
                       r"rag|retrieval|gemma|prompting|transformer|attention|loss)\b", re.I)
QUESTION = re.compile(r"^\s*(what|how|why|when|which|who|where|did|does|do|is|are|was|were|explain|summari[sz]e|"
                      r"remind|compare|tell me|list|describe|quiz)\b", re.I)

HELP = """chat commands:
  /notes <question>  force a notes lookup for this message
  /nonotes           turn automatic notes lookups off (again to turn on)
  /search <words>    show matching original passages (no generation)
  /save              save the last reply to outputs/drafts/ (kept separate from sources)
  /history           show what the assistant currently remembers of this chat
  /clear             forget this conversation
  /help, /exit"""


def decide_retrieval(text: str, idx: Optional[Index], has_history: bool) -> (bool, str):
    """Return (retrieve?, reason). Rules first, then a keyword-strength check."""
    if GREETING.match(text):
        return False, "greeting/small talk"
    if META.search(text):
        return False, "question about the assistant itself"
    if has_history and FOLLOW_UP.search(text):
        return False, "follow-up on the conversation"
    hinted = bool(NOTE_HINT.search(text))
    if idx is None:
        return False, "no index"
    res = idx.search(text, k=1, scope="all", client=None)
    top = res["results"][0] if res["results"] else None
    strength = top["bm25"] if top else 0.0
    terms = len(top["matched_terms"]) if top else 0
    if hinted and strength >= 3.0:
        return True, f"mentions course/project topics (keyword score {strength})"
    if QUESTION.search(text) and strength >= 7.0 and terms >= 2:
        return True, f"factual question with a strong match in notes (keyword score {strength})"
    return False, f"general conversation (best keyword score {strength})"


class ChatSession:
    def __init__(self, settings: Settings, client: OllamaClient, out: Callable = print):
        self.s, self.client, self.out = settings, client, out
        self.persona = read_instruction(settings, "persona.md")
        self.history: List[dict] = []          # only user/assistant text
        self.notes_enabled = True
        self.last_passages: List[dict] = []    # passages used by the last notes turn
        self.ctx = records.run_context(settings, client, "chat")
        self.turns: List[dict] = []
        self.name = records.stamp() + "-chat"
        try:
            self.idx = Index.load(settings.chunks_file, settings.embeddings_file)
        except FileNotFoundError:
            self.idx = None

    # ---- prompt assembly
    def _trimmed_history(self) -> List[dict]:
        h = self.history[-2 * self.s.chat_history_turns:]
        while h and sum(len(m["content"]) for m in h) > self.s.chat_history_chars:
            h = h[2:]
        return h

    def _retrieve(self, text: str) -> List[dict]:
        res = self.idx.search(text, k=4, scope="all", client=self.client)
        picked, used = [], 0
        for r in res["results"]:
            if used + len(r["passage"].text) > 4000 and picked:
                break
            picked.append(r)
            used += len(r["passage"].text)
        return [{"label": f"N{i}", "path": r["passage"].path, "locator": r["passage"].locator,
                 "kind": r["passage"].kind, "text": r["passage"].text} for i, r in enumerate(picked, 1)]

    def turn(self, text: str, force_notes: bool = False) -> dict:
        has_hist = bool(self.history)
        if force_notes:
            retrieve, reason = (self.idx is not None), "forced with /notes"
        elif not self.notes_enabled:
            retrieve, reason = False, "notes lookups turned off (/nonotes)"
        else:
            retrieve, reason = decide_retrieval(text, self.idx, has_hist)

        passages: List[dict] = []
        follow_up = has_hist and not retrieve and bool(FOLLOW_UP.search(text))
        if retrieve:
            passages = self._retrieve(text)
            self.last_passages = passages
        self.out(f"  (harness: {'notes lookup' if retrieve else 'no lookup'} — {reason})")
        for p in passages if retrieve else []:
            self.out(f"  [{p['label']}] {p['path']} — {p['locator']}")

        if passages:
            block = "\n\n".join(f"[{p['label']}] ({p['path']} — {p['locator']})\n{p['text']}" for p in passages)
            user = (f"(Harness: passages from JD's notes, retrieved for this message. Use them only if relevant, cite "
                    f"them as [N1], [N2] ..., and point out politely if they contradict what JD says.)\n\n"
                    f"{block}\n\nJD's message: {text}")
        elif follow_up:
            # Rework the previous reply, not the notes; earlier [N#] labels stay valid because
            # the previous reply (with its citations) is in the conversation history.
            user = (f"{text}\n\n(Harness: this is a follow-up. Apply it to your previous reply above and keep any "
                    f"[N#] citations that still apply.)")
        else:
            user = text
        messages = [{"role": "system", "content": self.persona}] + self._trimmed_history() + [{"role": "user", "content": user}]
        self.out("Margin: ", end="")
        res = self.client.chat(messages, temperature=self.s.temperature["chat"],
                               on_token=lambda t: (sys.stdout.write(t), sys.stdout.flush()), max_tokens=600)
        self.out("")
        reply = res["text"]
        chk = citations.check(reply, {p["label"]: p["text"] for p in passages}, prefix="N") if passages else None
        if chk and chk["invalid_labels"]:
            self.out(f"  (harness: warning — cited notes that were not shown: {', '.join(chk['invalid_labels'])})")
        if not passages and not follow_up and re.search(r"\[N\d+\]", reply):
            self.out("  (harness: warning — reply contains [N#] labels but no notes were shown this turn)")
        self.out(f"  ({res['stats']['wall_seconds']}s, {res['stats']['output_tokens']} tokens)")

        self.history += [{"role": "user", "content": text}, {"role": "assistant", "content": reply}]
        rec = {"user": text, "retrieved": retrieve, "retrieval_reason": reason,
               "passages": [{k: p[k] for k in ("label", "path", "locator", "kind")} for p in passages],
               "history_messages_sent": len(messages) - 2, "reply": reply,
               "citation_check": chk, "stats": res["stats"]}
        self.turns.append(rec)
        self.save()
        return rec

    # ---- persistence
    def save(self):
        md = [f"# Chat transcript ({self.ctx['timestamp']})", "",
              f"Mode: chat · Execution: {self.ctx['execution']} · Model: `{self.ctx['model']}` · "
              f"Runtime: {self.ctx.get('runtime')} · Internet: **{self.ctx['internet_at_run_time']}**", ""]
        for i, t in enumerate(self.turns, 1):
            md += [f"## Turn {i}", "", f"**JD:** {t['user']}", "",
                   f"_Harness: {'notes lookup' if t['retrieved'] else 'no lookup'} — {t['retrieval_reason']}; "
                   f"{t['history_messages_sent']} earlier messages sent as context._", ""]
            for p in t["passages"]:
                md.append(f"- [{p['label']}] `{p['path']}` — {p['locator']}")
            if t["passages"]:
                md.append("")
            md += ["**Margin:**", "", t["reply"], "", f"_{t['stats']['wall_seconds']} s, {t['stats']['output_tokens']} tokens_", ""]
        records.save(self.s.runs / "chat", self.name, {**self.ctx, "turns": self.turns}, "\n".join(md))

    def save_draft(self) -> Optional[str]:
        last = next((m["content"] for m in reversed(self.history) if m["role"] == "assistant"), None)
        if not last:
            return None
        self.s.drafts.mkdir(parents=True, exist_ok=True)
        prompt = next((m["content"] for m in reversed(self.history) if m["role"] == "user"), "draft")
        path = self.s.drafts / f"{records.stamp()}-{records.slug(prompt)}.md"
        path.write_text("---\nkind: chat draft (generated; NOT a source)\n"
                        f"model: {self.client.model}\n---\n\n{last}\n", encoding="utf-8")
        return self.s.rel(path)


def run_chat(settings: Settings, client: OllamaClient, script: Optional[str] = None, search_fn=None) -> None:
    sess = ChatSession(settings, client)
    print(f"Margin — your offline study partner  [{sess.ctx['execution']} · {client.model} · "
          f"internet: {sess.ctx['internet_at_run_time']}]")
    print("Type /help for commands, /exit to leave.\n")
    lines = None
    if script:
        with open(script, encoding="utf-8") as f:
            lines = [l.rstrip("\n") for l in f if l.strip() and not l.startswith("#")]
    while True:
        if lines is not None:
            if not lines:
                break
            text = lines.pop(0)
            print(f"you> {text}")
        else:
            try:
                text = input("you> ")
            except (EOFError, KeyboardInterrupt):
                print()
                break
        text = text.strip()
        if not text:
            continue
        if text in ("/exit", "/quit"):
            break
        if text == "/help":
            print(HELP)
            continue
        if text == "/clear":
            sess.history, sess.last_passages = [], []
            print("  (conversation cleared)")
            continue
        if text == "/nonotes":
            sess.notes_enabled = not sess.notes_enabled
            print(f"  (automatic notes lookups {'on' if sess.notes_enabled else 'off'})")
            continue
        if text == "/history":
            for m in sess._trimmed_history():
                print(f"  {m['role']}: {m['content'][:100]}")
            continue
        if text == "/save":
            p = sess.save_draft()
            print(f"  (saved draft to {p})" if p else "  (nothing to save yet)")
            continue
        if text.startswith("/search"):
            if search_fn:
                search_fn(text[len("/search"):].strip())
            continue
        force = text.startswith("/notes")
        if force:
            text = text[len("/notes"):].strip()
        try:
            sess.turn(text, force_notes=force)
        except ModelUnavailable as e:
            print(f"\n  (error) {e}")
    print(f"transcript saved: {settings.rel(settings.runs / 'chat' / (sess.name + '.md'))}")
