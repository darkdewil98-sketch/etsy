# Claude in Chrome prompt — round 6: bookish stickers with the digital-downloads filter applied

Why: in round 5 the "bookish stickers" search ran with NO filter chip, so digital downloads were mixed
into the 48 cards (median $3.50). That figure cannot be used as a physical-sticker price, so the
opportunity is currently UNRESOLVED. This re-run isolates physical stickers and records pack size,
which is what actually drives sticker margin.

```
You are a READ-ONLY Etsy research assistant in my logged-in account.
Do NOT favorite, add to cart, buy, message, create/edit listings, change settings, or spend money.
Never invent numbers. If a value is not visible, write NV.
Review counts on Etsy search cards are SHOP-level ratings, not sales — never convert them to sales.

SETUP
- Open https://www.etsy.com/search?q=bookish+stickers
- Keep sort = Most relevant, currency USD, ship-to United States.
- IMPORTANT: this search does NOT apply "Exclude digital downloads" by default. Apply it yourself
  (filter panel -> Special offers / Item type -> exclude digital / instant download), then confirm the
  active chip and record its exact label. Record the result count before and after applying it.
- Repeat the same for these keywords: "reading stickers", "book sticker pack", "kindle stickers".
- Ignore any third-party browser-extension overlays; record only what Etsy itself shows.

STEP 1 — SEARCH CARDS (48 per keyword, after the filter is applied)
One row per card:
keyword | position | ad? (Y/N) | shop | title (first 80 chars) | price shown | original price if struck through |
% off | free shipping badge (Y/N) | shop rating | shop review count | badges (Bestseller / Popular now / Star Seller) |
pack size from the title (single / 2 / 5 / 10 / 20 / 50 / sheet / "NV") | still digital? (Y/N — say Y if the
title or card says digital, download, PNG, SVG, printable, Cricut)

STEP 2 — LISTING DETAIL (first 5 NON-AD physical listings per keyword)
keyword | shop | listing URL | default price | every quantity/pack option with its price as shown |
sticker size options with prices | US shipping cost (and cost for each additional item if shown) |
personalization box Y/N | production partner text if shown | listing review count ; shop sales |
is it die-cut / kiss-cut / sheet.

OUTPUT — plain text, " | " separators, one row per line:
BLOCK 1 (per keyword): keyword | result count before filter | result count after filter | exact filter chip label | cards read
BLOCK 2 (cards)
BLOCK 3 (detail pages)
Do not summarize or compute medians — record raw values only.
```
