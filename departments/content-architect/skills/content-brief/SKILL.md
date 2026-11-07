---
name: content-brief
description: Turn a topic or keyword into a content brief that can win in classic search and be quoted by AI answer engines (ChatGPT, Perplexity, Gemini, Google AI Overviews). Covers intent, what already ranks and gets cited, the information only we can add, outline, quotable blocks, proof and distribution. Use before writing any article, landing page or guide.
---

# Content brief

**Goal:** never brief a piece that can't win. Before anyone writes, decide what this piece
says that nobody else can, and whether a search engine or an AI engine would ever pick it.

## Inputs
- **Required:** topic or target query, and the business goal (traffic, leads, sales enablement, authority).
- **Optional:** target persona, existing URL to refresh, Search Console data for the topic
  (queries, impressions, position), competitor URLs the user already knows.

## Read first
- `shared/icp.md`, `shared/personas.md` (who this is for)
- `shared/offer.md` (what we can prove, where this piece leads)
- `shared/brand-voice.md`
- `shared/rejected.md` (topics or formats we already said no to)
- `departments/content-architect/memory.md`

## Steps

1. **Pin the intent.** Classify the query: learn / compare / choose / do. Write the one question
   the reader needs answered, in their words. If the goal and the intent don't match
   (e.g. "leads" from a pure definition query), say so now.
2. **Check what wins today.** Search the query. List the top results and what format they use
   (guide, list, tool, comparison). Then ask the question to at least one AI assistant with
   web access and note which sources it cites. Record: which pages are cited, by whom, and
   whether they are vendor sites or third-party sites (reviews, communities, media).
3. **Decide the information gain.** What can we add that the current winners don't have?
   Options, strongest first: our own data, a real customer example (from `offer.md` proof),
   a clear opinion with reasons, a framework, a comparison nobody made. If the answer is
   "nothing", recommend **not** writing it, or writing it as a contribution to a third-party site.
4. **Run the quote test.** For each planned section ask: *could an AI engine quote this sentence
   on its own, out of context, and be correct?* Plan at least three quotable blocks:
   a one-sentence definition, a number with its source, a short comparison table or step list.
5. **Outline.** H1 = the reader's question answered. H2s = the follow-up questions, in the order
   the reader asks them. Under each H2: the answer in the first two sentences, then detail.
6. **Proof and links.** List the proof per section (source, date). Plan internal links to and
   from existing pages, and one call to action tied to `offer.md`, matched to the intent.
7. **Distribution.** Where else must this exist for AI engines to find and trust it?
   (third-party publications, communities, partner sites, review platforms). AI answers often cite
   third-party pages more than vendor sites, so plan at least one placement off your own site.
8. **Measurement.** What to watch after publishing, and when: rankings / impressions (Search Console),
   engaged sessions and conversions (analytics), whether AI assistants start citing it (manual
   check of the same questions after 4-8 weeks).

## Output
Save to `departments/content-architect/output/YYYY-MM-DD-{slug}.md`:

```
# Brief · {working title}
Query + intent + the reader's one question
Goal and success metric
What wins today (search + AI citations), with URLs
Our information gain (or: recommendation not to write)
Quote blocks planned (3+)
Outline (H1, H2s, first-two-sentence answers)
Proof per section, internal links, CTA
Distribution plan (incl. 1 off-site placement)
Measurement plan with dates
```

## Quality bar
- The information-gain section names something specific, not "better quality" or "more depth".
- Every statistic planned has a primary source (not a blog quoting a blog).
- A writer could start from this brief without asking a single question.
- "Don't write this" is a valid, useful outcome.

## Never
- Publish, schedule or change anything in the CMS. The brief is a draft for humans.
- Invent statistics, customer stories or quotes.

## Done when
The brief is saved and the user has seen the verdict on information gain. Then run `reflect`.
