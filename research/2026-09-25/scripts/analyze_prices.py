"""Analyze the 14-keyword Etsy search snapshot (672 cards + 70 detail pages) against verified POD costs.
All inputs are values recorded verbatim from Etsy pages (data/etsy_price_snapshot_raw.txt)."""
import re, statistics as st, csv
SRC = "research/2026-09-25/data/etsy_price_snapshot_raw.txt"
L = open(SRC, encoding="utf-8").read().splitlines()
i2 = next(i for i, l in enumerate(L) if l.startswith("BLOCK 2")); i3 = next(i for i, l in enumerate(L) if l.startswith("BLOCK 3"))
def num(s):
    s = s.strip().lower().replace("$", "").replace(",", "")
    if s.endswith("k"): return float(s[:-1]) * 1000
    try: return float(s)
    except: return None
cards = []
for l in L[i2 + 2:i3 - 1]:
    p = [x.strip() for x in l.split(" | ")]
    if len(p) < 14 or not p[1].isdigit(): continue
    cards.append(dict(kw=p[0], pos=int(p[1]), ad=p[2] == "Y", shop=p[3], title=p[4], price=num(p[5]), orig=num(p[6]) if p[6] else None,
                      free=p[8] == "Y", rating=p[9], reviews=num(p[10]) if p[10] not in ("NV", "") else None, badges=p[11], mat=p[12], pers=p[13] == "Y"))
details = []
for l in L[i3 + 2:]:
    p = [x.strip() for x in l.split(" | ")]
    if len(p) < 12 or not p[2].startswith("http"): continue
    details.append(dict(kw=p[0], shop=p[1], url=p[2], default=p[3], rng=p[4], ship=p[6], partner=p[9]))
# Verified Printful cost incl. US first-item shipping (see README section 2)
COST = {"ornament": 13.62, "stocking": 24.96, "mug15": 15.40, "pillow": 22.79, "tote": 20.56}
KWP = {"engagement ornament": "ornament", "personalized engagement ornament": "ornament", "first christmas married ornament": "ornament",
       "newlywed ornament": "ornament", "personalized christmas stocking": "stocking", "dog christmas stocking": "stocking", "auntie mug": "mug15",
       "custom pet pillow": "pillow", "custom dog pillow": "pillow", "baby's first christmas ornament": "ornament", "new house ornament": "ornament",
       "retirement gifts for women": "mug15", "family of 4 ornament": "ornament", "teacher thank you gift": "tote"}
def q(v, f): v = sorted(v); return v[min(len(v) - 1, int(round(f * (len(v) - 1))))] if v else None
def contrib(total, cost): return round(total * 0.905 - 0.45 - cost, 2)
rows = []
for kw in KWP:
    c = [x for x in cards if x["kw"] == kw]; pr = [x["price"] for x in c if x["price"]]; org = [x for x in c if x["price"] and not x["ad"]]
    d = [x for x in details if x["kw"] == kw]
    ships = [num(x["ship"]) for x in d if num(x["ship"]) is not None]; nfree = sum(1 for x in d if x["ship"].lower().startswith("free"))
    partner = sum(1 for x in d if "makes this item with help from" in x["partner"])
    medp = st.median(pr); meds = st.median(ships) if ships else 0.0
    mats = {}
    for x in c: mats[x["mat"]] = mats.get(x["mat"], 0) + 1
    cost = COST[KWP[kw]]
    rows.append(dict(keyword=kw, cards=len(c), ads=sum(x["ad"] for x in c), p25=q(pr, .25), median=medp, p75=q(pr, .75), min=min(pr), max=max(pr),
        organic_median=st.median([x["price"] for x in org]) if org else None,
        on_sale_pct=round(100 * sum(1 for x in c if x["orig"]) / len(c)), free_ship_cards_pct=round(100 * sum(x["free"] for x in c) / len(c)),
        reviews_1k_plus=sum(1 for x in c if (x["reviews"] or 0) >= 1000), bestseller=sum("Bestseller" in x["badges"] for x in c),
        star=sum("Star Seller" in x["badges"] for x in c), pers_pct=round(100 * sum(x["pers"] for x in c) / len(c)),
        top_materials=", ".join(f"{k} {v}" for k, v in sorted(mats.items(), key=lambda t: -t[1])[:4]),
        detail_n=len(d), detail_ship_median=meds if ships else "all free", detail_free=nfree, detail_partner=partner,
        pod_cost=cost, contrib_free_ship_at_median=contrib(medp, cost), contrib_with_ship_at_median=contrib(medp + meds, cost),
        contrib_at_p75_with_ship=contrib(q(pr, .75) + meds, cost)))
out = "research/2026-09-25/data/price_analysis.csv"
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows:
    print(f'{r["keyword"]:<34} med ${r["median"]:.2f} (P25 {r["p25"]}, P75 {r["p75"]}) sale {r["on_sale_pct"]}% freeship {r["free_ship_cards_pct"]}% 1k+ {r["reviews_1k_plus"]}/48 '
          f'ship(det) {r["detail_ship_median"]} partner {r["detail_partner"]}/{r["detail_n"]} | cost {r["pod_cost"]} -> contrib free {r["contrib_free_ship_at_median"]} / +ship {r["contrib_with_ship_at_median"]} / P75+ship {r["contrib_at_p75_with_ship"]} | {r["top_materials"]}')
