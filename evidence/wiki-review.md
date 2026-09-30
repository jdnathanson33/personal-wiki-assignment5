# Wiki review log

I read every Gemma-drafted note against the source sections it was built from (2026-09-29). Below is every correction. Notes not listed were accurate. After this review every note has `reviewed: true`.

## Link repairs

- Two Pac-Man README headings contain Markdown links (`[comparison.json](...)`), which break Obsidian heading links. Affected notes now link to the file with the plain heading text. The ingest code was fixed so this doesn't recur.

## Content corrections

| Note | Problem in the Gemma draft | Correction |
|---|---|---|
| [[Cloud Deployment]] | Implied I deployed with Supabase; my README shows Neon + Vercel (Supabase is the class slide's suggested stack). | “The Class 2 assignment named Next.js + Supabase + Vercel; my Networking Tracker was deployed on Vercel with Neon Postgres and Neon Auth.” |
| [[Context Windows]] | Slide says 1M tokens holds two copies of the ~500,000-token trilogy. | “enough to hold two copies of the Lord of the Rings trilogy (about 500,000 tokens each)” |
| [[Evaluation Design]] | Draft stated the 1,000-episode run as done; the README describes it as the next experiment. | “The proposed next experiment (not yet run) changes only the number of episodes, from 300 to 1,000, and keeps exploration at 0.10 and the learning rate at 0.0001…” |
| [[Evaluation Design]] | Vague claim not stated in the sources. | “In both projects the evaluation was small or public, so the results show limited evidence, and each README proposes a better-controlled next experiment.” |
| [[Training Loss Curves]] | Overstated ('further reduction is not possible'); README explains the floor comes from randomly filled template slots. | “For nanoGPT, loss fell quickly and then flattened at a floor above zero, because the template slots are filled at random; losses from the two experiments cannot…” |
| [[Class 3 - Machine Learning]] | Garbled merge of two agenda items on the 'Today's Route' slide. | “- The first half of the class covers AI history and the landscape and checks whether learning generalizes” |
| [[Class 3 - Machine Learning]] | Same slide: the route is the class agenda, not 'AI history'. | “- The class route includes” |
| [[Class 5 - LLMs Prompting and Retrieval]] | Reworded to match the slide's meaning. | “Fine-tuning, RLHF, and alignment are what labs do under the hood, so ideas like "Anthropic values" or "OpenAI personality" become real design choices rather tha…” |
| [[Fundamentals of Agentic AI]] | Draft implied the LLM class is the final class; the slides only cover five of seven classes. | “Fundamentals of Agentic AI is a seven-class course; this wiki covers the first five, which move from code and programming through software systems, machine lear…” |
| [[Personal Wiki Project]] | Slide says '3+ originals' (sources), not notes. | “must be built from 3+ original sources” |
| [[Tiny nanoGPT Model]] | Draft claimed the models evaluate 'language understanding based on corpus size'; the README explicitly says not to read results as understanding. | “with identical settings; only the training corpus changed. Both were scored on the same fixed 48-case language eval suite, and the README stresses that the resu…” |
| [[Tiny nanoGPT Model]] | Wrong: 4,132/460 applies only to the starter run; the expanded run was 8,790/977 (README §2 The runs). | “The train/validation split was 4,132 / 460 passages for the starter run and 8,790 / 977 for the expanded run (90/10 by passage, seed 42)” |
