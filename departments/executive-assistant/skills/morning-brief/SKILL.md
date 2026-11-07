---
name: morning-brief
description: Daily morning brief for the marketing lead. Reads today's calendar, inbox highlights, open follow-ups and priorities, and returns the top three things that matter today, prep notes for each meeting, decisions waiting on you, and what to say no to. Personal: reads and writes only in private/.
---

# Morning brief

**Goal:** in 3 minutes of reading, know what today is for. Not a summary of everything:
a decision about what matters.

## Inputs (any combination)
- Today's calendar: from a connected calendar, or pasted.
- Inbox highlights: from a connected mail tool, or pasted subject lines / short notes.
- `private/priorities.md`: this week's and this quarter's priorities.
- `private/followups.md`: open promises and things to chase.
- Optional: yesterday's brief (`private/briefs/`), to carry over what didn't happen.

If nothing is connected and nothing is pasted, ask for the calendar first. That is the minimum.

## Steps

1. **Load priorities** from `private/priorities.md`. If the file is empty, ask for the top 3
   priorities of the week and save them there.
2. **Go through today's meetings.** For each: what it's for, which priority it serves (or none),
   what you need to bring or decide, one question worth asking. Look up the relevant context
   (`shared/decisions.md`, department outputs) only for meetings that need it.
   Meetings that serve no priority: flag as candidates to decline or shorten.
3. **Inbox and follow-ups.** Pick only items that need you today: a decision, a reply you promised,
   a deadline. Everything else is noise and stays out of the brief.
4. **Choose the top three.** The three things that, if done today, move a priority. Be specific
   ("send the budget proposal to X" not "work on budget").
5. **Say no to something.** Name one thing to drop, delegate or postpone, with the reason.

## Output
Save to `private/briefs/YYYY-MM-DD.md` and show it in the chat:

```
# {Weekday, date}
Top 3 today: 1. … 2. … 3. …
Meetings: time · title · purpose · prep · question to ask
Decisions waiting on you: …
Follow-ups due: …
Say no to: … (why)
Carried over from yesterday: …
```

## Quality bar
- Fits on one screen.
- Each top-3 item links to a priority.
- No item appears without a reason to be there today.

## Never
- Reply to emails, accept or decline meetings. Suggest; the human acts.
- Write anything from this brief into `shared/` or `departments/`. It's personal.

## Done when
The brief is saved in `private/briefs/` and shown. Ask if anything should move to `private/followups.md`.
