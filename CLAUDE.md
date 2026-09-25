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
- The user is an **Etsy Plus** subscriber: Marketplace Insights keyword searches are unlimited
  (free accounts get 15/week). Don't ration searches to 15; explore related searches in depth.
- The user runs browser research through the Claude in Chrome extension (not connected to cloud
  sessions). Hand them a ready-to-paste prompt — see `research/2026-09-25/chrome_prompt.md` —
  and analyze the tables they paste back.
- Research-only: never create/edit/publish listings, change prices or shop settings, run ads, or
  spend money.

## Research outputs

- `research/<date>/` holds dated research runs (Trends, Printful costs, USPTO screens).
  Latest: `research/2026-09-25/FINAL_REPORT.md` (28 scored opportunities from real Insights data,
  Top 10, Top 5 clusters, copyable table). Re-score with `research/2026-09-25/scripts/score_opportunities.py`.
