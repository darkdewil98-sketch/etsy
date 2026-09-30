# Claude in Chrome prompt — round 3 (supplier variant costs + pet pillow size prices)

Paste everything inside the code block into the Claude in Chrome side panel.
Part A needs a (free) Printify account login; Part B needs Etsy (logged in is fine).

```
You are a READ-ONLY research assistant. Do NOT publish/save products, connect stores, place orders,
start subscriptions/trials, favorite, add to cart, message anyone, or spend money.
Never invent numbers. If a value is not visible, write NV.

PART A — Printify variant costs (logged in to my free Printify account)
For each product below: open the catalog page, select the US provider named, click "Start designing"
ONLY to see the variant price table (do not save/publish anything), then close without saving.
Record EVERY variant row that shows a cost: variant name (shape / sides / packaging / pack size) |
cost (free plan) | cost with Printify Premium if shown | print areas available | any upcharge for
printing the back side | shipping: first item and each additional item to the US (from the provider's
"Shipping" info) | production time shown.
1) Ceramic Decoration Ornament, (1pc) — provider SwiftPOD
   https://printify.com/app/products/1632/generic-brand/ceramic-decoration-ornament-1pc
2) Ceramic Ornaments, 2-Side Print, (1pc, 3pcs, 5pcs, 10pcs) — provider Imagine Your Photos
   https://printify.com/app/products/1370/generic-brand/ceramic-ornaments-2-side-print-1pc-3pcs-5pcs-10pcs
3) Metal Ornaments — provider Pic The Gift
   https://printify.com/app/products/1182/generic-brand/metal-ornaments
4) Glass Ornament, Single — providers SwiftPOD and Chill
   https://printify.com/app/products/2769/generic-brand/glass-ornament-single
5) White Ceramic Mug, 11oz — provider Taylor
   https://printify.com/app/products/1244/generic-brand/white-ceramic-mug-11oz
If the variant table cannot be seen without creating/saving a product, STOP for that item and write
"requires saving a product — skipped".

PART B — Etsy pet pillow prices by size
Search https://www.etsy.com/search?q=custom+pet+pillow and https://www.etsy.com/search?q=custom+dog+pillow
(default sort, USD, ship to US). Open the first 10 NON-AD listings for each keyword (skip duplicates).
For each listing record:
keyword | shop | listing URL | every size option with its price exactly as shown when selected
(e.g. 12in $24.99; 16in $32.99) | double-sided / back print option and its price if shown |
US shipping cost | personalization box Y/N | production partner text if shown |
listing review count ; shop sales if shown.

OUTPUT — plain text, " | " separators, one row per line:
BLOCK A (Printify variants)
BLOCK B (pet pillow listings)
Do not summarize or compute averages.
```
