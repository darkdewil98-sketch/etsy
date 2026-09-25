"""Size-matched (~16 in) pet-pillow prices from round-3 Etsy detail pages.
Each row is copied from data/round3_printify_variants_and_pillow_sizes_raw.txt (Block B): the size option closest to
16 in (15.4–16.9 in) and the listing's US shipping. Unique listings only; PawsonaCA (lumbar, no size) excluded."""
import csv, statistics as st
ROWS = [  # shop, option as shown, price, US shipping, note
 ("CathyHandcraftShop", '16"-Small–Medium', 25.99, 2.99, "white; other colors +$1"),
 ("SecretGardenbyGrace", '15.7"', 24.90, 0.00, "Spreadshirt partner"),
 ("AmyEngravedGifts", "40 cm (15.75 in)", 26.31, 6.92, ""),
 ("Lamoriea", "39cm/15.4inch", 24.21, 6.23, "43cm/16.9in = $29.06"),
 ("aurespaces", 'MEDIUM 16"', 52.70, 0.00, "eco canvas; double-sided up to $62.01"),
 ("LightMomentStudio", "16x16 - Case+Insert", 45.48, 5.99, "square pillow, not shaped; case only $27.48"),
 ("PawsInMemory", "16 inch (40 cm)", 24.90, 4.99, "double-sided included"),
 ("habinisi", "40cm(15.75in)", 19.20, 2.99, ""),
 ("GaiaByDin", "16in/40cm", 24.56, 0.00, ""),
 ("DripDropPrint", "40cm", 29.34, 0.00, "Printcious (HK) partner"),
 ("DoggoandHooman", 'Medium (16")', 34.80, 5.50, "Print Shop 3, Fridley MN"),
 ("CutiqueGifts", "16 inch", 43.89, 6.97, "Print on demand, Charlotte NC"),
]
tot = sorted(p + s for _, _, p, s, _ in ROWS)
def q(v, f):
    k = (len(v) - 1) * f; lo = int(k); hi = min(lo + 1, len(v) - 1)
    return round(v[lo] + (v[hi] - v[lo]) * (k - lo), 2)
summary = dict(n=len(tot), min=tot[0], p25=q(tot, .25), median=round(st.median(tot), 2), p75=q(tot, .75), max=tot[-1])
COST = 16.60 + 6.19  # Printful Custom Shaped Pillow 16x16 (#743) + US shipping (verified 2026-09-25)
contrib = lambda t: round(t * 0.905 - 0.45 - COST, 2)
summary.update(cost=round(COST, 2), contrib_median=contrib(summary["median"]), contrib_p75=contrib(summary["p75"]))
with open("research/2026-09-25/data/pillow_16in_prices.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["shop", "option", "price", "us_shipping", "buyer_total", "note"])
    for r in ROWS: w.writerow([r[0], r[1], r[2], r[3], round(r[2] + r[3], 2), r[4]])
    w.writerow([]); [w.writerow([k, v]) for k, v in summary.items()]
print(summary)
