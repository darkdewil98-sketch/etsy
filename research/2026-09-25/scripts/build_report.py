"""Build FINAL_REPORT.md from the scored opportunities, the Insights universe and the price analysis.
Run from repo root after score_opportunities.py and analyze_prices.py."""
import csv

D = "research/2026-09-25/"
R = list(csv.DictReader(open(D + "data/opportunities_scored.csv")))
U = {r["keyword"]: r for r in csv.DictReader(open(D + "data/insights_keyword_universe.csv"))}
PA = list(csv.DictReader(open(D + "data/price_analysis.csv")))
CONV = {"VH": "Very high", "H": "High", "T": "Typical", "L": "Low", "VL": "Very low"}

def kw(k):
    u = U[k]
    return f'{k} ({u["searches"]}/{u["listings"]}, {u["conv"]})'

def money(v):
    return f"${float(v):.2f}" if v not in ("", None) else "—"

SC = list(csv.DictReader(open(D + "data/supplier_scenarios.csv")))
REASON = {
    "engagement ornament": "Highest demand + competition score; with Printify/SwiftPOD cost ($9.72) verified contribution $7.91 at median, $14.04 at P75.",
    "custom pet pillow": "Very high conversion, smallest field (18.2k listings); ~16in size-matched median $30.16 total → $4.05, P75 $42.94 → $15.62 (Printful 16in).",
    "auntie mug": "Very high conversion, 7.9k listings; best verified mug cost (Printful 11oz $12.76) leaves $4.14 at median / $6.49 at P75.",
    "new house ornament": "High conversion; SwiftPOD cost gives $8.30 at median / $14.22 at P75; doubles as housewarming/closing gift.",
    "first christmas married ornament": "+11.4% growth, High conversion; SwiftPOD cost gives $7.92 at median / $12.80 at P75.",
    "dog memorial gift": "61.4k searches, High conversion, evergreen; competitor prices not yet collected.",
    "auntie shirt": "High conversion; apparel keeps the auntie niche but prices are not yet verified.",
    "baby's first christmas ornament": "High conversion; SwiftPOD cost gives $7.92 at median / $15.25 at P75 (best P75 in the set).",
    "client gift": "0.754 ratio; verified median $20.99 ($8.83 contribution at SwiftPOD cost) but page one is dominated by 1k+ review shops.",
    "retirement gifts for women": "15.5k searches, 0.321 ratio; Printful 11oz mug gives $4.39 at median / $8.13 at P75.",
    "bookish stickers": "Cheapest product ($6.83); competitor prices not yet collected.",
}

# ---- price findings table
P = ["| Keyword | Median | P25–P75 | Min–Max | On sale | Free-ship badge | 1k+ review cards | Typical US shipping | Detail pages with production partner | POD cost | Contribution at median (+ship) | Contribution at P75 (+ship) |",
     "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for a in PA:
    ship = "free" if a["detail_ship_median"] == "all free" else money(a["detail_ship_median"])
    P.append(f'| {a["keyword"]} | {money(a["median"])} | {money(a["p25"])}–{money(a["p75"])} | {money(a["min"])}–{money(a["max"])} | {a["on_sale_pct"]}% | '
             f'{a["free_ship_cards_pct"]}% | {a["reviews_1k_plus"]}/48 | {ship} | {a["detail_partner"]}/{a["detail_n"]} | {money(a["pod_cost"])} | '
             f'{money(a["contrib_with_ship_at_median"])} | {money(a["contrib_at_p75_with_ship"])} |')
price_table = "\n".join(P)

S2 = ["| Keyword | Supplier (verified 2026-09-25) | Unit cost incl. US ship | Buyer total at median | Contribution at median | Contribution at P75 |", "|---|---|---|---|---|---|"]
for x in SC:
    S2.append(f'| {x["keyword"]} | {x["supplier"]} | {money(x["unit_cost"])} | {money(x["buyer_total_median"])} | {money(x["contrib_median"])} | {money(x["contrib_p75"])} |')
supplier_table = "\n".join(S2)

# ---- top 10 (exclude REJECT)
live = [r for r in R if r["next"] != "REJECT"]
T = ["| Rank | ID | Primary keyword | Product | Searches | Listings | Demand/Competition | New-Shop Access | Margin status | Q4 | IP risk | Next step | Reason for selection |",
     "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for i, r in enumerate(live[:10], 1):
    if r["c_med"]:
        m = f'VERIFIED: {money(r["c_med"])} at median' + (f', {money(r["c_p75"])} at P75' if r["c_p75"] else "")
    elif r["keyword"] == "custom pet pillow":
        m = "UNRESOLVED"
    else:
        m = f'Cost {money(r["cost"])} verified; price NOT VERIFIED' if r["cost"] else "SUPPLIER COST NOT VERIFIED"
    T.append(f'| {i} | {r["id"]} | {r["keyword"]} | {r["product"]} | {r["searches"]} | {r["listings"]} | ratio {r["ratio"]}, conv {CONV[r["conv"]]} ({r["competition"]}) | '
             f'{r["access"]} | {m} | {"YES" if int(r["q4"]) >= 4 else "PARTIAL"} | LOW APPARENT | {r["next"]} | {REASON.get(r["keyword"], "")} |')
top10 = "\n".join(T)

# ---- copy table
C = ["| ID | Score | Keyword | Product | Searches | Listings | Ratio | Conv | Period chg | Competition | New-shop access | POD cost | Verified price range | Contribution median / P75 | Trend | Seasonality | Peak-risk | Evergreen | IP | Next step |",
     "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
TSV = ["\t".join(["id", "score", "keyword", "product", "searches", "listings", "ratio", "conv", "competition", "access", "pod_cost_usd",
                  "verified_price_range", "contrib_median", "contrib_p75", "next_step"])]
for r in R:
    cm = f'{money(r["c_med"])} / {money(r["c_p75"])}' if r["c_med"] else "—"
    C.append(f'| {r["id"]} | {r["score"]} | {r["keyword"]} | {r["product"]} | {r["searches"]} | {r["listings"]} | {r["ratio"]} | {r["conv"]} | {r["chg"]} | '
             f'{r["competition"]} | {r["access"]} | {money(r["cost"]) if r["cost"] else "NOT VERIFIED"} | {r["price_range"]} | {cm} | {r["trend"]} | '
             f'{r["season"]} | {r["peak"]} | {r["evergreen"]} | LOW APPARENT | {r["next"]} |')
    TSV.append("\t".join([r["id"], r["score"], r["keyword"], r["product"], r["searches"], r["listings"], r["ratio"], r["conv"], r["competition"],
                          r["access"], r["cost"] or "NOT VERIFIED", r["price_range"], r["c_med"] or "", r["c_p75"] or "", r["next"]]))
open(D + "data/opportunities_copy.tsv", "w").write("\n".join(TSV) + "\n")
copy = "\n".join(C)

clusters = f"""### Küme 1 — Çift ve kilometre taşı süsleri (talep en güçlü, marj koşullu)
- **Talep neden var:** İlk Noel hediyeleri (nişan, evlilik, bebek, yeni ev). Dönüşüm etiketleri çoğunlukla High/Very high.
- **Ana kelime:** {kw("engagement ornament")}
- **İlgili kelimeler:** {kw("personalized engagement ornament")}; {kw("first christmas married ornament")}; {kw("newlywed ornament")}; {kw("new house ornament")}; {kw("baby's first christmas ornament")}; {kw("first christmas ornament")}; {kw("family of 4 ornament")}; {kw("baptism ornament")}; {kw("pregnancy ornament")}
- **Doğrulanmış fiyat:**
  - Medyan $13.99–$14.41, üstüne tipik $5.99 kargo.
  - Kartların %73–88'i indirimde gösteriliyor ("orijinal" fiyat ~$20–28).
  - İlk sayfada 48 kartın 37–41'i 1k+ yorumlu.
  - Detay sayfalarının çoğu üretim ortağı beyan ediyor: Printway, Inner Circle Prints (Spokane), Ballston Spa NY, Strongsville OH seramik atölyesi.
- **Ekonomi:**
  - Printful ($13.62) ile medyan fiyatta katkı ~$4.
  - Printify/SwiftPOD seramik Round ($4.93 + $4.79 Economy kargo = $9.72, round 3'te varyant olarak doğrulandı) ile medyanda $7.91–$8.30, P75'te $12.80–$15.25.
  - Aynı siparişteki her ek süs: SwiftPOD +$0.49 kargo → medyan fiyatta ek birim katkısı ~$7.04–$7.43.
  - Hediye kutulu varyant $7.06 (+$2.13). Arka yüz baskı ek ücreti hâlâ **NOT VERIFIED**.
  - Printify Premium ($24.99/ay yıllık) ile birim başına $1.05 daha ucuz → başabaş ~24 süs/ay.
- **Özgün listing konsepti tahmini:** 40–60
- **IP:** LOW APPARENT ("MY FIRST CHRISTMAS", "JUST MARRIED", "HOME SWEET HOME", "REALTOR" hariç)
- **Rekabet:** Insights'ta LOW–MEDIUM. Arama sayfasında yerleşik mağazalar baskın.

### Küme 2 — Evcil hayvan fotoğraf ürünleri
- **Ana kelime:** {kw("custom pet pillow")}
- **İlgili kelimeler:** {kw("custom dog pillow")}; {kw("custom cat pillow")}; {kw("dog memorial gift")}; {kw("pet memorial gift")}; {kw("cat memorial ornament")}; {kw("custom dog shirt")}
- **Doğrulanmış fiyat:** Kart fiyatları anahtarlık/mini boylardan başlıyor (medyan $10.43), bu yüzden round 3'te boy eşleştirildi. ~16" boyda 12 listing'in fiyat + kargo toplamı:
  - Medyan $30.16, P25–P75 $27.96–$42.94, aralık $22.19–$52.70.
  - Detay: `data/pillow_16in_prices.csv`.
- **Ekonomi:** Printful 16" özel kesim yastık $22.79 → katkı medyanda $4.05, P75'te $15.62. Yani premium (~$40+) konumlanma gerekiyor. Printify'da ABD'de bu ürün için yerel üretici yok.
- **Özgün listing konsepti tahmini:** 30–50
- **IP:** "FUR BABY" (yastık sınıfında başvuru), "RAINBOW BRIDGE", "FOREVER IN MY HEART", "PAWSOME" kullanılmamalı.
- **Rekabet:** yastıkta LOW. Anma baş kelimesinde HIGH (428k ilan).

### Küme 3 — Hala/teyze, amca/dayı ve büyükanne rol hediyeleri
- **Ana kelime:** {kw("auntie mug")}
- **İlgili kelimeler:** {kw("auntie gifts")}; {kw("auntie shirt")}; {kw("uncle mug")}; {kw("personalized grandma sweatshirt")}; {kw("new grandma mug")}; {kw("new grandma gift")}
- **Doğrulanmış fiyat (auntie mug):**
  - Medyan $13.18 + $5.99 kargo.
  - Kartların %96'sı indirimde.
  - İncelenen 5 detay sayfasının 5'i de POD ortağı beyan ediyor (Printify dahil).
- **Ekonomi:** En iyi doğrulanmış kupa maliyeti Printful 11oz ($12.76). Katkı $4.14 (medyan) / $6.49 (P75) → ince. Printify/Taylor 11oz Premium ile $5.23 / $7.58. Giyim versiyonu (auntie shirt, grandma sweatshirt) fiyat doğrulaması bekliyor.
- **Özgün listing konsepti tahmini:** 30–40
- **IP:** "COOL AUNT", "MAMA", NANA/MIMI/GIGI/GLAMMA tek başına kullanılmamalı.

### Küme 4 — Meslek ve takdir hediyeleri (emeklilik, hemşire)
- **Ana kelime:** {kw("retirement gifts for women")}
- **İlgili kelimeler:** {kw("retirement mug")}; {kw("nurse retirement gift")}; {kw("nurse sweatshirt")}; {kw("nurse shirt")}
- **Doğrulanmış fiyat (retirement gifts for women):**
  - Medyan $13.46 + $5.99 kargo.
  - Mum, bardak ve kupa karışık bir pazar.
- **Ekonomi:** Printful 11oz kupa ile katkı $4.39 / $8.13. Mesleğe özel sweatshirt fiyatları doğrulanmadı.
- **Özgün listing konsepti tahmini:** 30–50
- **IP:** "OFFICIALLY RETIRED", "RETIRED" (tek başına), "HAPPY RETIREMENT" (battaniye) kullanılmamalı.

### Küme 5 — Yılbaşı tekstili (çorap, ağaç eteği): Printful ile ELENDİ
- **Ana kelime:** {kw("personalized christmas stocking")}
- **İlgili kelimeler:** {kw("dog christmas stocking")}; {kw("christmas tree skirt")}
- **Doğrulanmış fiyat:**
  - Çorap medyanı $9.02 (P75 $24.99).
  - Kumaş ve işlemeli ürünler baskın.
  - Kartların %94'ü indirimde.
- **Ekonomi:** Printful ($24.96) → medyanda −$13.52, P75'te $0.93. Printify/MWW Premium ($19.70) → −$8.26 / $6.19. Hiçbir doğrulanmış POD çorabı medyan fiyatta kârlı değil → **REJECT**. Talep güçlü (VH, +30.3%); çok daha ucuz bir tedarikçi olmadan girilmemeli.
"""

report = f"""# Etsy POD Fırsat Raporu — 25 Eylül 2026 (Marketplace Insights + doğrulanmış rakip fiyatları)

**Kaynaklar:**
1. Etsy Marketplace Insights. Mağaza VelvessenceUS (Etsy Plus), "Last 30 days" = 26 Ağu – 24 Eyl 2026. Link: https://www.etsy.com/your/shops/me/marketplace-insights?ref=seller-platform-mcnav · ham veri `data/marketplace_insights_raw.txt`
2. Etsy arama anlık görüntüsü, 14 kelime: 672 kart ve 70 detay sayfası, 25.09.2026 · ham veri `data/etsy_price_snapshot_raw.txt` · analiz `data/price_analysis.csv`
3. Printful canlı maliyetleri, USPTO taraması (iki tur), Google Trends mevsimselliği (bkz. `README.md`)

Tüm sayılar sayfalarda gösterildiği gibi. Yorum ve favori sayıları satışa çevrilmedi.

## Ana sonuç
**Süs kümesi, doğru tedarikçiyle testi hak ediyor. Çorap ve teacher tote elendi. Kupalar ince marjlı.**

Doğrulanmış rakip fiyatlarına göre süsler medyan ~$14 + $5.99 kargoya satılıyor. Katkı tedarikçiye göre değişiyor:
- **Printful süsü ($13.62):** medyanda ~$4.
- **Printify/SwiftPOD seramik süsü ($9.72, ABD'de üretim, 2.1 gün):** medyanda ~$8, P75'te $12.80–$15.25.

Round 3'te SwiftPOD varyantları doğrulandı:
- Round $4.93, Heart $5.25, hediye kutulu $7.06–$7.39.
- Economy kargo $4.79 + ek ürün başına $0.49.
- Arka yüz baskı ek ücreti **NOT VERIFIED**. Editör, arka yüze tasarım eklenmeden toplam göstermiyor.

Diğer ürünler:
- **Kupa:** en iyi doğrulanmış seçenek Printful 11oz ($12.76). Katkı ~$4 (medyan) / $6.5–8 (P75).
- **Çorap:** hiçbir doğrulanmış POD tedarikçisiyle medyan fiyatta kârlı değil.

Rakiplerin çoğu üretim ortağı beyan ediyor. Kartların %73–96'sı "indirimli" fiyatla gösteriliyor.

## Doğrulanmış fiyat bulguları (14 kelime, ilk 48 kart)

{price_table}

Notlar:
- Bu tablodaki "Contribution" Printful maliyetiyle hesaplandı: (fiyat + gözlenen ABD kargosu) × (1 − %9.5) − $0.45 − maliyet. Reklam ve indirim kodları hariç. Diğer tedarikçiler için aşağıdaki senaryo tablosuna bakın.
- Kart fiyatı en ucuz varyasyonu gösterir ("+" fiyatlar). Özellikle yastık ve çorapta bu fiyat aşağı yanlı.
- "1k+ review cards": kartta gösterilen yorum sayısı. Bunun listing'e mi mağazaya mı ait olduğu kartta belirtilmiyor.
- Malzeme dağılımı yalnızca başlıktan tahmin edildi (görseller incelenmedi).

## Tedarikçi senaryoları (aynı doğrulanmış rakip fiyatları, farklı doğrulanmış POD maliyetleri)

{supplier_table}

Printify Premium: aylık $39 veya yıllık faturada aylık $24.99 (printify.com/pricing, 25.09.2026). SwiftPOD süsünde birim başına tasarruf $1.05 → başabaş ~24 süs/ay.
Ham sayfa metinleri: `data/printify_raw/` · veri: `data/printify_costs_2026-09-25.json`, `data/supplier_scenarios.csv`.

## Round 3 — doğrulanmış varyant maliyetleri ve pet pillow boy fiyatları
- **Kaynak:** `data/round3_printify_variants_and_pillow_sizes_raw.txt`. Printify verisi, katalog sayfası ve editörün yüklediği herkese açık veriden okundu. Giriş yapılmadı, hiçbir ürün kaydedilmedi.
- **SwiftPOD seramik süs (bp 1632):**
  - Round $4.93 (Premium $3.88), Heart $5.25, Round + hediye kutusu $7.06, Heart + hediye kutusu $7.39.
  - Baskı alanları: ön ve arka. Economy kargo $4.79 / +$0.49. Standard kargo $5.89 / +$0.69. Üretim 2.1 gün.
- **Imagine Your Photos 2-side (bp 1370):** 1 adet $7.73, 3'lü $23.20, 5'li $38.67, 10'lu $77.32. Paketlerde birim fiyat indirimi yok.
- **Pic The Gift metal (bp 1182):** $4.75, kargo $5.89 / +$0.69.
- **SwiftPOD cam süs (bp 2769):** $5.59, hediye kutulu $7.73.
- **Taylor 11oz kupa (bp 1244):** $5.86, kargo $7.29 / +$3.09.
- **Pet pillow ~16" (12 listing):** fiyat + kargo medyanı $30.16, P75 $42.94.
  - Aralık: habinisi $19.20 + $2.99 kargo ile aurespaces $52.70 (ücretsiz kargo) arası.
  - Üretim ortağı beyan eden satıcılar: Spreadshirt, Printcious (HK), Print Shop 3 (MN), Charlotte NC, Printify.

## Puanlama (araştırma önceliği, satış olasılığı değil)
**Veriye dayalı bileşenler:**
- **Talep (20):** Insights arama sayısı
- **Rekabet (20):** arama/ilan oranı
- **Niyet (15):** Etsy dönüşüm etiketi
- **Marj (15):** Fiyatı doğrulanmış kelimelerde gerçek katkıdan hesaplandı: medyanda ≥$10=15, ≥$7=12, ≥$4=8, ≥$1=4, altı=0; P75 katkısı ≥$10 ise +2. Fiyatı doğrulanmamış kelimelerde en fazla 8 (temkinli).

**Analist puanları:** kişiselleştirme, genişleme, thumbnail, Q4.

**Cezalar:**
- ≥100k ilan: −10
- Maliyet >$40 veya tedarikçi doğrulanmamış: −10
- İlk sayfada 1k+ yorumlu kart sayısı ≥38/48: −10; 30–37: −5
- "client gift" için doğrulanmış baskınlık: −10

**Karar kuralı:**
- **REJECT:** P75 fiyatta katkı < $3
- **TEST NOW:** medyanda ≥ $4 ve P75'te ≥ $8 ve puan ≥ 70
- **RESEARCH MORE:** diğerleri

Marj hesabında her fırsat için **doğrulanmış en ucuz ABD tedarikçisi** kullanıldı: süslerde Printify/SwiftPOD, kupalarda Printful 11oz.

Kod: `scripts/analyze_prices.py`, `scripts/supplier_scenarios.py`, `scripts/score_opportunities.py`, `scripts/build_report.py`.

## TOP 10 ÖNCELİKLİ TEST

{top10}

**TEST NOW olanlar:** engagement ornament, first christmas married ornament, new house ornament, baby's first christmas ornament, custom pet pillow.
- **Süsler:** SwiftPOD Round ($9.72, doğrulanmış varyant) ile medyanda ~$8, P75'te $12.80–$15.25 katkı. Aynı siparişteki her ek süs ~$7 daha ekliyor.
- **Pet pillow:** boy eşleştirilmiş medyanda $4.05, P75'te $15.62 → ancak ~$40+ fiyatla.
- Printful ile aynı listing'lerde katkı ~$4'a düşüyor.
- İlk sayfada 37–41/48 kart 1k+ yorumlu. Bu yüzden yeni mağaza için ayrışan tasarım ve thumbnail yine şart.

## TOP 5 NİŞ KÜMESİ

{clusters}

## Elenenler (kanıtla)
| Kelime / konsept | Veri | Neden |
|---|---|---|
| personalized christmas stocking | {U["personalized christmas stocking"]["searches"]}/{U["personalized christmas stocking"]["listings"]}, VH | Doğrulanmış fiyatlarla Printful çorabında katkı −$13.52 (medyan) / $0.93 (P75). |
| teacher thank you gift (tote) | {U["teacher thank you gift"]["searches"]}/{U["teacher thank you gift"]["listings"]}, VH | Medyan $10.98. İlk sayfa süs ve bardak ağırlıklı. Tote ile katkı −$5.65 / −$2.02. |
| personalized baby blanket | {U["personalized baby blanket"]["searches"]}/{U["personalized baby blanket"]["listings"]}, VH | Çocuk ürünü uyumluluğu (CPSIA/CPC) → politika riski MEDIUM. |
| leaving work gifts | {U["leaving work gifts"]["searches"]}/{U["leaving work gifts"]["listings"]}, VL | Doğrulanmış medyan $12.39 < POD kupa maliyeti $12.76. |
| fall / autumn fashion | 97.1k/20.8k, 14.8k/4.6k, VL | Geniş gezinme terimleri. |
| stethoscope charm, compass keychain, planter, ring dish, charcuterie board, christmas eve box, guest book, ring box, advent calendar | Tablo B | POD değil. |
| MAMA / COOL AUNT / OFFICIALLY RETIRED / WORK BESTIE / MERRY & BRIGHT / HOLLY JOLLY / RAINBOW BRIDGE temalı tasarımlar | USPTO | İlgili sınıfta canlı tescil var. |

## Kopyalanabilir tablo (28 fırsat)

{copy}

TSV: `data/opportunities_copy.tsv` · Detaylı kartlar: `opportunities.md`

## Uyarılar
- Hiçbir fırsat için satış tahmini yapılmadı.
- IP sonuçları yalnızca ön eleme. Her listing metni yayından önce birebir aranmalı.
- Fotoğraf tabanlı ürünlerde alıcının fotoğraf hakkı olmalı. Üretim ortağı beyan edilmeli. AI ile üretilmiş nihai görselde AI beyanı gerekir.
"""
open(D + "FINAL_REPORT.md", "w").write(report)
print("FINAL_REPORT.md written;", len(R), "opportunities;", sum(r["next"] == "TEST NOW" for r in R), "TEST NOW;", sum(r["next"] == "REJECT" for r in R), "REJECT")
