# Project notes for Claude

## Etsy Marketplace Insights — ALWAYS use this URL

https://www.etsy.com/your/shops/me/marketplace-insights?ref=seller-platform-mcnav

- This is the user's canonical Marketplace Insights link. Always use it for Etsy keyword
  demand research (searches / listings, last ~30 days). Do not use `/your/shops/me/stats/...`
  variants.
- Marketplace Insights is the primary demand source for this project. Never substitute Google
  Trends or third-party keyword volume for it, and never invent Etsy numbers — write
  "NOT VERIFIED" when a value was not read from a live page.
- The page requires the user's logged-in Etsy seller session. From a cloud container it
  redirects to `/signin` and Etsy returns 403 (bot block on the container IP). In that case, say
  so and ask the user to run the research in their own logged-in browser (e.g. Claude in Chrome)
  or paste screenshots of the results. Do not ask for their Etsy password or 2FA codes.
- Research-only: never create/edit/publish listings, change prices or shop settings, run ads, or
  spend money.

## Research outputs

- `research/<date>/` holds dated research runs (Trends, Printful costs, USPTO screens).
  See `research/2026-09-25/README.md` for the latest, including the 15 recommended Marketplace
  Insights searches.
