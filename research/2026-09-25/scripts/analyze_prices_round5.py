"""Analyze the round-5 Etsy snapshot (16 keywords x 48 cards + 80 detail rows) against verified POD costs.
Source: data/etsy_price_snapshot_round5_2026-09-26_raw.txt (values recorded verbatim from Etsy pages).
Note: review counts on cards are shop-level, not listing sales."""
import statistics as st, csv
SRC = "research/2026-09-25/data/etsy_price_snapshot_round5_2026-09-26_raw.txt"
L = open(SRC, encoding="utf-8").read().splitlines()
i2 = next(i for i, l in enumerate(L) if l.startswith("BLOCK 2"))
i3 = next(i for i, l in enumerate(L) if l.startswith("BLOCK 3"))
def num(s):
    s = s.strip().lower().replace("$", "").replace(",", "")
    if s.endswith("k"): return float(s[:-1]) * 1000
    try: return float(s)
    except: return None
cards, details = [], []
for l in L[i2 + 2:i3 - 1]:
    p = [x.strip() for x in l.split(" | ")]
    if len(p) < 14 or not p[1].isdigit(): continue
    cards.append(dict(kw=p[0], ad=p[2] == "Y", shop=p[3], title=p[4], price=num(p[5]), orig=num(p[6]) if p[6] else None,
                      free=p[8] == "Y", reviews=num(p[10]) if p[10] not in ("NV", "") else None, badges=p[11], mat=p[12], pers=p[13] == "Y"))
for l in L[i3 + 2:]:
    p = [x.strip() for x in l.split(" | ")]
    if len(p) < 11 or not p[2].startswith("http"): continue
    details.append(dict(kw=p[0], shop=p[1], ship=p[6], partner=p[9]))
SUM = {l.split(" | ")[0].strip(): l.split(" | ")[1].strip() for l in L[13:i2 - 1] if " | " in l}
FILT = {l.split(" | ")[0].strip(): l.split(" | ")[2].strip() for l in L[13:i2 - 1] if " | " in l}
# opportunity keyword -> (product label, POD cost incl. US first-item shipping) — all verified 2026-09-25/26
COST = {
 "auntie shirt": ("Printful Bella+Canvas 3001 tee", 16.87), "aunt shirt": ("Printful Bella+Canvas 3001 tee", 16.87),
 "dog memorial gift": ("Printful Canvas 10x10", 23.62), "cat memorial ornament": ("Printify/SwiftPOD ceramic 2-side", 11.36),
 "baptism ornament": ("Printify/SwiftPOD ceramic 2-side", 11.36), "pregnancy ornament": ("Printify/SwiftPOD ceramic 2-side", 11.36),
 "custom dog shirt": ("Printful Bella+Canvas 3001 tee", 16.87), "personalized grandma sweatshirt": ("Printful Gildan 18000 + sleeve", 33.91),
 "new grandma mug": ("Printful White Glossy Mug 11oz", 12.76), "uncle mug": ("Printful White Glossy Mug 11oz", 12.76),
 "bookish stickers": ("Printful kiss-cut sticker 3x3", 6.83), "nurse sweatshirt": ("Printful Gildan 18000", 27.96),
 "custom embroidered sweatshirt": ("Printful Gildan 18000 embroidery", 30.91), "family christmas shirts": ("Printful Bella+Canvas 3001 tee", 16.87),
 "turkey trot shirt": ("Printful Bella+Canvas 3001 tee", 16.87), "christmas tree skirt": ("Printful Christmas Tree Skirt", 51.74),
}
def q(v, f):
    v = sorted(v); k = (len(v) - 1) * f; lo = int(k); hi = min(lo + 1, len(v) - 1)
    return round(v[lo] + (v[hi] - v[lo]) * (k - lo), 2)
rows = []
for kw, (prod, cost) in COST.items():
    c = [x for x in cards if x["kw"] == kw]; pr = [x["price"] for x in c if x["price"]]
    d = [x for x in details if x["kw"] == kw]
    ships = [num(x["ship"]) for x in d if num(x["ship"]) is not None]
    nfree = sum(1 for x in d if x["ship"].lower().startswith("free"))
    ship = round(st.median(ships), 2) if ships else 0.0
    med, p75 = st.median(pr), q(pr, .75)
    contrib = lambda t: round((t + ship) * 0.905 - 0.45 - cost, 2)
    mats = {}
    for x in c: mats[x["mat"]] = mats.get(x["mat"], 0) + 1
    rows.append(dict(keyword=kw, product=prod, pod_cost=cost, result_count=SUM.get(kw, "NV"), filters=FILT.get(kw, "NV"),
        cards=len(c), ads=sum(x["ad"] for x in c), min=min(pr), p25=q(pr, .25), median=round(med, 2), p75=p75, max=max(pr),
        on_sale_pct=round(100 * sum(1 for x in c if x["orig"]) / len(c)), free_ship_pct=round(100 * sum(x["free"] for x in c) / len(c)),
        pers_pct=round(100 * sum(x["pers"] for x in c) / len(c)), shop_reviews_1k_plus=sum(1 for x in c if (x["reviews"] or 0) >= 1000),
        bestseller=sum("Bestseller" in x["badges"] for x in c), star=sum("Star Seller" in x["badges"] for x in c),
        detail_n=len(d), detail_ship_median=ship if ships else "all free", detail_free=nfree,
        detail_partner=sum(1 for x in d if "with help from" in x["partner"]),
        top_materials=", ".join(f"{k} {v}" for k, v in sorted(mats.items(), key=lambda t: -t[1])[:3]),
        contrib_median=contrib(med), contrib_p75=contrib(p75)))
rows.sort(key=lambda r: -r["contrib_p75"])
with open("research/2026-09-25/data/price_analysis_round5.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows:
    print(f'{r["keyword"]:<32} med ${r["median"]:>6.2f} p75 ${r["p75"]:>6.2f} ship {r["detail_ship_median"]} | cost {r["pod_cost"]:>5} -> med {r["contrib_median"]:>7} p75 {r["contrib_p75"]:>7} | sale {r["on_sale_pct"]}% 1k+shop {r["shop_reviews_1k_plus"]}/48 | {r["top_materials"][:52]}')
