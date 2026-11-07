---
name: account-brief
description: Research one target account and turn it into a fit score, a "why now", a buying-committee map and three outreach angles with first-touch drafts. Use when the user names a company (or domain) they want to approach. Produces a draft. Never sends anything.
---

# Account brief

**Goal:** in 15 minutes, know whether an account is worth pursuing, who to talk to, and what to say
that is specific to them. The output is a brief a human uses to decide and to write.

## Inputs
- **Required:** company name or website domain.
- **Optional:** a target role, a reason the user is looking at this account (event, website visit,
  referral), any notes from the CRM pasted in.

## Read first
- `shared/icp.md` (fit criteria and scoring)
- `shared/personas.md` (roles in the buying committee)
- `shared/offer.md` (what we can credibly offer, proof)
- `shared/brand-voice.md` (for the drafts)
- `departments/abm-outbound/memory.md`

If `icp.md` still has placeholders, say so and score with explicit assumptions.

## Steps

1. **Collect public facts.** Use web search (company website, news from the last 12 months,
   job postings, press releases, public reports). For every fact write: the fact, the source URL,
   the date. No source → it doesn't go in the brief.
2. **Score fit** with the table in `shared/icp.md`. Show each criterion, the evidence, the points.
   If a disqualifier applies, stop here and say why. That is a valid, useful result.
3. **Find the "why now".** Look for triggers listed in the ICP: leadership change, funding,
   expansion, hiring for related roles, new product, regulatory change. Rate each trigger:
   strong (directly creates the need) / weak (circumstantial).
4. **Map the buying committee by role.** Use `shared/personas.md`. List which roles likely exist
   at this company and which persona each matches. Use role titles, not people's names,
   unless the user supplies a name. Do not collect personal details beyond public professional role.
5. **Write three angles.** Each angle is one line of logic:
   *trigger → problem it probably causes → how our offer helps → proof → small ask.*
   Each angle targets one persona. Rank them by strength of evidence, not by creativity.
6. **Draft first touches** for the strongest angle:
   - email: max 90 words, one idea, one question at the end, no attachments
   - LinkedIn connection note: max 300 characters, no pitch
   Follow `shared/brand-voice.md`. Mention the trigger specifically. No flattery, no "I hope this finds you well".
7. **List what's missing**: facts you couldn't verify, assumptions you made, questions for the human.

## Output
Save to `departments/abm-outbound/output/accounts/YYYY-MM-DD-{company-slug}.md`:

```
# {Company} · account brief · {date}
Verdict: PURSUE / NURTURE / DROP + one-line reason
Fit score: {n}/100 (table)
Why now: {strongest trigger, source, date}
Buying committee: {roles → personas}
Angles (ranked): 1. … 2. … 3. …
Drafts: email + LinkedIn note (angle 1)
Sources: numbered list with URLs and dates
Gaps and assumptions: …
```

## Quality bar
- Every claim about the company has a source and a date. Facts older than 12 months are marked as such.
- The angles could not be sent to a different company without rewriting. If they could, they're too generic: redo step 5.
- The drafts pass the brand-voice "never" list.
- A DROP verdict with clear reasons counts as success.

## Never
- Send emails, connection requests or messages. Drafts only.
- Scrape LinkedIn or buy contact data inside this skill.
- Guess email addresses or store private contact details in the shared folder.

## Done when
The brief file exists, the verdict is stated, and the user has seen the gaps list.
Then run `reflect`.
