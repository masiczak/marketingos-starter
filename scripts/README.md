# scripts/

Plain code for things that must be exact: numbers, data pulls, file checks.
The AI writes the comment around the numbers. The script produces the numbers.

| Script | What it does | Needs |
|---|---|---|
| `perf_summary.py` | campaign summary from CSV exports, current vs previous period | Python 3 (standard library only) |

Try it with the fake sample data:
```
python3 scripts/perf_summary.py --current scripts/sample-data/current.csv --previous scripts/sample-data/previous.csv --target-cpa 100
```

Integration scripts (pulling data straight from Search Console, GA4, ad platforms) are not
included on purpose: they need your accounts and credentials. `/marketingos-setup` (Step 4)
helps you decide, per tool, whether to use a ready connector, a script, or a manual export.
