"""Score POD opportunities from the 2026-09-25 Marketplace Insights export.

Data-driven parts (Demand, Competition, Buyer intent, Margin, penalties) are computed from:
  - data/insights_keyword_universe.csv  (Etsy Marketplace Insights, last 30 days, verbatim values)
  - Printful catalog/shipping costs verified 2026-09-25 (see README section 2)
Judgment parts (Personalization, Expansion, Thumbnail, Q4 timing) are analyst ratings and are
labelled as such in the output. The score is a research-priority score, NOT a sales probability.

Run from repo root: python research/2026-09-25/scripts/score_opportunities.py
"""
import csv

UNIVERSE = "research/2026-09-25/data/insights_keyword_universe.csv"
OUT_CSV = "research/2026-09-25/data/opportunities_scored.csv"
OUT_MD = "research/2026-09-25/opportunities.md"

# Printful: base price (standard print included) + US first-item shipping, USD, verified 2026-09-25.
COST = {
    "ceramic2": ("Printful Ceramic Ornament, 2-side (#900)", 7.73, 5.89),
    "ceramic1": ("Printful Ceramic Ornament, circle (#881)", 6.34, 5.49),
    "wood_orn": ("Printful Wooden Ornament (#634)", 8.37, 5.19),
    "stocking": ("Printful Rustic Christmas Stocking (#1428)", 17.17, 7.79),
    "pillow": ("Printful Custom Shaped Pillow 16x16 (#743)", 16.60, 6.19),
    "mug11": ("Printful White Glossy Mug 11oz (#19)", 6.07, 6.69),
    "mug15": ("Printful White Glossy Mug 15oz (#19)", 8.11, 7.29),
    "sweat": ("Printful Gildan 18000 crewneck, front print (#145)", 19.17, 8.79),
    "sweat_sleeve": ("Printful Gildan 18000 + sleeve print (#145)", 25.12, 8.79),
    "sweat_emb": ("Printful Gildan 18000, embroidery left chest (#145)", 22.12, 8.79),
    "tee": ("Printful Bella+Canvas 3001 tee (#71)", 11.92, 4.95),
    "canvas10": ("Printful Canvas 10x10 (#3)", 16.83, 6.79),
    "tote": ("Printful Eco Tote EC8000 (#367)", 15.87, 4.69),
    "sticker": ("Printful Kiss-cut sticker 3x3 (#358)", 2.34, 4.49),
    "treeskirt": ("Printful Christmas Tree Skirt (#1427)", 43.95, 7.79),
    "bookmark": ("Bookmark (no Printful product; supplier NOT VERIFIED)", None, None),
}
FEE_PCT, FEE_FIX = 0.095, 0.45  # 6.5% transaction + 3% processing; $0.25 + $0.20 listing (third-party reported)

def need_price(cost, contrib):
    return round((contrib + cost + FEE_FIX) / (1 - FEE_PCT), 2)

# id, primary keyword, secondary keywords, product key, buyer, occasion, personalization method,
# pers(0-10), expansion(0-10), thumb(0-5), q4(0-5), seasonality, peak_risk, evergreen, trend label,
# IP notes, competitor evidence, design direction, why-niche, risks
C = [
 ("engagement ornament", ["personalized engagement ornament", "first christmas engaged ornament", "engaged ornament", "engaged christmas ornament"],
  "ceramic2", "Newly engaged couples; friends/family buying for them", "Christmas 2026 (first holiday engaged), engagement parties",
  "Both names + engagement date/year + optional city", 10, 9, 5, 5, "HIGH", "MEDIUM", "MEDIUM", "EARLY SIGNAL",
  "No live exact USPTO mark for 'engaged', 'just engaged', 'our first christmas engaged' in product classes. Avoid 'JUST MARRIED' on apparel (Reg. 2932679, IC 025).",
  "NOT VERIFIED (competitor SERP for this keyword not captured).",
  "Typography-led ceramic disc: two first names joined by a hand-drawn ring line, 'Engaged' + year, date on back. Offer 3-4 colourways (champagne, sage, navy, blush) as variations.",
  "Conversion label is High/Very high across the engaged-ornament family, and listings are 14k–52k vs 140k for generic 'personalized ornament'.",
  ["Strongly Q4-peaked; engagement demand also spikes Dec-Feb (proposal season) which helps sell-through.", "Crowded by laser-engraved wood; ceramic print must look premium in photos."]),
 ("first christmas married ornament", ["newlywed ornament", "mr and mrs ornament", "personalized wedding ornament", "married ornament"],
  "ceramic2", "Newlyweds (2026 weddings); parents, wedding guests", "First Christmas as married couple",
  "Couple surname/first names + wedding date + 'first Christmas married 2026'", 10, 9, 5, 5, "HIGH", "HIGH", "LOW", "VERIFIED CURRENT TREND",
  "No live exact mark for 'first christmas as mr & mrs', 'newlyweds' in product classes. 'Mr & Mrs': 20 live marks contain it, none exact in product classes — still avoid it as a standalone design text.",
  "NOT VERIFIED.",
  "Minimal 'est.' style layout: surname large, 'Married 2026' small caps, wedding date; back side with venue city or vows line typed by buyer.",
  "Insights shows +11.4% period growth with High conversion; 'newlywed ornament' has one of the best ratios in the ornament family (4.6k / 16.5k).",
  ["Very date-bound ('2026'): unsold designs need a year swap for 2027.", "Wedding-season overlap: demand is highest Oct–Dec only."]),
 ("personalized christmas stocking", ["christmas stocking personalized", "personalized stocking", "embroidered christmas stocking"],
  "stocking", "Parents building a family stocking set; grandparents", "Christmas decorating (Oct–Dec)",
  "Family member name per stocking, optional year; sold as individual stockings so families buy 3–6", 10, 8, 4, 5, "HIGH", "HIGH", "LOW", "VERIFIED CURRENT TREND",
  "Avoid 'MERRY & BRIGHT' (reg. in IC 024/025), 'HOLLY JOLLY' (IC 025/016/028), standalone 'JOY'/'BELIEVE'. Name-only designs are clear.",
  "NOT VERIFIED. Related terms show embroidered/needlepoint/quilted formats dominate the category.",
  "Rustic canvas-look print with oversized name in modern script + small woodland/snowflake icon; matching set of 6 icons so a family can mix and match.",
  "+30.3% period growth and Very high conversion; multi-unit family orders raise AOV (Printful extra-item shipping is +$3.75).",
  ["Premium segment is embroidered/needlepoint; a printed stocking must compete on design and price.", "Printful stocking cost $24.96 incl. shipping leaves a thin margin unless sold ≥ ~$39."]),
 ("dog christmas stocking", ["cat christmas stocking", "pet stocking"],
  "stocking", "Dog owners (and cat owners)", "Christmas", "Pet name + breed-specific illustration or pet photo", 10, 8, 4, 5, "HIGH", "HIGH", "LOW", "EARLY SIGNAL",
  "Avoid 'PAWSOME' (reg. IC 016/028), 'FURBABY' (IC 021) wording.",
  "NOT VERIFIED.",
  "Breed-line-art series (start with top 10 breeds) + pet name; option to upload a photo for a cut-out portrait on the cuff area.",
  "Typical conversion with 27k listings — much smaller field than generic stockings (58k–356k).",
  ["Breed art must be drawn originally (no traced stock art)."]),
 ("custom pet pillow", ["custom dog pillow", "custom cat pillow"],
  "pillow", "Pet owners; gift-givers for pet owners; pet memorial buyers", "Christmas, birthdays, pet memorial",
  "Buyer uploads pet photo → cut-out shaped pillow; optional name on back", 10, 8, 5, 3, "MEDIUM", "LOW", "HIGH", "EVERGREEN",
  "Avoid 'FUR BABY' (pending IC 020 — covers cushions/pillows) and 'FOREVER IN MY HEART' (Reg. 7359901, IC 020).",
  "NOT VERIFIED.",
  "Photo cut-out with clean white border; add a subtle printed name/paw-date on the reverse. Thumbnail: pillow next to the real-pet photo.",
  "All three variants carry a Very high conversion label and 9.5k–18k listings — among the smallest fields in the dataset with this intent level.",
  ["Photo quality from buyers varies; needs a clear photo-guide and manual cut-out time per order.", "Uses buyer photos: buyer must have rights; seller's value is the editing/design (disclose production partner)."]),
 ("baby's first christmas ornament", ["first christmas ornament", "personalized baby ornament", "new baby ornament", "newborn christmas ornament"],
  "ceramic2", "New parents; grandparents; baby-shower guests", "Baby's first Christmas 2026",
  "Baby name + birth date/weight + year; optional photo on back", 10, 9, 5, 5, "HIGH", "HIGH", "MEDIUM", "EARLY SIGNAL",
  "Use 'Baby's First Christmas' — 'MY FIRST CHRISTMAS' is registered (Reg. 4530374 IC 025 baby clothing; Reg. 2040424 IC 028 stuffed toys).",
  "NOT VERIFIED.",
  "Soft watercolour motif per month-of-birth (birth flower) + name + stats; back side photo. Blue/pink/neutral variations.",
  "High conversion, +4.9% growth; 'first christmas ornament' alone has 19.6k searches with a 0.165 ratio.",
  ["Large, mature category (89k listings on the primary term).", "Q4-only peak."]),
 ("baptism ornament", ["christening ornament", "first holy communion ornament"],
  "ceramic2", "Godparents, grandparents", "Baptism/christening, first Christmas", "Child name + baptism date + church/city", 9, 7, 4, 3, "MEDIUM", "LOW", "HIGH", "EVERGREEN",
  "No specific marks found; keep religious imagery generic (dove, cross, olive branch) — no church logos.",
  "NOT VERIFIED.",
  "Minimal line-art dove or olive branch, name in serif caps, date; pairs with godparent gift bundles.",
  "Typical conversion; year-round occasion keeps it selling after Q4.",
  ["Smaller volume (2.9k); needs variety across denominations without using protected symbols/logos."]),
 ("pregnancy ornament", ["pregnancy announcement ornament", "baby announcement ornament"],
  "ceramic2", "Expecting parents announcing to grandparents", "Christmas pregnancy reveal", "Due date + 'Grandma/Grandpa' names + baby nickname", 10, 7, 4, 5, "HIGH", "HIGH", "LOW", "EARLY SIGNAL",
  "No specific marks found for 'pregnancy announcement ornament'.",
  "NOT VERIFIED.",
  "Reveal-style ornament: 'Coming [month] 2027' with tiny ultrasound-frame graphic; variations for grandparents, aunts, siblings.",
  "Ties into the new-grandma cluster (new grandma gift 4.3k searches) and Christmas reveals.",
  ["Low conversion label (L) on primary; VL on announcement variant."]),
 ("family of 4 ornament", ["personalized family ornament", "family christmas ornament", "family name ornament"],
  "ceramic2", "Parents; grandparents buying for adult children", "Christmas", "Each family member's name (+ pets) with simple figures; 'family of 3/4/5/6' variations", 10, 10, 5, 5, "HIGH", "HIGH", "MEDIUM", "EARLY SIGNAL",
  "No live mark for 'family of four'.",
  "NOT VERIFIED.",
  "Illustrated family-figure builder (hair/skin/pets choices) is the common format; differentiate with a typographic 'family name + names list' version and a line-art version.",
  "Micro keyword 'family of 4 ornament' shows a 0.157 ratio with Typical conversion (1.7k / 10.8k) vs 144k listings on 'family christmas ornament'.",
  ["Figure-builder listings are labour-intensive per order.", "Generic 'family christmas ornament' is crowded (144k)."]),
 ("new house ornament", ["new home ornament", "first christmas in new home ornament", "first house ornament", "our first home ornament"],
  "ceramic2", "New homeowners; friends; real-estate agents", "First Christmas in new home; housewarming", "House illustration from buyer photo or house-style template + address/family name + year", 10, 9, 5, 5, "HIGH", "MEDIUM", "HIGH", "EARLY SIGNAL",
  "Avoid 'HOME SWEET HOME' (Reg. 7006924, IC 021). No live mark for 'our first home' / 'first christmas in our new home'.",
  "Related 'client gift' SERP (Table B) is dominated by watercolor house-portrait ornaments: median $20.99, top shop LoveSuna shows 62.7k reviews / 371.7k shop sales.",
  "Line-art house from photo (1-colour on white ceramic) — faster than watercolor, distinct from the dominant watercolor look.",
  "High conversion on 'new house ornament' with 19.8k listings, and the same product serves the housewarming and closing-gift clusters.",
  ["House drawings from photos take time; needs a template-based faster tier.", "Dominated at the top by very large shops (verified on 'client gift')."]),
 ("client gift", ["realtor closing gift", "closing gift", "new homeowner gift"],
  "ceramic2", "Real-estate agents, loan officers, small businesses (B2B)", "Closings; year-end client appreciation", "Client house + family name + closing date; agent's own name/business on back (no third-party logos)", 10, 9, 4, 5, "MEDIUM", "MEDIUM", "HIGH", "EARLY SIGNAL",
  "Do NOT use the word 'REALTOR' in designs (collective mark, Reg. 4583156 IC 025 / 4583155 IC 014). Use 'real estate agent'/'closing gift'.",
  "VERIFIED (Table B): 36,810 search results; price $2.03–$80.99, median $20.99; 96% personalized (title proxy); 28/48 cards show 1k+ reviews; Bestseller 14, Star Seller 34. Examples: LoveSuna $12.48 (62.7k reviews, 371.7k sales); HeldDearCo $11.74 (840, 8k); SNUGAMATE $25.12 (6.4k, 36.1k); Alishannondesigns $11.99 (1.1k, 8k); SeedlingGoodsLLC $9.99 (186, 1.2k).",
  "Agent-branded bulk pack (5/10/25 ornaments) with a clean line-art house style; year-end 'thank you' client-appreciation version.",
  "Best ratio of any POD-able keyword (0.754: 15.9k searches vs 21.1k listings); B2B buyers order multiples.",
  ["Very low conversion label (VL) and heavy concentration of 1k+ review shops on page one (verified).", "Verified median price $20.99 vs $13.62 cost → about $4.9 contribution at median; bulk pricing needed."]),
 ("dog memorial gift", ["pet memorial gift", "pet remembrance gift", "dog remembrance gift"],
  "canvas10", "Grieving dog owners; friends sending sympathy gifts", "Pet loss (year-round), memorial Christmas", "Pet photo portrait + name + years", 10, 9, 4, 3, "LOW", "LOW", "HIGH", "EVERGREEN",
  "Avoid 'RAINBOW BRIDGE' (Reg. 8198078 IC 028; Reg. 2725281 IC 020), 'FOREVER IN MY HEART' (IC 020), 'ALWAYS IN MY HEART' (IC 014/016).",
  "NOT VERIFIED.",
  "Soft painted-style portrait from photo on canvas with name + dates; companion ornament and pillow versions for the same order.",
  "Largest-volume keyword in the pet cluster (61.4k searches) with a High conversion label; evergreen demand.",
  ["428k listings — very crowded head term; winning needs long-tail listing titles (breed + memorial)."]),
 ("cat memorial ornament", ["cat memorial gift", "cat remembrance gift", "pet memorial ornament"],
  "ceramic2", "Cat owners after loss; friends", "Pet loss; memorial Christmas", "Cat photo or breed art + name + dates", 10, 8, 4, 4, "MEDIUM", "LOW", "HIGH", "EVERGREEN",
  "Same memorial phrase exclusions as dog memorial.",
  "NOT VERIFIED.",
  "Minimal cat silhouette in cat's own coat colours chosen by buyer + name + dates; photo option on back.",
  "Cat-specific memorial ornaments have 46.7k listings vs 115.7k for dog; related 'cat memorial gift' has 14.1k searches.",
  ["Low conversion label (L) on the ornament term."]),
 ("auntie mug", ["aunt mug", "auntie gifts", "gift for auntie", "auntie birthday gift"],
  "mug15", "Nieces/nephews (often parents buying for kids); siblings", "Christmas, birthdays, pregnancy announcement ('promoted to auntie')", "Nieces'/nephews' names + 'Auntie' + est. year", 9, 9, 5, 4, "LOW", "LOW", "HIGH", "EVERGREEN",
  "Avoid 'COOL AUNT' (Reg. 7232375, IC 025). No live exact marks for 'auntie', 'best auntie', 'auntie est', 'promoted to auntie' in product classes.",
  "NOT VERIFIED.",
  "Typography-first mug: 'Auntie' in bold serif + kids' names in a stacked list; variants 'promoted to', 'est. 20XX', photo version.",
  "Very high conversion with only 7.9k listings (0.228 ratio); 'auntie gifts' adds 8.1k searches with a 0.190 ratio.",
  ["Mug price ceiling is typically low; 15oz mug cost is $15.40."]),
 ("auntie shirt", ["aunt shirt", "new aunt gift", "promoted to aunt shirt"],
  "tee", "Aunts / new aunts; siblings buying", "Pregnancy announcements, Christmas, birthdays", "Kids' names on sleeve or under 'Auntie'", 9, 9, 4, 3, "LOW", "LOW", "HIGH", "EVERGREEN",
  "Avoid 'COOL AUNT' (IC 025 registered).",
  "NOT VERIFIED.",
  "Clean 'Auntie' wordmark with names on sleeve; matching 'Uncle' tee as cross-sell.",
  "High conversion on 'auntie shirt' (3.8k searches); pairs with the auntie-mug niche.",
  ["45.7k listings — medium competition.", "Apparel sizing returns."]),
 ("uncle mug", ["uncle birthday gift", "gift for uncle", "new uncle gift"],
  "mug15", "Nieces/nephews; siblings", "Christmas, birthdays", "Kids' names + 'Uncle'", 9, 7, 4, 4, "LOW", "LOW", "HIGH", "EVERGREEN",
  "No specific marks found.",
  "NOT VERIFIED.",
  "Mirror of the auntie line with a more rugged palette; 'uncle birthday gift' angle.",
  "Only 8.6k listings for uncle mug with High conversion; 'uncle birthday gift' shows Very high conversion.",
  ["Small volume (591 searches)."]),
 ("personalized grandma sweatshirt", ["custom grandma sweatshirt", "personalized grandma shirt", "grandma embroidered sweatshirt", "grandma sweatshirt with names"],
  "sweat_sleeve", "Adult children/grandchildren buying for grandma", "Christmas, Mother's Day, birthdays", "Grandkids' names on sleeve + 'Grandma' + est. year", 10, 9, 4, 5, "MEDIUM", "LOW", "HIGH", "EARLY SIGNAL",
  "Use 'Grandma' — avoid standalone 'MAMA' (Reg. 8387670, IC 025, 2026-08-11), 'NANA'/'MIMI' (pending IC 025), 'GIGI', 'GLAMMA'.",
  "NOT VERIFIED.",
  "Embroidered-look 'Grandma' with grandkids' names down the sleeve (Printful sleeve print +$5.95); embroidery upgrade variation.",
  "Very high conversion across the grandma-sweatshirt terms; seed 'grandma sweatshirt with names' grew +53.8%.",
  ["Low search volume per term (226–763).", "Sleeve print raises cost to $33.91."]),
 ("new grandma mug", ["new grandma gift", "new grandparent gift", "custom grandpa mug", "new grandpa gift"],
  "mug15", "Expecting parents announcing; friends of new grandparents", "Pregnancy reveal, Christmas, birth", "Baby's due date/name + 'Grandma est. 2026/2027'", 9, 8, 4, 4, "LOW", "LOW", "HIGH", "EVERGREEN",
  "Avoid NANA/MIMI/GIGI/GLAMMA as standalone design text.",
  "NOT VERIFIED.",
  "'Promoted to Grandma' reveal mug with due-date; matching grandpa version.",
  "Very high conversion on 'new grandma mug' and 'custom grandpa mug'; 'new grandma gift' has 4.3k searches.",
  ["Small volume per mug term (262–405)."]),
 ("custom dog shirt", ["custom pet sweatshirt", "custom dog hoodie", "dog mom gift"],
  "tee", "Dog owners", "Christmas, birthdays, everyday", "Pet photo → illustrated face + pet name", 10, 9, 5, 3, "LOW", "LOW", "HIGH", "EVERGREEN",
  "Avoid 'PAWSOME', 'FURBABY'. 'Dog mom' has 8 live marks containing it — avoid 'DOG MOM' as the main design text.",
  "NOT VERIFIED.",
  "Minimal line-portrait of the pet + name in small caps; sweatshirt/hoodie upsell variations.",
  "Very high conversion with 7.3k searches; the photo-to-illustration step is the differentiator.",
  ["136.6k listings — crowded.", "Illustration labour per order."]),
 ("custom embroidered sweatshirt", ["embroidered sweatshirt custom", "custom name embroidery", "grandma embroidered sweatshirt"],
  "sweat_emb", "Women 25-55 buying for self/family", "Christmas, birthdays", "Name/initials/kids' names embroidered left chest", 9, 9, 4, 4, "LOW", "LOW", "HIGH", "EVERGREEN",
  "Personal names only; avoid MAMA standalone.",
  "NOT VERIFIED.",
  "Tonal embroidery on garment-dyed look colours; mini-icon + name; seasonal colour drops.",
  "11k searches with Typical conversion and a 0.099 ratio; Printful embroidery costs +$2.95 over DTG.",
  ["111k listings; embroidery digitisation quality matters."]),
 ("family christmas shirts", ["matching family christmas shirts", "christmas family shirts"],
  "tee", "Parents organising family photos/events", "Christmas photos, parties", "Family surname + year; each member role/name", 9, 8, 5, 5, "HIGH", "HIGH", "LOW", "VERIFIED CURRENT TREND",
  "Avoid 'HOLLY JOLLY' (IC 025), standalone 'JOY'/'BELIEVE' (IC 025), 'MERRY & BRIGHT' (pajamas IC 025).",
  "NOT VERIFIED.",
  "Coordinated set: same design, different role/name per shirt; buyer adds each size as a separate line.",
  "+17.5% growth; multi-unit orders (4–8 shirts) lift AOV; tee cost $16.87 + $2.20 per extra item.",
  ["121k listings; highly seasonal (Dec)."]),
 ("turkey trot shirt", ["thanksgiving shirt", "thanksgiving family shirts"],
  "tee", "Families/teams running Thanksgiving 5K races", "Thanksgiving (Nov 26, 2026)", "Team/family name + year + race city", 9, 6, 4, 4, "HIGH", "HIGH", "LOW", "VERIFIED CURRENT TREND",
  "No live exact mark for 'turkey trot' or 'gobble till you wobble' in product classes; still use original phrases. Avoid 'GIVE THANKS' (IC 025) and 'GRATEFUL' (IC 025).",
  "NOT VERIFIED.",
  "Team-shirt layout: '[Family] Turkey Trot 2026' + runner turkey illustration; group-order friendly.",
  "Only 5.4k listings (0.163 ratio); parent term 'thanksgiving shirt' grew +36.4%.",
  ["Very Low conversion label; hard deadline ~Nov 15 for POD delivery.", "Small volume (878)."]),
 ("teacher thank you gift", ["personalized teacher gift", "teacher tote bag", "teacher christmas gift"],
  "tote", "Parents/room parents buying for teachers", "Christmas, end of year, Teacher Appreciation (May)", "Teacher name + class/grade + student names", 9, 8, 4, 4, "MEDIUM", "LOW", "HIGH", "EVERGREEN",
  "No specific marks found for 'teacher thank you'.",
  "NOT VERIFIED.",
  "Tote with teacher's name + class signature-style student names; mug version.",
  "Very high conversion on 'teacher thank you gift' (3k searches); 'teacher christmas gift' grew +20.2%.",
  ["Teacher gift budgets are often low.", "Personalization with many student names is error-prone."]),
 ("retirement gifts for women", ["retirement mug", "retirement coffee mug", "nurse retirement gift", "retirement ornament"],
  "mug15", "Coworkers, adult children", "Retirement parties (year-round), Christmas", "Name + career years + profession icon", 8, 9, 4, 3, "LOW", "LOW", "HIGH", "EVERGREEN",
  "Avoid 'OFFICIALLY RETIRED' (Reg. 5201467, IC 014/016/021/025), 'RETIRED' standalone (pending IC 025), 'HAPPY RETIREMENT' on blankets (Reg. 7173581, IC 024).",
  "Related 'leaving work gifts' SERP (Table B) is dominated by funny-label candles/mugs at median $12.39 — below a POD mug's $12.76 cost.",
  "Profession-specific retirement mugs (nurse, teacher, office) with career-years timeline; avoid the 'funny candle' price segment.",
  "15.5k searches with a 0.321 ratio on 'retirement gifts for women'; 'nurse retirement gift' shows High conversion.",
  ["Verified low price anchor ($12.39 median) in the adjacent leaving-work segment.", "Conversion label only Low on the head term."]),
 ("bookish stickers", ["book lover gift", "gifts for book lovers", "reading journal"],
  "sticker", "Readers / book-club members", "Stocking stuffers, everyday", "Reader name or reading-goal sticker pack", 4, 8, 4, 4, "LOW", "LOW", "HIGH", "EVERGREEN",
  "Use 'bookish' only in tags, not as design text (BOOKISH pending IC 028; 9 live marks contain it). Book titles/characters are prohibited IP.",
  "NOT VERIFIED.",
  "Original reading-life sticker packs (tbr, annotation tabs aesthetic) — no book titles or quotes.",
  "Typical conversion, 7.5k searches, 0.119 ratio; stickers ship cheaply (+$0.05 extra item).",
  ["Low price point; 'book lover gift' shows an unusual -49.5% swing (98.4k searches) — treat head-term volume with caution."]),
 ("christmas tree skirt", ["personalized tree skirt", "quilted tree skirt"],
  "treeskirt", "Homeowners decorating", "Christmas decorating", "Family name + established year", 7, 6, 4, 5, "HIGH", "HIGH", "LOW", "EARLY SIGNAL",
  "Avoid 'MERRY & BRIGHT', 'HOLLY JOLLY', standalone 'JOY'/'BELIEVE'.",
  "NOT VERIFIED.",
  "Monogram/family-name skirt coordinated with the stocking line.",
  "0.497 ratio (7.2k searches vs 14.5k listings) — one of the widest gaps found.",
  ["Very low conversion label.", "Printful cost $51.74 incl. shipping requires a high price."]),
 ("nurse sweatshirt", ["nurse shirt", "nurse gift", "new nurse gift"],
  "sweat", "Nurses; family/friends; nursing students", "Christmas, Nurses Week (May), graduation", "Name + credential (RN/LPN/NP) + specialty", 8, 9, 4, 3, "LOW", "LOW", "HIGH", "EVERGREEN",
  "No live exact marks found for 'nurse life'. Do not use hospital/health-system names or logos; no medical claims.",
  "NOT VERIFIED.",
  "Specialty-specific designs (ER, NICU, L&D, oncology) with credential personalization instead of generic 'nurse' slogans.",
  "17.1k searches with a 0.106 ratio; specialty long-tails offer a less crowded entry.",
  ["160.8k listings; Low conversion label on the head term."]),
 ("personalized bookmark", ["name bookmark", "custom name bookmark", "photo bookmark"],
  "bookmark", "Readers; gift-givers", "Stocking stuffers, teacher gifts", "Name/initial/photo", 9, 7, 4, 4, "LOW", "LOW", "HIGH", "EVERGREEN",
  "No specific marks found.", "NOT VERIFIED.",
  "Printed name bookmark with tassel; teacher and grandparent variants.",
  "Very high conversion, 6.5k searches, 0.190 ratio.",
  ["SUPPLIER COST NOT VERIFIED — Printful has no bookmark product; another POD provider must be verified first."]),
]

# Penalties backed by verified Table B evidence (keyword -> (points, reason)).
VERIFIED_PENALTY = {
    "client gift": (-10, "extreme competition verified (28/48 page-one cards show 1k+ reviews) -10"),
}

# Verified competitor prices (data/price_analysis.csv from the 14-keyword Etsy snapshot, 2026-09-25).
# Contribution = (price + observed US shipping) * (1 - 9.5%) - $0.45 - Printful cost.
PRICE_FILE = "research/2026-09-25/data/price_analysis.csv"
PRICE_KW = {  # opportunity -> snapshot keywords used as evidence (first one drives the margin score)
    "engagement ornament": ["engagement ornament", "personalized engagement ornament"],
    "first christmas married ornament": ["first christmas married ornament", "newlywed ornament"],
    "personalized christmas stocking": ["personalized christmas stocking"],
    "dog christmas stocking": ["dog christmas stocking"],
    "auntie mug": ["auntie mug"],
    "custom pet pillow": ["custom pet pillow", "custom dog pillow"],
    "baby's first christmas ornament": ["baby's first christmas ornament"],
    "new house ornament": ["new house ornament"],
    "retirement gifts for women": ["retirement gifts for women"],
    "family of 4 ornament": ["family of 4 ornament"],
    "teacher thank you gift": ["teacher thank you gift"],
}
# Card prices for pet pillows are "from" prices of keychain/mini sizes; size-matched 16in price is not visible.
PRICE_UNRESOLVED = {"custom pet pillow": "card prices start at keychain/mini sizes (detail ranges $9.90–$38.99 up to $144.50); "
                                         "a size-matched 16in price was not recorded -> margin unresolved"}
def pts_margin_verified(c_med, c_p75):
    """Points from verified contribution at median (and P75) buyer price incl. shipping."""
    base = 15 if c_med >= 10 else 12 if c_med >= 7 else 8 if c_med >= 4 else 4 if c_med >= 1 else 0
    return min(15, base + (2 if c_p75 >= 10 else 0))
def pts_verified_dominance(n1k):
    return -10 if n1k >= 38 else -5 if n1k >= 30 else 0

def pts_demand(s): return 20 if s >= 10000 else 17 if s >= 5000 else 14 if s >= 2000 else 11 if s >= 1000 else 8 if s >= 500 else 5
def pts_comp(r): return 20 if r >= .2 else 17 if r >= .15 else 14 if r >= .1 else 11 if r >= .07 else 8 if r >= .05 else 5
INTENT = {"VH": 15, "H": 12, "T": 9, "L": 6, "VL": 3}
def pts_margin(c): return 3 if c is None else 13 if c <= 15 else 11 if c <= 25 else 8 if c <= 35 else 5
def comp_label(r, li): return "HIGH" if (li >= 100000 or r < .05) else "LOW" if (r >= .15 and li < 60000) else "MEDIUM"
def access(r, li, conv):
    if r >= .15 and li < 60000 and conv in ("VH", "H", "T"): return "HIGH"
    if li >= 100000 or r < .03: return "LOW"
    return "MEDIUM"

U = {r["keyword"]: r for r in csv.DictReader(open(UNIVERSE))}
P = {r["keyword"]: r for r in csv.DictReader(open(PRICE_FILE))}
rows = []
for (kw, sec, pk, buyer, occ, pmeth, pers, exp, thumb, q4, season, peak, ever, trend, ip, comp_ev, design, why, risks) in C:
    u = U[kw]
    s, li, ratio, conv = float(u["searches_n"]), float(u["listings_n"]), float(u["ratio"]), u["conv"]
    pname, base, ship = COST[pk]
    cost = round(base + ship, 2) if base is not None else None
    d, cpt, it, mg = pts_demand(s), pts_comp(ratio), INTENT[conv], pts_margin(cost)
    pen = (-10 if li >= 100000 else 0) + (-10 if (cost is None or cost > 40) else 0) + VERIFIED_PENALTY.get(kw, (0, ""))[0]
    price_ev, price_range, c_med, c_p75, dom_pen = "", "NOT VERIFIED", None, None, 0
    if kw in PRICE_KW:
        pa = [P[k] for k in PRICE_KW[kw]]
        a = pa[0]
        ship = 0.0 if a["detail_ship_median"] == "all free" else float(a["detail_ship_median"])
        c_med, c_p75 = float(a["contrib_with_ship_at_median"]), float(a["contrib_at_p75_with_ship"])
        price_range = f'${float(a["p25"]):.2f}–${float(a["p75"]):.2f} (P25–P75), median ${float(a["median"]):.2f}, full ${float(a["min"]):.2f}–${float(a["max"]):.2f}; typical US shipping ${ship:.2f}'
        price_ev = "; ".join(
            f'"{x["keyword"]}": {x["cards"]} cards, median ${float(x["median"]):.2f}, {x["on_sale_pct"]}% shown on sale, {x["free_ship_cards_pct"]}% free-shipping badge, '
            f'{x["reviews_1k_plus"]}/48 cards with 1k+ reviews, Bestseller {x["bestseller"]}, Star Seller {x["star"]}, ads {x["ads"]}; '
            f'detail pages: {x["detail_partner"]}/{x["detail_n"]} disclose a production partner, median US shipping {x["detail_ship_median"]}; materials (title guess): {x["top_materials"]}'
            for x in pa)
        if kw in PRICE_UNRESOLVED:
            mg = 6; c_med = c_p75 = None
        else:
            mg = pts_margin_verified(c_med, c_p75)
        dom_pen = pts_verified_dominance(int(a["reviews_1k_plus"]))
        pen += dom_pen
    elif kw == "client gift":
        # Table B: verified median $20.99; shipping not recorded -> assume buyer pays no shipping (conservative)
        c_med = round(20.99 * 0.905 - FEE_FIX - cost, 2); mg = pts_margin_verified(c_med, 0)
        price_range = "$2.03–$80.99, median $20.99 (Table B, 48 cards); shipping NOT VERIFIED"
    elif not comp_ev.startswith("VERIFIED"):
        mg = min(mg, 8)  # competitor price not verified: cap margin at neutral (conservative)
    score = max(0, d + cpt + it + mg + pers + exp + thumb + q4 + pen)
    if kw in PRICE_KW and kw not in PRICE_UNRESOLVED:
        nxt = "REJECT" if c_p75 < 3 else "TEST NOW" if (c_med >= 4 and c_p75 >= 8 and score >= 70) else "RESEARCH MORE"
    elif kw in PRICE_UNRESOLVED:
        nxt = "RESEARCH MORE"
    else:
        nxt = "RESEARCH MORE"  # no verified competitor prices yet
    secs = []
    for k in sec:
        if k in U: secs.append(f'{k} {U[k]["searches"]}/{U[k]["listings"]} {U[k]["conv"]}')
    rows.append(dict(keyword=kw, searches=u["searches"], listings=u["listings"], chg=u["chg"] or "not shown", ratio=round(ratio, 3), conv=conv,
        product=pname, base=base, ship=ship, cost=cost, price10=need_price(cost, 10) if cost else None, price15=need_price(cost, 15) if cost else None,
        demand=d, comp=cpt, intent=it, margin=mg, pers=pers, exp=exp, thumb=thumb, q4=q4, penalty=pen, score=score,
        competition=comp_label(ratio, li), access=access(ratio, li, conv), buyer=buyer, occasion=occ, pmeth=pmeth,
        season=season, peak=peak, evergreen=ever, trend=trend, ip=ip, comp_ev=comp_ev, design=design, why=why, risks=risks,
        secondary="; ".join(secs) or "-", price_ev=price_ev, price_range=price_range, c_med=c_med, c_p75=c_p75, dom_pen=dom_pen, next=nxt))
rows.sort(key=lambda r: (r["next"] == "REJECT", -r["score"]))
for i, r in enumerate(rows, 1): r["id"] = f"#{i:02d}"

CONVNAME = {"VH": "Very high", "H": "High", "T": "Typical", "L": "Low", "VL": "Very low"}
LVL = lambda n: "VERY HIGH" if n >= 9 else "HIGH" if n >= 7 else "MEDIUM" if n >= 5 else "LOW"
THB = lambda n: "HIGH" if n >= 4 else "MEDIUM" if n >= 3 else "LOW"

with open(OUT_CSV, "w", newline="") as f:
    keys = ["id", "score", "keyword", "product", "searches", "listings", "ratio", "conv", "chg", "competition", "access", "cost", "price10", "price15",
            "c_med", "c_p75", "price_range", "next", "demand", "comp", "intent", "margin", "pers", "exp", "thumb", "q4", "penalty", "dom_pen",
            "trend", "season", "peak", "evergreen", "secondary"]
    w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore"); w.writeheader(); w.writerows(rows)

md = []
for r in rows:
    cost_txt = f'${r["cost"]:.2f} (base ${r["base"]:.2f} + US ship ${r["ship"]:.2f})' if r["cost"] else "SUPPLIER COST NOT VERIFIED"
    if r["c_med"] is not None:
        p75_txt = f'; ${r["c_p75"]:.2f} at P75' if r["c_p75"] is not None else "; P75 not recorded"
        marg = (f'VERIFIED: contribution ${r["c_med"]:.2f} at median buyer price incl. shipping{p75_txt} '
                f'(Printful cost, Etsy fees 6.5% + 3% + $0.45; no ads/discounts). Needed for $10: ${r["price10"]} total incl. shipping.')
    elif r["keyword"] in PRICE_UNRESOLVED:
        marg = "UNRESOLVED — " + PRICE_UNRESOLVED[r["keyword"]] + f'. Needed for $10 contribution: ${r["price10"]} total incl. shipping.'
    elif r["cost"]:
        marg = (f'Competitor price NOT VERIFIED. Needed for $10 contribution: ${r["price10"]}; for $15: ${r["price15"]} (total incl. shipping).')
    else:
        marg = "Not calculated (supplier cost not verified)."
    if r["comp_ev"].startswith("VERIFIED"):
        price_cell = "See competitor evidence (verified)"
    else:
        price_cell = r["price_range"]
    ev = r["comp_ev"] if not r["price_ev"] else (r["price_ev"] if r["comp_ev"].startswith("NOT VERIFIED") else r["comp_ev"] + " | " + r["price_ev"])
    nxt = r["next"]
    md.append(f"""### {r['id']} — {r['keyword']}
**Opportunity Score:** {r['score']}/100 (Demand {r['demand']} · Competition {r['comp']} · Intent {r['intent']} · Margin {r['margin']} · Personalization {r['pers']}* · Expansion {r['exp']}* · Thumbnail {r['thumb']}* · Q4 {r['q4']}* · Penalty {r['penalty']}) — *analyst rating

| Field | Value |
|---|---|
| Product | {r['product']} |
| Primary buyer | {r['buyer']} |
| Occasion | {r['occasion']} |
| Primary keyword | {r['keyword']} |
| Etsy searches | {r['searches']} |
| Etsy listings | {r['listings']} |
| Search period | Last 30 days (Aug 26 – Sep 24, 2026) |
| Period change | {r['chg']} |
| Etsy conversion label | {CONVNAME[r['conv']]} |
| Searches/listings | {r['ratio']} |
| Secondary keywords (searches/listings conv) | {r['secondary']} |
| Trend | {r['trend']} |
| Competition | {r['competition']} |
| New Shop Accessibility | {r['access']} |
| Observed competitor evidence | {ev} |
| Observed POD cost (Printful) | {cost_txt} |
| Selling price range | {price_cell} |
| Margin | {marg} |
| Personalization | YES — {r['pmeth']} |
| Expansion potential | {LVL(r['exp'])} |
| Thumbnail potential | {THB(r['thumb'])} |
| Q4 | {'YES' if r['q4'] >= 4 else 'PARTIAL'} · Seasonality {r['season']} · Peak-risk {r['peak']} · Evergreen {r['evergreen']} |
| IP risk | LOW APPARENT IP RISK (screen only) — {r['ip']} |
| Policy risk | LOW — original seller design, POD partner disclosed; AI DISCLOSURE REQUIRED IF AI-GENERATED FINAL ART IS USED |
| Recommended next step | {nxt} |

**Why:** {r['why']}
**Design direction:** {r['design']}
**Primary risks:** {' / '.join(r['risks'])}{(chr(10) + '**Verified penalty:** ' + VERIFIED_PENALTY[r['keyword']][1]) if r['keyword'] in VERIFIED_PENALTY else ''}
""")
open(OUT_MD, "w").write("\n".join(md))
print(f"{len(rows)} opportunities -> {OUT_CSV}, {OUT_MD}")
for r in rows:
    print(f'{r["id"]} {r["score"]:>3} {r["keyword"]:<34} {r["searches"]:>6}/{r["listings"]:<7} {r["conv"]:>2} cost={r["cost"]} c_med={r["c_med"]} c_p75={r["c_p75"]} mg={r["margin"]} pen={r["penalty"]} {r["next"]}')
