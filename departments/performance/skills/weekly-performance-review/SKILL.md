---
name: weekly-performance-review
description: Weekly review of paid campaigns from platform exports (Google Ads, Microsoft Ads, LinkedIn, Meta or any CSV with spend and conversions). Computes metrics with a script, compares with the previous period and with targets, flags waste and opportunities, and proposes actions for a human to approve. Never changes anything in an ad account.
---

# Weekly performance review

**Goal:** in 10 minutes, know where money was wasted, where to add budget, and what to test next.
Every number comes from the data, computed by code. The AI writes the comment around it.

## Inputs
- **Required:** one CSV export per platform, campaign level, for **this period** and the **previous period**
  (same length, e.g. last 7 days and the 7 days before).
  Minimum columns: campaign, cost/spend, clicks, impressions, conversions.
  Optional: conversion value, impression share lost to budget.
- **Optional:** search terms report (Google / Microsoft Ads) for waste detection.

If no files are given, tell the user exactly what to export (platform, report, columns, date ranges).
Once an integration is connected (`integrations.md`), pull the same data through it instead.

## Read first
- `departments/performance/targets.md` (target CPA / ROAS, budget limits)
- `shared/offer.md` (which campaigns map to which offer)
- `departments/performance/memory.md`

## Steps

1. **Validate the data.** Check: date ranges match and don't overlap, same currency, no empty
   conversion column, no duplicated campaigns. If something is off, stop and say what.
2. **Compute with the script**, not in your head:
   ```
   python3 scripts/perf_summary.py --current this.csv --previous last.csv --target-cpa {from targets.md} --waste {from targets.md}
   ```
   It prints totals and a per-campaign table: spend, clicks, CTR, CPC, conversions, conversion rate,
   CPA, changes vs previous period, and flags (waste, CPA over target, CTR / conversion-rate drops). If the export columns have different names, the script tells you;
   map them with `--map "spend=Cost,conversions=Conv."`.
3. **Flag, using `targets.md`** (the script already marks the first three; you add the rest):
   - **Waste:** campaigns with spend above the waste threshold and zero conversions.
   - **Over target:** CPA more than 30% above target (or ROAS 30% below).
   - **Drops:** CTR or conversion rate down more than 25% vs previous period.
   - **Opportunities:** CPA below target **and** impression share lost to budget > 10%.
   - **Search terms** (if provided): terms with spend and no conversions that don't match the offer → negative keyword candidates.
4. **Look for the cause before proposing a fix.** For each flag, list possible causes in order
   of likelihood (tracking issue, seasonality, landing page change, competitor, creative fatigue)
   and what would confirm each. Mark clearly: hypothesis, not fact.
5. **Propose actions.** Max 5, ranked by expected impact. Each: what to change, why (number),
   expected effect, how we'll know in a week. These are proposals. A human approves each one.

## Output
Save to `departments/performance/output/YYYY-MM-DD-weekly.md`:

```
# Weekly performance · {period}
Summary (5 lines max): spend, conversions, CPA vs target, biggest change, biggest risk
Table: per campaign (from the script)
Flags: waste / over target / drops / opportunities
Proposed actions (for approval): 1-5
Data notes: date ranges, sources, anything missing
```

## Quality bar
- Every number in the summary appears in the script output. No rounding that changes meaning.
- Each proposed action names the number that justifies it.
- Hypotheses are labelled as hypotheses.

## Never
- Change bids, budgets, status or targeting in any ad account. Even if an integration allows it,
  this skill only proposes.
- Report a number the script didn't produce.

## Done when
The report is saved and the user has the list of proposed actions. Then run `reflect`.
