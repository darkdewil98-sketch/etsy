# Etsy POD Fırsat Raporu — 25 Eylül 2026 (Marketplace Insights + doğrulanmış rakip fiyatları)

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

Printify fiyatları "from" fiyatı, yani en ucuz varyasyon. Çift yüz baskı ve hediye kutusu ek ücreti **NOT VERIFIED**.

Diğer ürünler:
- **Kupa:** en iyi doğrulanmış seçenek Printful 11oz ($12.76). Katkı ~$4 (medyan) / $6.5–8 (P75).
- **Çorap:** hiçbir doğrulanmış POD tedarikçisiyle medyan fiyatta kârlı değil.

Rakiplerin çoğu üretim ortağı beyan ediyor. Kartların %73–96'sı "indirimli" fiyatla gösteriliyor.

## Doğrulanmış fiyat bulguları (14 kelime, ilk 48 kart)

| Keyword | Median | P25–P75 | Min–Max | On sale | Free-ship badge | 1k+ review cards | Typical US shipping | Detail pages with production partner | POD cost | Contribution at median (+ship) | Contribution at P75 (+ship) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| engagement ornament | $13.99 | $9.96–$20.76 | $4.49–$30.00 | 81% | 12% | 41/48 | $5.99 | 4/5 | $13.62 | $4.01 | $10.14 |
| personalized engagement ornament | $13.24 | $9.96–$19.42 | $4.49–$30.00 | 81% | 12% | 41/48 | $5.99 | 4/5 | $13.62 | $3.33 | $8.93 |
| first christmas married ornament | $14.00 | $9.90–$19.39 | $3.45–$40.00 | 88% | 8% | 39/48 | $5.99 | 3/5 | $13.62 | $4.02 | $8.90 |
| newlywed ornament | $13.99 | $10.12–$19.98 | $4.49–$40.00 | 85% | 8% | 40/48 | $5.99 | 3/5 | $13.62 | $4.01 | $9.43 |
| personalized christmas stocking | $9.02 | $4.13–$24.99 | $1.95–$79.95 | 94% | 29% | 37/48 | $4.12 | 1/5 | $24.96 | $-13.52 | $0.93 |
| dog christmas stocking | $15.47 | $5.97–$28.68 | $3.00–$215.00 | 83% | 29% | 31/48 | $5.95 | 0/5 | $24.96 | $-6.02 | $5.93 |
| auntie mug | $13.18 | $10.99–$15.78 | $4.25–$26.22 | 96% | 0% | 25/48 | $5.99 | 5/5 | $15.40 | $1.50 | $3.85 |
| custom pet pillow | $10.43 | $8.40–$17.85 | $4.69–$44.13 | 96% | 44% | 23/48 | $6.22 | 1/5 | $22.79 | $-8.17 | $-1.46 |
| custom dog pillow | $12.39 | $9.34–$22.31 | $4.69–$44.13 | 96% | 42% | 24/48 | $6.22 | 1/5 | $22.79 | $-6.40 | $2.58 |
| baby's first christmas ornament | $14.00 | $9.96–$22.10 | $2.97–$41.59 | 73% | 15% | 40/48 | $5.99 | 1/5 | $13.62 | $4.02 | $11.35 |
| new house ornament | $14.41 | $9.99–$20.96 | $3.99–$80.00 | 75% | 8% | 37/48 | $5.99 | 2/5 | $13.62 | $4.40 | $10.32 |
| retirement gifts for women | $13.46 | $11.86–$17.59 | $4.04–$64.50 | 94% | 6% | 38/48 | $5.99 | 4/5 | $15.40 | $1.75 | $5.49 |
| family of 4 ornament | $9.41 | $5.69–$15.99 | $0.44–$55.00 | 85% | 15% | 36/48 | $5.99 | 2/5 | $13.62 | $-0.13 | $5.82 |
| teacher thank you gift | $10.98 | $6.04–$14.99 | $1.80–$39.99 | 81% | 4% | 34/48 | $5.99 | 3/5 | $20.56 | $-5.65 | $-2.02 |

Notlar:
- Bu tablodaki "Contribution" Printful maliyetiyle hesaplandı: (fiyat + gözlenen ABD kargosu) × (1 − %9.5) − $0.45 − maliyet. Reklam ve indirim kodları hariç. Diğer tedarikçiler için aşağıdaki senaryo tablosuna bakın.
- Kart fiyatı en ucuz varyasyonu gösterir ("+" fiyatlar). Özellikle yastık ve çorapta bu fiyat aşağı yanlı.
- "1k+ review cards": kartta gösterilen yorum sayısı. Bunun listing'e mi mağazaya mı ait olduğu kartta belirtilmiyor.
- Malzeme dağılımı yalnızca başlıktan tahmin edildi (görseller incelenmedi).

## Tedarikçi senaryoları (aynı doğrulanmış rakip fiyatları, farklı doğrulanmış POD maliyetleri)

| Keyword | Supplier (verified 2026-09-25) | Unit cost incl. US ship | Buyer total at median | Contribution at median | Contribution at P75 |
|---|---|---|---|---|---|
| engagement ornament | Printful ceramic 2-side #900 | $13.62 | $19.98 | $4.01 | $10.14 |
| engagement ornament | Printify / SwiftPOD ceramic (bp 1632, from) | $9.72 | $19.98 | $7.91 | $14.04 |
| engagement ornament | Printify / SwiftPOD ceramic, Premium (from) | $8.67 | $19.98 | $8.96 | $15.09 |
| engagement ornament | Printify / Pic The Gift metal (bp 1182, from) | $10.64 | $19.98 | $6.99 | $13.12 |
| engagement ornament | Printify / SwiftPOD glass (bp 2769, from) | $10.38 | $19.98 | $7.25 | $13.38 |
| first christmas married ornament | Printful ceramic 2-side #900 | $13.62 | $19.98 | $4.02 | $8.90 |
| first christmas married ornament | Printify / SwiftPOD ceramic (bp 1632, from) | $9.72 | $19.98 | $7.92 | $12.80 |
| first christmas married ornament | Printify / SwiftPOD ceramic, Premium (from) | $8.67 | $19.98 | $8.97 | $13.85 |
| first christmas married ornament | Printify / Pic The Gift metal (bp 1182, from) | $10.64 | $19.98 | $7.00 | $11.88 |
| first christmas married ornament | Printify / SwiftPOD glass (bp 2769, from) | $10.38 | $19.98 | $7.26 | $12.14 |
| newlywed ornament | Printful ceramic 2-side #900 | $13.62 | $19.98 | $4.01 | $9.43 |
| newlywed ornament | Printify / SwiftPOD ceramic (bp 1632, from) | $9.72 | $19.98 | $7.91 | $13.33 |
| newlywed ornament | Printify / SwiftPOD ceramic, Premium (from) | $8.67 | $19.98 | $8.96 | $14.38 |
| newlywed ornament | Printify / Pic The Gift metal (bp 1182, from) | $10.64 | $19.98 | $6.99 | $12.41 |
| newlywed ornament | Printify / SwiftPOD glass (bp 2769, from) | $10.38 | $19.98 | $7.25 | $12.67 |
| baby's first christmas ornament | Printful ceramic 2-side #900 | $13.62 | $19.98 | $4.02 | $11.35 |
| baby's first christmas ornament | Printify / SwiftPOD ceramic (bp 1632, from) | $9.72 | $19.98 | $7.92 | $15.25 |
| baby's first christmas ornament | Printify / SwiftPOD ceramic, Premium (from) | $8.67 | $19.98 | $8.97 | $16.30 |
| baby's first christmas ornament | Printify / Pic The Gift metal (bp 1182, from) | $10.64 | $19.98 | $7.00 | $14.33 |
| baby's first christmas ornament | Printify / SwiftPOD glass (bp 2769, from) | $10.38 | $19.98 | $7.26 | $14.59 |
| new house ornament | Printful ceramic 2-side #900 | $13.62 | $20.41 | $4.40 | $10.32 |
| new house ornament | Printify / SwiftPOD ceramic (bp 1632, from) | $9.72 | $20.41 | $8.30 | $14.22 |
| new house ornament | Printify / SwiftPOD ceramic, Premium (from) | $8.67 | $20.41 | $9.35 | $15.27 |
| new house ornament | Printify / Pic The Gift metal (bp 1182, from) | $10.64 | $20.41 | $7.38 | $13.30 |
| new house ornament | Printify / SwiftPOD glass (bp 2769, from) | $10.38 | $20.41 | $7.64 | $13.56 |
| family of 4 ornament | Printful ceramic 2-side #900 | $13.62 | $15.40 | $-0.13 | $5.82 |
| family of 4 ornament | Printify / SwiftPOD ceramic (bp 1632, from) | $9.72 | $15.40 | $3.77 | $9.72 |
| family of 4 ornament | Printify / SwiftPOD ceramic, Premium (from) | $8.67 | $15.40 | $4.82 | $10.77 |
| family of 4 ornament | Printify / Pic The Gift metal (bp 1182, from) | $10.64 | $15.40 | $2.85 | $8.80 |
| family of 4 ornament | Printify / SwiftPOD glass (bp 2769, from) | $10.38 | $15.40 | $3.11 | $9.06 |
| auntie mug | Printful 15oz #19 | $15.40 | $19.17 | $1.50 | $3.85 |
| auntie mug | Printful 11oz #19 | $12.76 | $19.17 | $4.14 | $6.49 |
| auntie mug | Printify / Taylor 11oz (bp 1244, from) | $13.15 | $19.17 | $3.75 | $6.10 |
| auntie mug | Printify / Taylor 11oz, Premium | $11.67 | $19.17 | $5.23 | $7.58 |
| auntie mug | Printify / SPOKE 15oz (bp 425, from) | $17.31 | $19.17 | $-0.41 | $1.94 |
| retirement gifts for women | Printful 15oz #19 | $15.40 | $19.45 | $1.75 | $5.49 |
| retirement gifts for women | Printful 11oz #19 | $12.76 | $19.45 | $4.39 | $8.13 |
| retirement gifts for women | Printify / Taylor 11oz (bp 1244, from) | $13.15 | $19.45 | $4.00 | $7.74 |
| retirement gifts for women | Printify / Taylor 11oz, Premium | $11.67 | $19.45 | $5.48 | $9.22 |
| retirement gifts for women | Printify / SPOKE 15oz (bp 425, from) | $17.31 | $19.45 | $-0.16 | $3.58 |
| personalized christmas stocking | Printful rustic #1428 | $24.96 | $13.13 | $-13.52 | $0.93 |
| personalized christmas stocking | Printify / MWW (bp 380, from) | $24.67 | $13.13 | $-13.23 | $1.22 |
| personalized christmas stocking | Printify / MWW, Premium | $19.70 | $13.13 | $-8.26 | $6.19 |
| personalized christmas stocking | Printify / Imagine Your Photos (bp 734, from) | $25.95 | $13.13 | $-14.51 | $-0.06 |
| dog christmas stocking | Printful rustic #1428 | $24.96 | $21.43 | $-6.02 | $5.93 |
| dog christmas stocking | Printify / MWW (bp 380, from) | $24.67 | $21.43 | $-5.73 | $6.22 |
| dog christmas stocking | Printify / MWW, Premium | $19.70 | $21.43 | $-0.76 | $11.19 |
| dog christmas stocking | Printify / Imagine Your Photos (bp 734, from) | $25.95 | $21.43 | $-7.01 | $4.94 |

Printify Premium: aylık $39 veya yıllık faturada aylık $24.99 (printify.com/pricing, 25.09.2026). SwiftPOD süsünde birim başına tasarruf $1.05 → başabaş ~24 süs/ay.
Ham sayfa metinleri: `data/printify_raw/` · veri: `data/printify_costs_2026-09-25.json`, `data/supplier_scenarios.csv`.

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

| Rank | ID | Primary keyword | Product | Searches | Listings | Demand/Competition | New-Shop Access | Margin status | Q4 | IP risk | Next step | Reason for selection |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | #01 | engagement ornament | Printify / SwiftPOD Ceramic Ornament (bp 1632; 'from' price, 2-side/gift-box upcharge NOT VERIFIED) | 10.6k | 51.9k | ratio 0.204, conv High (LOW) | HIGH | VERIFIED: $7.91 at median, $14.04 at P75 | YES | LOW APPARENT | TEST NOW | Highest demand + competition score; with Printify/SwiftPOD cost ($9.72) verified contribution $7.91 at median, $14.04 at P75. |
| 2 | #02 | auntie mug | Printful White Glossy Mug 11oz (#19) | 1.8k | 7.9k | ratio 0.228, conv Very high (LOW) | HIGH | VERIFIED: $4.14 at median, $6.49 at P75 | YES | LOW APPARENT | RESEARCH MORE | Very high conversion, 7.9k listings; best verified mug cost (Printful 11oz $12.76) leaves $4.14 at median / $6.49 at P75. |
| 3 | #03 | first christmas married ornament | Printify / SwiftPOD Ceramic Ornament (bp 1632; 'from' price, 2-side/gift-box upcharge NOT VERIFIED) | 6.7k | 33.8k | ratio 0.198, conv High (LOW) | HIGH | VERIFIED: $7.92 at median, $12.80 at P75 | YES | LOW APPARENT | TEST NOW | +11.4% growth, High conversion; SwiftPOD cost gives $7.92 at median / $12.80 at P75. |
| 4 | #04 | custom pet pillow | Printful Custom Shaped Pillow 16x16 (#743) | 3.2k | 18.2k | ratio 0.176, conv Very high (LOW) | HIGH | UNRESOLVED (size-matched price not recorded) | PARTIAL | LOW APPARENT | RESEARCH MORE | Very high conversion, smallest field (18.2k listings); size-matched price still unresolved. |
| 5 | #05 | new house ornament | Printify / SwiftPOD Ceramic Ornament (bp 1632; 'from' price, 2-side/gift-box upcharge NOT VERIFIED) | 2.5k | 19.8k | ratio 0.126, conv High (MEDIUM) | MEDIUM | VERIFIED: $8.30 at median, $14.22 at P75 | YES | LOW APPARENT | TEST NOW | High conversion; SwiftPOD cost gives $8.30 at median / $14.22 at P75; doubles as housewarming/closing gift. |
| 6 | #06 | baby's first christmas ornament | Printify / SwiftPOD Ceramic Ornament (bp 1632; 'from' price, 2-side/gift-box upcharge NOT VERIFIED) | 8.2k | 88.9k | ratio 0.092, conv High (MEDIUM) | MEDIUM | VERIFIED: $7.92 at median, $15.25 at P75 | YES | LOW APPARENT | TEST NOW | High conversion; SwiftPOD cost gives $7.92 at median / $15.25 at P75 (best P75 in the set). |
| 7 | #07 | client gift | Printify / SwiftPOD Ceramic Ornament (bp 1632; 'from' price, 2-side/gift-box upcharge NOT VERIFIED) | 15.9k | 21.1k | ratio 0.754, conv Very low (LOW) | MEDIUM | VERIFIED: $8.83 at median | YES | LOW APPARENT | RESEARCH MORE | 0.754 ratio; verified median $20.99 ($8.83 contribution at SwiftPOD cost) but page one is dominated by 1k+ review shops. |
| 8 | #08 | dog memorial gift | Printful Canvas 10x10 (#3) | 61.4k | 428.2k | ratio 0.143, conv High (HIGH) | LOW | Cost $23.62 verified; price NOT VERIFIED | PARTIAL | LOW APPARENT | RESEARCH MORE | 61.4k searches, High conversion, evergreen; competitor prices not yet collected. |
| 9 | #09 | auntie shirt | Printful Bella+Canvas 3001 tee (#71) | 3.8k | 45.7k | ratio 0.083, conv High (MEDIUM) | MEDIUM | Cost $16.87 verified; price NOT VERIFIED | PARTIAL | LOW APPARENT | RESEARCH MORE | High conversion; apparel keeps the auntie niche but prices are not yet verified. |
| 10 | #10 | retirement gifts for women | Printful White Glossy Mug 11oz (#19) | 15.5k | 48.3k | ratio 0.321, conv Low (LOW) | MEDIUM | VERIFIED: $4.39 at median, $8.13 at P75 | PARTIAL | LOW APPARENT | RESEARCH MORE | 15.5k searches, 0.321 ratio; Printful 11oz mug gives $4.39 at median / $8.13 at P75. |

**TEST NOW olanlar:** engagement ornament, first christmas married ornament, new house ornament, baby's first christmas ornament.
- Dördü de Printify/SwiftPOD seramik süsü ($9.72) varsayımıyla. Medyan fiyatta ~$8, P75'te $12.80–$15.25 katkı.
- Printful ile aynı listing'lerde katkı ~$4'a düşüyor.
- İlk sayfada 37–41/48 kart 1k+ yorumlu. Bu yüzden yeni mağaza için ayrışan tasarım ve thumbnail yine şart.

## TOP 5 NİŞ KÜMESİ

### Küme 1 — Çift ve kilometre taşı süsleri (talep en güçlü, marj koşullu)
- **Talep neden var:** İlk Noel hediyeleri (nişan, evlilik, bebek, yeni ev). Dönüşüm etiketleri çoğunlukla High/Very high.
- **Ana kelime:** engagement ornament (10.6k/51.9k, H)
- **İlgili kelimeler:** personalized engagement ornament (3.1k/16.7k, VH); first christmas married ornament (6.7k/33.8k, H); newlywed ornament (4.6k/16.5k, L); new house ornament (2.5k/19.8k, H); baby's first christmas ornament (8.2k/88.9k, H); first christmas ornament (19.6k/119.1k, L); family of 4 ornament (1.7k/10.8k, T); baptism ornament (2.9k/31.4k, T); pregnancy ornament (1.7k/19.3k, L)
- **Doğrulanmış fiyat:**
  - Medyan $13.99–$14.41, üstüne tipik $5.99 kargo.
  - Kartların %73–88'i indirimde gösteriliyor ("orijinal" fiyat ~$20–28).
  - İlk sayfada 48 kartın 37–41'i 1k+ yorumlu.
  - Detay sayfalarının çoğu üretim ortağı beyan ediyor: Printway, Inner Circle Prints (Spokane), Ballston Spa NY, Strongsville OH seramik atölyesi.
- **Ekonomi:**
  - Printful ($13.62) ile medyan fiyatta katkı ~$4.
  - Printify/SwiftPOD seramik ($9.72, "from" fiyatı) ile medyanda $7.91–$8.30, P75'te $12.80–$15.25.
  - Printify Premium ($24.99/ay yıllık) ile birim başına $1.05 daha ucuz → başabaş ~24 süs/ay.
- **Özgün listing konsepti tahmini:** 40–60
- **IP:** LOW APPARENT ("MY FIRST CHRISTMAS", "JUST MARRIED", "HOME SWEET HOME", "REALTOR" hariç)
- **Rekabet:** Insights'ta LOW–MEDIUM. Arama sayfasında yerleşik mağazalar baskın.

### Küme 2 — Evcil hayvan fotoğraf ürünleri
- **Ana kelime:** custom pet pillow (3.2k/18.2k, VH)
- **İlgili kelimeler:** custom dog pillow (2.5k/17.3k, VH); custom cat pillow (1.4k/9.5k, VH); dog memorial gift (61.4k/428.2k, H); pet memorial gift (55.9k/555k, T); cat memorial ornament (3.2k/46.7k, L); custom dog shirt (7.3k/136.6k, VH)
- **Doğrulanmış fiyat:** Kart fiyatları anahtarlık ve mini boy varyasyonlarından başlıyor (medyan $10.43). Detay sayfalarında yastık varyasyon aralıkları $9.90–$38.99 (bir mağazada $144.50'ye kadar).
- **Ekonomi:** Printful 16" yastık $22.79. 16" boyun gerçek fiyatı kaydedilmedi → **UNRESOLVED**.
- **Özgün listing konsepti tahmini:** 30–50
- **IP:** "FUR BABY" (yastık sınıfında başvuru), "RAINBOW BRIDGE", "FOREVER IN MY HEART", "PAWSOME" kullanılmamalı.
- **Rekabet:** yastıkta LOW. Anma baş kelimesinde HIGH (428k ilan).

### Küme 3 — Hala/teyze, amca/dayı ve büyükanne rol hediyeleri
- **Ana kelime:** auntie mug (1.8k/7.9k, VH)
- **İlgili kelimeler:** auntie gifts (8.1k/42.6k, T); auntie shirt (3.8k/45.7k, H); uncle mug (591/8.6k, H); personalized grandma sweatshirt (645/30.7k, VH); new grandma mug (405/28.2k, VH); new grandma gift (4.3k/137.3k, L)
- **Doğrulanmış fiyat (auntie mug):**
  - Medyan $13.18 + $5.99 kargo.
  - Kartların %96'sı indirimde.
  - İncelenen 5 detay sayfasının 5'i de POD ortağı beyan ediyor (Printify dahil).
- **Ekonomi:** En iyi doğrulanmış kupa maliyeti Printful 11oz ($12.76). Katkı $4.14 (medyan) / $6.49 (P75) → ince. Printify/Taylor 11oz Premium ile $5.23 / $7.58. Giyim versiyonu (auntie shirt, grandma sweatshirt) fiyat doğrulaması bekliyor.
- **Özgün listing konsepti tahmini:** 30–40
- **IP:** "COOL AUNT", "MAMA", NANA/MIMI/GIGI/GLAMMA tek başına kullanılmamalı.

### Küme 4 — Meslek ve takdir hediyeleri (emeklilik, hemşire)
- **Ana kelime:** retirement gifts for women (15.5k/48.3k, L)
- **İlgili kelimeler:** retirement mug (1.8k/45.1k, T); nurse retirement gift (1.1k/18.7k, H); nurse sweatshirt (17.1k/160.8k, L); nurse shirt (15.1k/270.4k, L)
- **Doğrulanmış fiyat (retirement gifts for women):**
  - Medyan $13.46 + $5.99 kargo.
  - Mum, bardak ve kupa karışık bir pazar.
- **Ekonomi:** Printful 11oz kupa ile katkı $4.39 / $8.13. Mesleğe özel sweatshirt fiyatları doğrulanmadı.
- **Özgün listing konsepti tahmini:** 30–50
- **IP:** "OFFICIALLY RETIRED", "RETIRED" (tek başına), "HAPPY RETIREMENT" (battaniye) kullanılmamalı.

### Küme 5 — Yılbaşı tekstili (çorap, ağaç eteği): Printful ile ELENDİ
- **Ana kelime:** personalized christmas stocking (9.2k/57.9k, VH)
- **İlgili kelimeler:** dog christmas stocking (2.4k/27.4k, T); christmas tree skirt (7.2k/14.5k, VL)
- **Doğrulanmış fiyat:**
  - Çorap medyanı $9.02 (P75 $24.99).
  - Kumaş ve işlemeli ürünler baskın.
  - Kartların %94'ü indirimde.
- **Ekonomi:** Printful ($24.96) → medyanda −$13.52, P75'te $0.93. Printify/MWW Premium ($19.70) → −$8.26 / $6.19. Hiçbir doğrulanmış POD çorabı medyan fiyatta kârlı değil → **REJECT**. Talep güçlü (VH, +30.3%); çok daha ucuz bir tedarikçi olmadan girilmemeli.


## Elenenler (kanıtla)
| Kelime / konsept | Veri | Neden |
|---|---|---|
| personalized christmas stocking | 9.2k/57.9k, VH | Doğrulanmış fiyatlarla Printful çorabında katkı −$13.52 (medyan) / $0.93 (P75). |
| teacher thank you gift (tote) | 3k/39.6k, VH | Medyan $10.98. İlk sayfa süs ve bardak ağırlıklı. Tote ile katkı −$5.65 / −$2.02. |
| personalized baby blanket | 35k/88.3k, VH | Çocuk ürünü uyumluluğu (CPSIA/CPC) → politika riski MEDIUM. |
| leaving work gifts | 3.6k/7.1k, VL | Doğrulanmış medyan $12.39 < POD kupa maliyeti $12.76. |
| fall / autumn fashion | 97.1k/20.8k, 14.8k/4.6k, VL | Geniş gezinme terimleri. |
| stethoscope charm, compass keychain, planter, ring dish, charcuterie board, christmas eve box, guest book, ring box, advent calendar | Tablo B | POD değil. |
| MAMA / COOL AUNT / OFFICIALLY RETIRED / WORK BESTIE / MERRY & BRIGHT / HOLLY JOLLY / RAINBOW BRIDGE temalı tasarımlar | USPTO | İlgili sınıfta canlı tescil var. |

## Kopyalanabilir tablo (28 fırsat)

| ID | Score | Keyword | Product | Searches | Listings | Ratio | Conv | Period chg | Competition | New-shop access | POD cost | Verified price range | Contribution median / P75 | Trend | Seasonality | Peak-risk | Evergreen | IP | Next step |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| #01 | 85 | engagement ornament | Printify / SwiftPOD Ceramic Ornament (bp 1632; 'from' price, 2-side/gift-box upcharge NOT VERIFIED) | 10.6k | 51.9k | 0.204 | H | not shown | LOW | HIGH | $9.72 | $9.96–$20.76 (P25–P75), median $13.99, full $4.49–$30.00; typical US shipping $5.99 | $7.91 / $14.04 | EARLY SIGNAL | HIGH | MEDIUM | MEDIUM | LOW APPARENT | TEST NOW |
| #02 | 81 | auntie mug | Printful White Glossy Mug 11oz (#19) | 1.8k | 7.9k | 0.228 | VH | not shown | LOW | HIGH | $12.76 | $10.99–$15.78 (P25–P75), median $13.18, full $4.25–$26.22; typical US shipping $5.99 | $4.14 / $6.49 | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #03 | 79 | first christmas married ornament | Printify / SwiftPOD Ceramic Ornament (bp 1632; 'from' price, 2-side/gift-box upcharge NOT VERIFIED) | 6.7k | 33.8k | 0.198 | H | +11.4% | LOW | HIGH | $9.72 | $9.90–$19.39 (P25–P75), median $14.00, full $3.45–$40.00; typical US shipping $5.99 | $7.92 / $12.80 | VERIFIED CURRENT TREND | HIGH | HIGH | LOW | LOW APPARENT | TEST NOW |
| #04 | 78 | custom pet pillow | Printful Custom Shaped Pillow 16x16 (#743) | 3.2k | 18.2k | 0.176 | VH | not shown | LOW | HIGH | $22.79 | $8.40–$17.85 (P25–P75), median $10.43, full $4.69–$44.13; typical US shipping $6.22 | — | EVERGREEN | MEDIUM | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #05 | 78 | new house ornament | Printify / SwiftPOD Ceramic Ornament (bp 1632; 'from' price, 2-side/gift-box upcharge NOT VERIFIED) | 2.5k | 19.8k | 0.126 | H | not shown | MEDIUM | MEDIUM | $9.72 | $9.99–$20.96 (P25–P75), median $14.41, full $3.99–$80.00; typical US shipping $5.99 | $8.30 / $14.22 | EARLY SIGNAL | HIGH | MEDIUM | HIGH | LOW APPARENT | TEST NOW |
| #06 | 73 | baby's first christmas ornament | Printify / SwiftPOD Ceramic Ornament (bp 1632; 'from' price, 2-side/gift-box upcharge NOT VERIFIED) | 8.2k | 88.9k | 0.092 | H | +4.9% | MEDIUM | MEDIUM | $9.72 | $9.96–$22.10 (P25–P75), median $14.00, full $2.97–$41.59; typical US shipping $5.99 | $7.92 / $15.25 | EARLY SIGNAL | HIGH | HIGH | MEDIUM | LOW APPARENT | TEST NOW |
| #07 | 73 | client gift | Printify / SwiftPOD Ceramic Ornament (bp 1632; 'from' price, 2-side/gift-box upcharge NOT VERIFIED) | 15.9k | 21.1k | 0.754 | VL | not shown | LOW | MEDIUM | $9.72 | $2.03–$80.99, median $20.99 (Table B, 48 cards); shipping NOT VERIFIED | $8.83 / — | EARLY SIGNAL | MEDIUM | MEDIUM | HIGH | LOW APPARENT | RESEARCH MORE |
| #08 | 70 | dog memorial gift | Printful Canvas 10x10 (#3) | 61.4k | 428.2k | 0.143 | H | not shown | HIGH | LOW | $23.62 | NOT VERIFIED | — | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #09 | 70 | auntie shirt | Printful Bella+Canvas 3001 tee (#71) | 3.8k | 45.7k | 0.083 | H | not shown | MEDIUM | MEDIUM | $16.87 | NOT VERIFIED | — | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #10 | 68 | retirement gifts for women | Printful White Glossy Mug 11oz (#19) | 15.5k | 48.3k | 0.321 | L | not shown | LOW | MEDIUM | $12.76 | $11.86–$17.59 (P25–P75), median $13.46, full $4.04–$64.50; typical US shipping $5.99 | $4.39 / $8.13 | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #11 | 68 | bookish stickers | Printful Kiss-cut sticker 3x3 (#358) | 7.5k | 63.1k | 0.119 | T | not shown | MEDIUM | MEDIUM | $6.83 | NOT VERIFIED | — | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #12 | 66 | family of 4 ornament | Printify / SwiftPOD Ceramic Ornament (bp 1632; 'from' price, 2-side/gift-box upcharge NOT VERIFIED) | 1.7k | 10.8k | 0.157 | T | not shown | LOW | HIGH | $9.72 | $5.69–$15.99 (P25–P75), median $9.41, full $0.44–$55.00; typical US shipping $5.99 | $3.77 / $9.72 | EARLY SIGNAL | HIGH | HIGH | MEDIUM | LOW APPARENT | RESEARCH MORE |
| #13 | 66 | personalized bookmark | Bookmark (no Printful product; supplier NOT VERIFIED) | 6.5k | 34.2k | 0.19 | VH | not shown | LOW | HIGH | NOT VERIFIED | NOT VERIFIED | — | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #14 | 65 | baptism ornament | Printify / SwiftPOD Ceramic Ornament (bp 1632; 'from' price, 2-side/gift-box upcharge NOT VERIFIED) | 2.9k | 31.4k | 0.092 | T | not shown | MEDIUM | MEDIUM | $9.72 | NOT VERIFIED | — | EVERGREEN | MEDIUM | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #15 | 65 | custom dog shirt | Printful Bella+Canvas 3001 tee (#71) | 7.3k | 136.6k | 0.053 | VH | not shown | HIGH | LOW | $16.87 | NOT VERIFIED | — | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #16 | 64 | personalized grandma sweatshirt | Printful Gildan 18000 + sleeve print (#145) | 645 | 30.7k | 0.021 | VH | not shown | HIGH | LOW | $33.91 | NOT VERIFIED | — | EARLY SIGNAL | MEDIUM | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #17 | 64 | custom embroidered sweatshirt | Printful Gildan 18000, embroidery left chest (#145) | 11k | 111.2k | 0.099 | T | not shown | HIGH | LOW | $30.91 | NOT VERIFIED | — | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #18 | 62 | pregnancy ornament | Printify / SwiftPOD Ceramic Ornament (bp 1632; 'from' price, 2-side/gift-box upcharge NOT VERIFIED) | 1.7k | 19.3k | 0.088 | L | not shown | MEDIUM | MEDIUM | $9.72 | NOT VERIFIED | — | EARLY SIGNAL | HIGH | HIGH | LOW | LOW APPARENT | RESEARCH MORE |
| #19 | 62 | cat memorial ornament | Printify / SwiftPOD Ceramic Ornament (bp 1632; 'from' price, 2-side/gift-box upcharge NOT VERIFIED) | 3.2k | 46.7k | 0.069 | L | not shown | MEDIUM | MEDIUM | $9.72 | NOT VERIFIED | — | EVERGREEN | MEDIUM | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #20 | 62 | nurse sweatshirt | Printful Gildan 18000 crewneck, front print (#145) | 17.1k | 160.8k | 0.106 | L | not shown | HIGH | LOW | $27.96 | NOT VERIFIED | — | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #21 | 60 | uncle mug | Printful White Glossy Mug 11oz (#19) | 591 | 8.6k | 0.069 | H | not shown | MEDIUM | MEDIUM | $12.76 | NOT VERIFIED | — | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #22 | 59 | turkey trot shirt | Printful Bella+Canvas 3001 tee (#71) | 878 | 5.4k | 0.163 | VL | not shown | LOW | MEDIUM | $16.87 | NOT VERIFIED | — | VERIFIED CURRENT TREND | HIGH | HIGH | LOW | LOW APPARENT | RESEARCH MORE |
| #23 | 58 | new grandma mug | Printful White Glossy Mug 11oz (#19) | 405 | 28.2k | 0.014 | VH | not shown | HIGH | LOW | $12.76 | NOT VERIFIED | — | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #24 | 57 | christmas tree skirt | Printful Christmas Tree Skirt (#1427) | 7.2k | 14.5k | 0.497 | VL | not shown | LOW | MEDIUM | $51.74 | NOT VERIFIED | — | EARLY SIGNAL | HIGH | HIGH | LOW | LOW APPARENT | RESEARCH MORE |
| #25 | 56 | dog christmas stocking | Printful Rustic Christmas Stocking (#1428) | 2.4k | 27.4k | 0.088 | T | not shown | MEDIUM | MEDIUM | $24.96 | $5.97–$28.68 (P25–P75), median $15.47, full $3.00–$215.00; typical US shipping $5.95 | $-6.02 / $5.93 | EARLY SIGNAL | HIGH | HIGH | LOW | LOW APPARENT | RESEARCH MORE |
| #26 | 56 | family christmas shirts | Printful Bella+Canvas 3001 tee (#71) | 6.1k | 121k | 0.05 | L | +17.5% | HIGH | LOW | $16.87 | NOT VERIFIED | — | VERIFIED CURRENT TREND | HIGH | HIGH | LOW | LOW APPARENT | RESEARCH MORE |
| #27 | 71 | personalized christmas stocking | Printful Rustic Christmas Stocking (#1428) | 9.2k | 57.9k | 0.159 | VH | +30.3% | LOW | HIGH | $24.96 | $4.13–$24.99 (P25–P75), median $9.02, full $1.95–$79.95; typical US shipping $4.12 | $-13.52 / $0.93 | VERIFIED CURRENT TREND | HIGH | HIGH | LOW | LOW APPARENT | REJECT |
| #28 | 60 | teacher thank you gift | Printful Eco Tote EC8000 (#367) | 3k | 39.6k | 0.076 | VH | not shown | MEDIUM | MEDIUM | $20.56 | $6.04–$14.99 (P25–P75), median $10.98, full $1.80–$39.99; typical US shipping $5.99 | $-5.65 / $-2.02 | EVERGREEN | MEDIUM | LOW | HIGH | LOW APPARENT | REJECT |

TSV: `data/opportunities_copy.tsv` · Detaylı kartlar: `opportunities.md`

## Uyarılar
- Hiçbir fırsat için satış tahmini yapılmadı.
- IP sonuçları yalnızca ön eleme. Her listing metni yayından önce birebir aranmalı.
- Fotoğraf tabanlı ürünlerde alıcının fotoğraf hakkı olmalı. Üretim ortağı beyan edilmeli. AI ile üretilmiş nihai görselde AI beyanı gerekir.
