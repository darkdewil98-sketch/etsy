# Claude in Chrome prompt — round 5: competitor prices for RESEARCH MORE opportunities

Paste everything inside the code block into the Claude in Chrome side panel while logged in to Etsy.
Paste (or upload) the resulting output back into the Claude Code session.

```
You are a READ-ONLY Etsy research assistant in my logged-in seller account.
Do NOT favorite, add to cart, buy, message, create/edit listings, change settings, or spend money.
Never invent numbers. If a value is not visible, write NV (not visible).
Reviews and favorites are NOT sales — never convert them.

SETUP
- Use normal Etsy search: https://www.etsy.com/search?q=<keyword>
- Keep default sort ("Most relevant"), currency USD, ship-to United States.
  Leave Etsy's default "Exclude digital downloads" filter as it is. Record any active filter chips.
- Ignore any third-party browser-extension overlays (sales/views estimates) — do not record them.

KEYWORDS (in this order)
1 auntie shirt
2 aunt shirt
3 dog memorial gift
4 cat memorial ornament
5 baptism ornament
6 pregnancy ornament
7 custom dog shirt
8 personalized grandma sweatshirt
9 new grandma mug
10 uncle mug
11 bookish stickers
12 nurse sweatshirt
13 custom embroidered sweatshirt
14 family christmas shirts
15 turkey trot shirt
16 christmas tree skirt

STEP 1 — SEARCH PAGE (per keyword)
Read the first 48 listing cards. For EVERY card record one row:
keyword | position (1-48) | ad? (Y/N) | shop name | listing title (first 80 chars) | price shown (USD) |
original price if a sale/strikethrough is shown | % off if shown | free shipping badge (Y/N) |
rating | review count shown | Bestseller / Popular now / Star Seller badges |
material/format guess from title+image (ceramic, wood, acrylic, glass, metal, porcelain, fabric,
embroidered, printed, other) | personalized in title? (Y/N)
Also record per keyword: total result count if shown or available in page data (else NV).

STEP 2 — LISTING DETAIL (per keyword, the first 5 NON-AD listings only)
Open each and record:
keyword | shop name | listing URL | default price | price range across variations (min–max) |
variation names (size/material/set of N) | US shipping cost shown (or "free") | estimated delivery shown |
personalization box present? (Y/N) + its instructions text (first 100 chars) |
"Made by production partner" / production-partner info if shown (quote it) |
listing review count and shop sales count if shown | processing time if shown.

OUTPUT — three plain-text blocks I can copy, using " | " as separator, one row per line:
BLOCK 1 (keyword summary): keyword | result count | filters active | cards read
BLOCK 2 (all search cards): the STEP 1 rows
BLOCK 3 (detail pages): the STEP 2 rows
Do not summarize or compute medians — I will compute them. Just record raw values exactly as shown.
```
