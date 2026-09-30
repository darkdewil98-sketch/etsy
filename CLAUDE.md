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
  verified competitor prices, supplier scenarios, Top 10, Top 5 clusters, copyable table).
  Pipeline (run from repo root, in order): analyze_prices.py -> analyze_prices_round5.py -> pillow_16in.py
  -> supplier_scenarios.py -> score_opportunities.py -> build_report.py.
  **Research is complete (2026-09-28): 4 TEST NOW, 7 REJECT, 17 RESEARCH MORE.** All demand, cost and
  competitor-price inputs are verified from live pages; see the report's "Araştırmanın durumu" section.
  Data notes: ornaments are costed on the verified SwiftPOD 2-side price ($6.57 + $4.79 Economy shipping);
  "PET PILLOW" is a live registration, so the pillow opportunity leads with "custom dog pillow";
  card review counts are SHOP-level; the "Hide ads" numbers in the round-1 file came from a browser
  extension and are unused. bookish stickers is closed as UNRESOLVED by the user's decision — that search
  ran unfiltered and mixes in digital downloads; `chrome_prompt_round6_stickers.md` would resolve it.
- Printify's public catalog pages render in headless Chromium (after adding the CCR proxy CA to
  ~/.pki/nssdb with certutil); they show 'From USD' costs, Premium costs and US shipping per provider.
