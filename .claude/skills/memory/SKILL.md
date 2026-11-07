---
name: memory
description: Writes a confirmed lesson into the right place so the same mistake doesn't happen twice. Called by reflect after the user agrees. Also use when the user says "remember that…" or "from now on…". Keeps memory files short by merging and deleting.
---

# Memory

**Goal:** one lesson, in the one place where it will be read next time. Short files stay useful.
Long files get ignored.

## Where a lesson goes

| The lesson is about… | Write it to |
|---|---|
| how one department should work | `departments/{dept}/memory.md` |
| a missing or wrong fact about the company, customers, offer, voice | the matching `shared/*.md` file (edit the fact itself, not a note about it) |
| a decision made, with its reason | `shared/decisions.md` |
| an idea rejected, with its reason | `shared/rejected.md` |
| a step that should always happen in a skill | that skill's `SKILL.md` (edit the step) |
| a rule for every task | `CLAUDE.md` → Rules (only if truly universal; keep that file short) |
| something personal, or about a specific person | `private/` only |

When unsure, prefer the most specific place (a department) over the most general (`CLAUDE.md`).

## Steps

1. **Read the target file first.** Is this lesson already there, or does it contradict something?
2. **Write one line** in the file's format:
   `- YYYY-MM-DD · {lesson, as an instruction} · {why / which task}`
   Write it as an instruction for next time ("Check the date range before computing CPA"),
   not as a story ("Last time the dates were wrong").
3. **Merge or replace.** If a similar line exists, update it instead of adding a new one.
   If the new lesson contradicts an old one, replace the old one and say so.
4. **Keep it short.** If a department memory has more than ~30 lines, propose which lines to
   delete or merge: closed projects, fixed problems, lessons that are now part of a skill.
5. **Confirm** to the user in one line: what was written, where.

## Never
- Store secrets, personal data about colleagues or customers' personal details.
- Write to `shared/` or `CLAUDE.md` without showing the change first.
