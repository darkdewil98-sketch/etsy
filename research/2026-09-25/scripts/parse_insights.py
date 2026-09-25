"""Parse the Marketplace Insights export (Table A) into a flat keyword universe.
Every number comes verbatim from the Insights page as captured in marketplace_insights_raw.txt."""
import re, csv, sys
SRC = "research/2026-09-25/data/marketplace_insights_raw.txt"
def num(s):
    s = s.strip().replace(",", "")
    m = {"k": 1e3, "M": 1e6}.get(s[-1:], 1)
    return float(s[:-1]) * m if s[-1:] in "kM" else float(s)
lines = open(SRC, encoding="utf-8").read().splitlines()
start = next(i for i, l in enumerate(lines) if l.startswith("keyword | searches"))
end = next(i for i, l in enumerate(lines) if l.startswith("TABLE B"))
seeds, pool = [], {}
for l in lines[start + 2:end - 1]:
    p = [x.strip() for x in l.split(" | ")]
    if len(p) < 9: continue
    kw, s, chg, li, conv, per, tier, ratio, rel = p[:9]
    seeds.append(dict(keyword=kw, searches=s, searches_n=num(s), chg=chg, listings=li, listings_n=num(li),
                      conv=conv, tier=tier, source="searched"))
    pool.setdefault(kw, dict(keyword=kw, searches=s, listings=li, conv=conv, chg=chg, seen_in=tier))
    for t in rel.split("; "):
        m = re.match(r"(.+?) ([\d.,]+[kM]?)/([\d.,]+[kM]?) (VL|L|T|H|VH)$", t.strip())
        if not m: continue
        term = m.group(1)
        if term not in pool:
            pool[term] = dict(keyword=term, searches=m.group(2), listings=m.group(3), conv=m.group(4), chg="", seen_in=f"related of {kw}")
rows = []
for d in pool.values():
    d["searches_n"] = num(d["searches"]); d["listings_n"] = num(d["listings"])
    d["ratio"] = round(d["searches_n"] / d["listings_n"], 4) if d["listings_n"] else 0
    rows.append(d)
rows.sort(key=lambda r: -r["searches_n"])
out = "research/2026-09-25/data/insights_keyword_universe.csv"
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["keyword", "searches", "listings", "ratio", "conv", "chg", "seen_in", "searches_n", "listings_n"])
    w.writeheader(); w.writerows(rows)
print(f"searched keywords: {len(seeds)}; unique keywords incl. related: {len(rows)} -> {out}")
