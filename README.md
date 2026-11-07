# MarketingOS Starter

A folder that turns a general AI model into **your** marketing department.

Same models for everyone. The difference is what you've written down.
You can't buy context. You can write it down.

This starter gives you the structure, four working skills and a setup assistant.
It contains **no company data**. Every file you need to fill in has `{{placeholders}}`.

---

## What's inside

```
marketingos-starter/
├── CLAUDE.md                  the switchboard: request → department → skill → files
├── shared/                    context every department reads (you fill it in)
├── private/                   yours only. Ignored by git. Never shared.
├── departments/
│   ├── abm-outbound/          skill: account-brief
│   ├── performance/           skill: weekly-performance-review
│   ├── content-architect/     skill: content-brief
│   └── executive-assistant/   skill: morning-brief
├── scripts/                   plain code for numbers (no AI guessing)
└── .claude/skills/
    ├── marketingos-setup/     guided setup, step by step
    ├── reflect/               after every finished task: what went wrong, and why
    └── memory/                writes the lesson down, so it doesn't happen twice
```

Each department has:
- `skills/`: how we do things, in plain English
- `memory.md`: lessons learned, written by the system after real work
- `integrations.md`: which tools this department needs, and how to connect them later

## Start in 3 steps

1. **Copy this folder** somewhere on your laptop that is *not* synced by iCloud, OneDrive or Dropbox
   (for example `~/marketingos`).
2. **Open it in Claude Code** (desktop app, VS Code extension or terminal).
3. Type: **`/marketingos-setup`**

The setup assistant asks you questions, fills in `shared/` with you, connects your tools one by one,
and helps you share the folder with your team. It saves progress in `SETUP-PROGRESS.md`,
so you can stop and come back tomorrow.

## Using the department skills

Just ask in plain words. `CLAUDE.md` routes the request to the right department and skill:
- "Brief me on example.com as a target account" → `account-brief`
- "Here are last week's and the week before's Google Ads exports, review them" → `weekly-performance-review`
- "Content brief for the query *how to choose a CRM for a small team*" → `content-brief`
- "Morning brief" → `morning-brief`

Skills in `.claude/skills/` (setup, reflect, memory) also work as slash commands.

## You don't need integrations to start

Every skill works today with what you paste in or export as CSV.
Integrations (Search Console, GA4, Google Ads, your CMS, your CRM) make it faster and less generic.
Add them when you're ready. Each `integrations.md` says what you'll need.

## Three rules worth keeping

1. **Nothing reaches a customer without a human click.** Skills produce drafts. You decide what runs.
2. **Numbers come from the source, not from the model's memory.** Use exports, APIs or `scripts/`.
3. **People data never enters the shared folder.** 1:1s, salaries, health, recruitment → `private/`.

---

From the talk *Build your MarketingOS in one day*, Digital Marketing Europe, Vilnius 2026.
