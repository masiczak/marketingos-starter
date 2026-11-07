#!/usr/bin/env python3
"""Campaign performance summary from CSV exports. Standard library only.

Every number in the weekly review comes from here, not from the model's memory.

Usage:
  python3 scripts/perf_summary.py --current this.csv [--previous last.csv]
         [--map "spend=Cost,conversions=Conv."] [--target-cpa 120] [--waste 240]

Flags per campaign: no conversions (and spend above --waste, if given),
CPA >130% of target, CTR or conversion rate down more than 25% vs previous period
(conversion-rate drops need >=5 previous conversions, otherwise: "low volume, watch").

Column names are matched case-insensitively against common export headers
(Google Ads, Microsoft Ads, LinkedIn, Meta). Use --map when yours differ.
"""
import argparse
import csv
import sys

ALIASES = {
    "campaign": ["campaign", "campaign name", "campaign_name"],
    "spend": ["cost", "spend", "amount spent", "total spent", "amount spent (eur)",
              "amount spent (usd)", "spend (eur)", "spend (usd)"],
    "clicks": ["clicks", "link clicks"],
    "impressions": ["impressions", "impr.", "impr"],
    "conversions": ["conversions", "conv.", "conversions (all)", "results", "leads"],
}


def num(value):
    if value is None:
        return 0.0
    v = str(value).strip().replace(" ", "").replace(" ", "")
    for sym in ("€", "$", "£", "zł", "%"):
        v = v.replace(sym, "")
    if v in ("", "-", "--"):
        return 0.0
    if "," in v and "." in v:
        v = v.replace(",", "") if v.rfind(".") > v.rfind(",") else v.replace(".", "").replace(",", ".")
    elif "," in v:
        v = v.replace(",", ".") if len(v.split(",")[-1]) != 3 else v.replace(",", "")
    try:
        return float(v)
    except ValueError:
        return 0.0


def find_header(rows):
    """Skip report title lines that some platforms put above the header."""
    for i, row in enumerate(rows[:15]):
        low = [c.strip().lower() for c in row]
        if any(a in low for a in ALIASES["campaign"]) and any(a in low for a in ALIASES["spend"]):
            return i
    return 0


def load(path, overrides):
    with open(path, newline="", encoding="utf-8-sig") as f:
        sample = f.read(4096)
        f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
        except csv.Error:
            dialect = csv.excel
        rows = list(csv.reader(f, dialect))
    h = find_header(rows)
    header = [c.strip() for c in rows[h]]
    low = [c.lower() for c in header]
    cols = {}
    for key, names in ALIASES.items():
        if key in overrides:
            target = overrides[key].strip().lower()
            if target not in low:
                sys.exit(f"[{path}] --map {key}={overrides[key]}: column not found. Columns: {header}")
            cols[key] = low.index(target)
            continue
        for n in names:
            if n in low:
                cols[key] = low.index(n)
                break
    missing = [k for k in ALIASES if k not in cols]
    if missing:
        sys.exit(f"[{path}] missing columns: {missing}. Columns found: {header}\n"
                 f"Map them with --map \"{missing[0]}=<your column name>\"")
    data = {}
    for row in rows[h + 1:]:
        if len(row) <= max(cols.values()):
            continue
        name = row[cols["campaign"]].strip()
        if not name or name.lower().startswith(("total", "--")):
            continue
        d = data.setdefault(name, {"spend": 0.0, "clicks": 0.0, "impressions": 0.0, "conversions": 0.0})
        for k in ("spend", "clicks", "impressions", "conversions"):
            d[k] += num(row[cols[k]])
    return data


def metrics(d):
    ctr = d["clicks"] / d["impressions"] * 100 if d["impressions"] else None
    cpc = d["spend"] / d["clicks"] if d["clicks"] else None
    cpa = d["spend"] / d["conversions"] if d["conversions"] else None
    cvr = d["conversions"] / d["clicks"] * 100 if d["clicks"] else None
    return ctr, cpc, cpa, cvr


def fmt(x, nd=2):
    return "—" if x is None else f"{x:,.{nd}f}"


def delta(cur, prev):
    if cur is None or prev in (None, 0):
        return "—"
    return f"{(cur - prev) / prev * 100:+.0f}%"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--current", required=True)
    p.add_argument("--previous")
    p.add_argument("--map", default="", help='e.g. "spend=Cost,conversions=Conv."')
    p.add_argument("--target-cpa", type=float)
    p.add_argument("--waste", type=float, help="flag spend above this with zero conversions")
    a = p.parse_args()
    overrides = dict(x.split("=", 1) for x in a.map.split(",") if "=" in x)

    cur = load(a.current, overrides)
    prev = load(a.previous, overrides) if a.previous else {}

    def total(data):
        t = {"spend": 0.0, "clicks": 0.0, "impressions": 0.0, "conversions": 0.0}
        for d in data.values():
            for k in t:
                t[k] += d[k]
        return t

    tc, tp = total(cur), total(prev) if prev else None
    print("## Totals")
    print("| Metric | Current | Previous | Change |")
    print("|---|---:|---:|---:|")
    for k in ("spend", "clicks", "impressions", "conversions"):
        nd = 0 if k in ("clicks", "impressions") else 2
        print(f"| {k} | {fmt(tc[k], nd)} | {fmt(tp[k], nd) if tp else '—'} | {delta(tc[k], tp[k]) if tp else '—'} |")
    c_ctr, c_cpc, c_cpa, c_cvr = metrics(tc)
    p_ctr, p_cpc, p_cpa, p_cvr = metrics(tp) if tp else (None, None, None, None)
    print(f"| CTR % | {fmt(c_ctr)} | {fmt(p_ctr)} | {delta(c_ctr, p_ctr)} |")
    print(f"| CPC | {fmt(c_cpc)} | {fmt(p_cpc)} | {delta(c_cpc, p_cpc)} |")
    print(f"| CPA | {fmt(c_cpa)} | {fmt(p_cpa)} | {delta(c_cpa, p_cpa)} |")
    print(f"| Conv. rate % | {fmt(c_cvr)} | {fmt(p_cvr)} | {delta(c_cvr, p_cvr)} |")

    print("\n## Campaigns (sorted by spend)")
    print("| Campaign | Spend | Clicks | CTR % | CTR vs prev | CPC | Conv. | Conv. rate % | CVR vs prev | CPA | CPA vs prev | Flag |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|")
    for name, d in sorted(cur.items(), key=lambda kv: -kv[1]["spend"]):
        ctr, cpc, cpa, cvr = metrics(d)
        pctr, _, pcpa, pcvr = metrics(prev[name]) if name in prev else (None, None, None, None)
        flags = []
        if d["spend"] > 0 and d["conversions"] == 0:
            if a.waste is None or d["spend"] > a.waste:
                flags.append("waste: no conversions")
        if a.target_cpa and cpa and cpa > a.target_cpa * 1.3:
            flags.append("CPA >130% target")
        if ctr is not None and pctr and (ctr - pctr) / pctr < -0.25:
            flags.append("CTR drop >25%")
        if cvr is not None and pcvr and (cvr - pcvr) / pcvr < -0.25:
            # too few conversions to call it a trend: say so instead of flagging
            if name in prev and prev[name]["conversions"] >= 5 and d["conversions"] > 0:
                flags.append("conv. rate drop >25%")
            elif d["conversions"] > 0:
                flags.append("low volume, watch")
        if name not in prev and prev:
            flags.append("new")
        print(f"| {name} | {fmt(d['spend'])} | {fmt(d['clicks'],0)} | {fmt(ctr)} | {delta(ctr, pctr)} | {fmt(cpc)} | "
              f"{fmt(d['conversions'],1)} | {fmt(cvr)} | {delta(cvr, pcvr)} | {fmt(cpa)} | {delta(cpa, pcpa)} | {', '.join(flags)} |")
    gone = [n for n in prev if n not in cur]
    if gone:
        print(f"\nIn previous period only: {', '.join(gone)}")


if __name__ == "__main__":
    main()
