---
name: reflect
description: Post-task reflection. Run after every finished task (not after quick questions). Asks what went wrong or took too long, why, and whether a lesson should be kept. If yes, hands over to the memory skill. This is how the system gets better every time you use it.
---

# Reflect

**Goal:** catch the lesson while the task is fresh. Two minutes, not a retrospective.

## When
- After a skill finishes (account brief, weekly review, content brief, morning brief, any new skill).
- After any task where the user corrected you, a tool failed, or the result needed rework.
- Skip for quick questions and one-line answers.

## Steps

1. **Look back at this task.** Answer briefly:
   - What did the user correct, reject or redo?
   - What took longer than it should (missing context, wrong file, tool failure, unclear step)?
   - What did you have to guess? Was the guess right?
   - What worked well and should become the default?
2. **Find the cause**, one level deeper than the symptom. Classify it:
   - `context`: a fact was missing or wrong in `shared/` (e.g. ICP outdated)
   - `skill`: a step was missing, unclear or in the wrong order
   - `tool`: an integration or script failed or gave bad data
   - `preference`: the user wants it done differently (format, tone, length)
   - `none`: nothing worth keeping
3. **Decide.** Is this lesson likely to matter again? If it happened once by chance, drop it.
   If it would change how the task is done next time, keep it.
4. **Propose, don't apply.** Show the user one short block:
   ```
   Reflect · {task}
   What happened: …
   Cause ({category}): …
   Proposed fix: {which file, what change}
   ```
   Ask: keep it? On "yes", run the `memory` skill with this block.
   If the fix is to a skill or a `shared/` file, show the exact edit before making it.

## Never
- Write lessons about people (who made a mistake, who is slow). Lessons are about the system.
- Edit `shared/` or a skill without the user's yes.
