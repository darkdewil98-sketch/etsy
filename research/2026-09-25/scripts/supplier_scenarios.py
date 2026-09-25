"""Round-3 (2026-09-25) verified variant costs: SwiftPOD Round $4.93 / Heart $5.25 / +gift box $7.06; Economy US shipping
$4.79 first + $0.49 each additional (Standard $5.89 / $0.69). Back-side print upcharge NOT VERIFIED.
Compare contribution per order across verified POD supplier costs, using verified Etsy competitor prices.
Supplier costs: Printful public API/shipping page and Printify public catalog pages (US local providers), 2026-09-25.
Printify 'From USD' = cheapest variant; extra-variant (e.g. 2-side print, gift box) cost NOT VERIFIED."""
import csv, json
PA = {r["keyword"]: r for r in csv.DictReader(open("research/2026-09-25/data/price_analysis.csv"))}
S = {  # product family -> [(supplier label, product cost, US shipping first item)]
 "ornament": [("Printful ceramic 2-side #900", 7.73, 5.89),
              ("Printify / SwiftPOD ceramic Round (bp 1632), Economy ship", 4.93, 4.79),
              ("Printify / SwiftPOD ceramic Round, Premium, Economy ship", 3.88, 4.79),
              ("Printify / SwiftPOD ceramic Heart, Economy ship", 5.25, 4.79),
              ("Printify / SwiftPOD ceramic Round + gift box, Economy ship", 7.06, 4.79),
              ("Printify / Pic The Gift metal (bp 1182, from)", 4.75, 5.89),
              ("Printify / SwiftPOD glass (bp 2769, from)", 5.59, 4.79)],
 "mug15": [("Printful 15oz #19", 8.11, 7.29), ("Printful 11oz #19", 6.07, 6.69),
           ("Printify / Taylor 11oz (bp 1244)", 5.86, 7.29), ("Printify / Taylor 11oz, Premium", 4.38, 7.29),
           ("Printify / SPOKE 15oz (bp 425, from)", 8.62, 8.69)],
 "stocking": [("Printful rustic #1428", 17.17, 7.79), ("Printify / MWW (bp 380, from)", 18.08, 6.59),
              ("Printify / MWW, Premium", 13.11, 6.59), ("Printify / Imagine Your Photos (bp 734, from)", 17.16, 8.79)],
}
KW = {"engagement ornament": "ornament", "first christmas married ornament": "ornament", "newlywed ornament": "ornament",
      "baby's first christmas ornament": "ornament", "new house ornament": "ornament", "family of 4 ornament": "ornament",
      "auntie mug": "mug15", "retirement gifts for women": "mug15", "personalized christmas stocking": "stocking", "dog christmas stocking": "stocking"}
def contrib(total, cost): return round(total * 0.905 - 0.45 - cost, 2)
rows = []
for kw, fam in KW.items():
    a = PA[kw]; ship = 0.0 if a["detail_ship_median"] == "all free" else float(a["detail_ship_median"])
    med, p75 = float(a["median"]) + ship, float(a["p75"]) + ship
    for lab, c, s in S[fam]:
        cost = round(c + s, 2)
        rows.append(dict(keyword=kw, supplier=lab, unit_cost=cost, buyer_total_median=round(med, 2), buyer_total_p75=round(p75, 2),
                         contrib_median=contrib(med, cost), contrib_p75=contrib(p75, cost)))
with open("research/2026-09-25/data/supplier_scenarios.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows: print(f'{r["keyword"]:<34} {r["supplier"]:<46} cost {r["unit_cost"]:>6} | med {r["contrib_median"]:>7} | p75 {r["contrib_p75"]:>7}')
# Marginal contribution of each additional ornament in the same order (buyer pays median item price, no extra shipping charged;
# Etsy $0.20 listing fee applies per unit, $0.25 processing fixed fee does not repeat)
for kw in ["engagement ornament", "new house ornament", "baby's first christmas ornament"]:
    m = float(PA[kw]["median"])
    print(f"extra-unit contribution {kw}: ${round(m * 0.905 - 0.20 - (4.93 + 0.49), 2)} (SwiftPOD Round + $0.49 extra-item shipping, at median ${m})")
# Premium break-even: yearly plan $24.99/month (Printify pricing page, 2026-09-25)
save = 4.93 - 3.88
print(f"\nPremium break-even (ornaments, SwiftPOD): $24.99 / ${save:.2f} per unit = {24.99/save:.1f} ornaments per month")
