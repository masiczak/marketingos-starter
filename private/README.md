# private/

This folder is **ignored by git**. Nothing here is ever shared, even if the rest of the
folder goes to GitHub. Only this README is tracked, so the folder exists after cloning.

Put here:
- `priorities.md`: your goals and this week's priorities (read by morning-brief)
- `followups.md`: open threads, promises, things to chase (read by morning-brief)
- `briefs/`: generated morning briefs
- 1:1 notes, career goals, anything about people on your team
- anything personal

Rule: if it's about a person, not about the work, it lives here.
Check before your first push: `git check-ignore -v private/priorities.md` should print a match.
