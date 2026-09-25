# Etsy POD Fırsat Raporu — 25 Eylül 2026 (Marketplace Insights verisiyle)

**Veri kaynağı:** Etsy Marketplace Insights. Mağaza VelvessenceUS (Etsy Plus), dönem "Last 30 days" = 26 Ağustos – 24 Eylül 2026.
Veriyi kullanıcı, Claude in Chrome ile şu linkten topladı:
https://www.etsy.com/your/shops/me/marketplace-insights?ref=seller-platform-mcnav
Ham dosya: `data/marketplace_insights_raw.txt`.

**Ek kaynaklar:** Printful canlı maliyetleri, USPTO canlı marka taraması (iki tur), Google Trends mevsimsellik verisi (bkz. `README.md`).

## Veri bütünlüğü notları
- 154 anahtar kelime arandı. Her birinin "Similar search terms" tablosunun ilk 3 sayfası alındı. Toplam **2.482 benzersiz terim**, `data/insights_keyword_universe.csv` dosyasında.
- Tüm arama ve ilan sayıları Insights sayfasında gösterildiği gibi (k/M yuvarlamasıyla). "Ratio" = searches / listings, benim hesabım.
- Dönüşüm etiketi (VL/L/T/H/VH), Etsy'nin kendi "conversion rate" etiketi. Alıcı niyeti puanında kullanıldı.
- Insights'taki "listings" ile Etsy aramasındaki sonuç sayısı farklı ölçüler. Tablo B'de ikisi de ayrı ayrı raporlandı.
- **Fiyatlar:** Rakip fiyatı yalnızca Tablo B'de incelenen 15 kelime için doğrulandı. Bunlardan POD'a uyan ikisi var: "client gift" ve "leaving work gifts". Diğer tüm fırsatlarda satış fiyatı **NOT VERIFIED**. Marj tablosu bu yüzden "en az kaça satılmalı" sorusunu cevaplıyor.
- Yorum ve favori sayıları satışa çevrilmedi. Mağaza toplam satışları yalnızca mağaza olgunluğu göstergesi olarak kullanıldı.
- **Q4 zamanlaması:** Insights dönemi zirve öncesi. Google Trends'te süs ve çorap rampası geçen yıl 21–28 Eylül'de başladı. Q4 kelimelerinin arama sayısı önümüzdeki haftalarda muhtemelen artacak. Bu bir tahmin değil, geçmiş mevsimsellik.

## Puanlama yöntemi (araştırma önceliği, satış olasılığı değil)
Otomatik ve veriye dayalı bileşenler:
- **Talep (20):** Insights arama sayısı; ≥10k=20, ≥5k=17, ≥2k=14, ≥1k=11, ≥500=8.
- **Rekabet (20):** oran; ≥0.20=20, ≥0.15=17, ≥0.10=14, ≥0.07=11, ≥0.05=8.
- **Niyet (15):** Etsy dönüşüm etiketi; VH=15, H=12, T=9, L=6, VL=3.
- **Marj (15):** Printful maliyeti; ≤$15=13, ≤$25=11, ≤$35=8, üstü=5, doğrulanmamış=3. Fiyat doğrulanmadığı için üst sınır 13.

Analist puanları: kişiselleştirme (10), genişleme (10), thumbnail (5), Q4 (5).

Cezalar:
- ≥100k ilan: −10
- Maliyet >$40 veya tedarikçi doğrulanmamış: −10
- Doğrulanmış aşırı rekabet / zayıf ekonomi: −10'ar

Kod: `scripts/score_opportunities.py`.

## TOP 10 ÖNCELİKLİ TEST

| Rank | ID | Primary keyword | Product | Searches | Listings | Demand/Competition | New-Shop Access | Margin status | Q4 | IP risk | Reason for selection |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | #01 | engagement ornament | Printful Ceramic Ornament, 2-side (#900) | 10.6k | 51.9k | ratio 0.204, conv High (LOW competition) | HIGH | Cost $13.62 verified; price NOT VERIFIED; ≥$26.6 for $10 contribution | YES | LOW APPARENT | Highest combined score: 10.6k searches, 0.204 ratio, High conversion; whole engaged-ornament family is small-field (14k–52k listings). |
| 2 | #02 | first christmas married ornament | Printful Ceramic Ornament, 2-side (#900) | 6.7k | 33.8k | ratio 0.198, conv High (LOW competition) | HIGH | Cost $13.62 verified; price NOT VERIFIED; ≥$26.6 for $10 contribution | YES | LOW APPARENT | +11.4% period growth with High conversion; 'newlywed ornament' 0.279 ratio in the same buyer set. |
| 3 | #03 | personalized christmas stocking | Printful Rustic Christmas Stocking (#1428) | 9.2k | 57.9k | ratio 0.159, conv Very high (LOW competition) | HIGH | Cost $24.96 verified; price NOT VERIFIED; ≥$39.13 for $10 contribution | YES | LOW APPARENT | Very high conversion, +30.3% growth; multi-unit family orders. |
| 4 | #04 | auntie mug | Printful White Glossy Mug 15oz (#19) | 1.8k | 7.9k | ratio 0.228, conv Very high (LOW competition) | HIGH | Cost $15.40 verified; price NOT VERIFIED; ≥$28.56 for $10 contribution | YES | LOW APPARENT | Very high conversion with only 7.9k listings (0.228 ratio); evergreen beyond Q4. |
| 5 | #05 | custom pet pillow | Printful Custom Shaped Pillow 16x16 (#743) | 3.2k | 18.2k | ratio 0.176, conv Very high (LOW competition) | HIGH | Cost $22.79 verified; price NOT VERIFIED; ≥$36.73 for $10 contribution | PARTIAL | LOW APPARENT | Very high conversion on all three pet-pillow terms with 9.5k–18k listings; evergreen. |
| 6 | #06 | baby's first christmas ornament | Printful Ceramic Ornament, 2-side (#900) | 8.2k | 88.9k | ratio 0.092, conv High (MEDIUM competition) | MEDIUM | Cost $13.62 verified; price NOT VERIFIED; ≥$26.6 for $10 contribution | YES | LOW APPARENT | High conversion, 8.2k searches; 'first christmas ornament' adds 19.6k searches at 0.165. |
| 7 | #07 | new house ornament | Printful Ceramic Ornament, 2-side (#900) | 2.5k | 19.8k | ratio 0.126, conv High (MEDIUM competition) | MEDIUM | Cost $13.62 verified; price NOT VERIFIED; ≥$26.6 for $10 contribution | YES | LOW APPARENT | High conversion with 19.8k listings; same product feeds housewarming and closing-gift demand. |
| 8 | #08 | retirement gifts for women | Printful White Glossy Mug 15oz (#19) | 15.5k | 48.3k | ratio 0.321, conv Low (LOW competition) | MEDIUM | Cost $15.40 verified; price NOT VERIFIED; ≥$28.56 for $10 contribution | PARTIAL | LOW APPARENT | 15.5k searches at a 0.321 ratio; evergreen; avoid the verified low-price funny-candle segment. |
| 9 | #09 | family of 4 ornament | Printful Ceramic Ornament, 2-side (#900) | 1.7k | 10.8k | ratio 0.157, conv Typical (LOW competition) | HIGH | Cost $13.62 verified; price NOT VERIFIED; ≥$26.6 for $10 contribution | YES | LOW APPARENT | 0.157 ratio micro-keyword (10.8k listings) vs 144k on the generic family term. |
| 10 | #10 | teacher thank you gift | Printful Eco Tote EC8000 (#367) | 3k | 39.6k | ratio 0.076, conv Very high (MEDIUM competition) | MEDIUM | Cost $20.56 verified; price NOT VERIFIED; ≥$34.27 for $10 contribution | YES | LOW APPARENT | Very high conversion; teacher Christmas searches +20.2%; second peak in May. |

## TOP 5 NİŞ KÜMESİ

### Küme 1 — Çift ve kilometre taşı süsleri (en güçlü)
- **Talep neden var:** İlk Noel (nişan, evlilik, bebek, yeni ev) hediyeleri. Insights'ta bu ailenin dönüşümü çoğunlukla High/Very high.
- **Ana kelime:** engagement ornament (10.6k/51.9k, H)
- **İlgili kelimeler:** personalized engagement ornament (3.1k/16.7k, VH); first christmas married ornament (6.7k/33.8k, H); newlywed ornament (4.6k/16.5k, L); first christmas engaged ornament (2.4k/14.2k, T); new house ornament (2.5k/19.8k, H); baby's first christmas ornament (8.2k/88.9k, H); first christmas ornament (19.6k/119.1k, L); family of 4 ornament (1.7k/10.8k, T); baptism ornament (2.9k/31.4k, T); pregnancy ornament (1.7k/19.3k, L)
- **Alıcılar:** çiftler, ebeveynler, büyükanne/büyükbabalar, düğün misafirleri, emlak danışmanları
- **Durumlar:** ilk Noel, nişan, düğün, yeni ev, doğum, vaftiz, hamilelik duyurusu
- **POD ürünleri:** Printful çift yüzlü seramik süs ($13.62), ahşap ($13.56), akrilik ($13.29), metal ($10.50)
- **Kişiselleştirme:** isimler, tarih, yıl, şehir, ev çizimi, doğum bilgileri, fotoğraf (arka yüz)
- **Q4 açısı:** Google Trends'te süs rampası geçen yıl 21–28 Eylül'de başladı. Insights dönemi (26 Ağu – 24 Eyl) zirve öncesi.
- **Özgün listing konsepti tahmini:** 40–60 (8 durum × 3–4 stil × renk varyasyonları)
- **IP riski:** LOW APPARENT. "MY FIRST CHRISTMAS", "JUST MARRIED" (giyim), "HOME SWEET HOME" (kupa), "RAINBOW BRIDGE" kullanılmamalı.
- **Rekabet:** LOW–MEDIUM (mikro kelimelerde 10.8k–52k ilan)

### Küme 2 — Kişiselleştirilmiş yılbaşı çorapları ve tekstil
- **Talep neden var:** Aileler her üye için isimli çorap alıyor, bu da çoklu adet siparişe dönüşüyor.
- **Ana kelime:** personalized christmas stocking (9.2k/57.9k, VH) (+30.3%)
- **İlgili kelimeler:** christmas stocking personalized (9k/64.8k, H); personalized stocking (4.3k/76.1k, H); dog christmas stocking (2.4k/27.4k, T); cat christmas stocking (1.3k/18.4k, L); christmas tree skirt (7.2k/14.5k, VL); personalized tree skirt (1.3k/13.2k, VL)
- **Alıcılar:** ebeveynler, büyükanneler, evcil hayvan sahipleri
- **Durumlar:** Noel dekorasyonu (Ekim–Aralık)
- **POD ürünleri:** Printful rustik çorap ($24.96), ağaç eteği ($51.74)
- **Kişiselleştirme:** isim, evcil hayvan adı ve ırkı, aile soyadı, yıl
- **Q4 açısı:** tamamen Q4
- **Özgün listing konsepti tahmini:** 20–30
- **IP riski:** LOW APPARENT. "MERRY & BRIGHT", "HOLLY JOLLY", tek başına "JOY"/"BELIEVE" kullanılmamalı.
- **Rekabet:** MEDIUM. İşlemeli ve needlepoint çoraplar premium segmenti tutuyor.

### Küme 3 — Evcil hayvan fotoğraf ürünleri
- **Talep neden var:** Hayvan sahipleri kendi hayvanlarının görüntüsünü istiyor. Anma ürünleri yıl boyu satıyor.
- **Ana kelime:** custom pet pillow (3.2k/18.2k, VH)
- **İlgili kelimeler:** custom dog pillow (2.5k/17.3k, VH); custom cat pillow (1.4k/9.5k, VH); dog memorial gift (61.4k/428.2k, H); pet memorial gift (55.9k/555k, T); pet remembrance gift (21.3k/183.3k, H); cat memorial ornament (3.2k/46.7k, L); custom dog shirt (7.3k/136.6k, VH); custom pet portrait (36.8k/188.6k, VL)
- **Alıcılar:** köpek ve kedi sahipleri, taziye hediyesi alanlar
- **Durumlar:** Noel, doğum günü, kayıp/anma (yıl boyu)
- **POD ürünleri:** özel kesim yastık ($22.79), kanvas 10x10 ($23.62), seramik süs ($13.62), tişört ($16.87)
- **Kişiselleştirme:** hayvan fotoğrafı, isim, tarihler
- **Q4 açısı:** Noel hediyesi ve anma süsleri
- **Özgün listing konsepti tahmini:** 30–50
- **IP riski:** LOW APPARENT. "FUR BABY" (yastık sınıfı 020), "FURBABY", "PAWSOME", "RAINBOW BRIDGE", "FOREVER IN MY HEART" kullanılmamalı.
- **Rekabet:** yastıkta LOW, anma baş kelimesinde HIGH (428k ilan)

### Küme 4 — Hala/teyze, amca/dayı ve büyükanne rol hediyeleri
- **Talep neden var:** Aile rolüne özel, çocuk isimleriyle kişiselleştirilen hediyeler. Yıl boyu doğum günü ve duyuru talebi var.
- **Ana kelime:** auntie mug (1.8k/7.9k, VH)
- **İlgili kelimeler:** auntie gifts (8.1k/42.6k, T); auntie shirt (3.8k/45.7k, H); aunt shirt (4k/60.5k, T); uncle mug (591/8.6k, H); uncle birthday gift (914/26.7k, VH); personalized grandma sweatshirt (645/30.7k, VH); custom grandma sweatshirt (452/65.9k, VH); new grandma mug (405/28.2k, VH); new grandma gift (4.3k/137.3k, L); custom grandpa mug (262/23.9k, VH)
- **Alıcılar:** yeğenlerin ebeveynleri, torunlar, kardeşler
- **Durumlar:** Noel, doğum günleri, hamilelik duyurusu, Anneler Günü
- **POD ürünleri:** 15oz kupa ($15.40), tişört ($16.87), kol baskılı sweatshirt ($33.91), süs
- **Kişiselleştirme:** çocukların isimleri, est. yılı, duyuru tarihi
- **Q4 açısı:** Noel hediyesi; asıl değeri evergreen
- **Özgün listing konsepti tahmini:** 30–40
- **IP riski:** LOW APPARENT. "COOL AUNT" (giyim), "MAMA" (giyim, 11.08.2026), NANA/MIMI/GIGI/GLAMMA tek başına kullanılmamalı.
- **Rekabet:** kupada LOW, giyimde MEDIUM

### Küme 5 — Meslek ve takdir hediyeleri (emeklilik, öğretmen, hemşire)
- **Talep neden var:** İş yeri ve okul hediyeleşmesi. Emeklilik yıl boyu, öğretmen hediyesi Aralık ve Mayıs'ta zirve yapıyor.
- **Ana kelime:** retirement gifts for women (15.5k/48.3k, L)
- **İlgili kelimeler:** retirement mug (1.8k/45.1k, T); nurse retirement gift (1.1k/18.7k, H); retirement ornament (999/22.4k, L); teacher thank you gift (3k/39.6k, VH); teacher christmas gift (3.3k/114.6k, VL); personalized teacher gift (4.5k/88.8k, L); nurse sweatshirt (17.1k/160.8k, L); nurse shirt (15.1k/270.4k, L)
- **Alıcılar:** iş arkadaşları, veliler, aile
- **Durumlar:** emeklilik partisi, yıl sonu, Noel, Nurses Week, Teacher Appreciation
- **POD ürünleri:** kupa ($15.40), tote ($20.56), sweatshirt ($27.96), süs ($13.62)
- **Kişiselleştirme:** isim, meslek/uzmanlık, hizmet yılları, öğrenci isimleri
- **Q4 açısı:** öğretmen Noel hediyesi (+20.2%), yıl sonu emeklilikleri
- **Özgün listing konsepti tahmini:** 30–50 (meslek × durum × ürün)
- **IP riski:** LOW APPARENT. "OFFICIALLY RETIRED", "RETIRED" (tek başına), "HAPPY RETIREMENT" (battaniye), "WORK BESTIE" (kupa) kullanılmamalı.
- **Rekabet:** MEDIUM. Bitişik "leaving work gifts" segmentinde doğrulanmış medyan fiyat $12.39 (düşük).

## Ana listeye alınmayanlar (kanıtla)
| Kelime / konsept | Insights verisi | Neden elendi |
|---|---|---|
| personalized baby blanket | 35k/88.3k, VH, oran 0.396 | Veride en güçlü tekil sinyal. Ama bebeğe yönelik battaniye ABD'de "children's product" sayılabilir (CPSIA / Children's Product Certificate). Printful throw blanket çocuk ürünü olarak sertifikalı değil → **POLİTİKA RİSKİ MEDIUM → elendi.** Uyumlu bir tedarikçi bulunursa ilk araştırılacak konu. |
| leaving work gifts | 3.6k/7.1k, VL | Tablo B'de doğrulandı: medyan fiyat $12.39. POD kupa maliyeti $12.76 → zayıf ekonomi. |
| fall fashion / autumn fashion | 97.1k/20.8k ve 14.8k/4.6k, VL | Tarama notuna göre geniş gezinme terimi. Etsy aramasında 474,991 ve 204,157 sonuç var. |
| stethoscope charm, compass keychain, personalized planter, ring/jewelry dish, charcuterie board, christmas eve box, guest book alternative, engagement ring box, advent calendar | Tablo B | POD değil (gravürlü veya fiziksel ürünler). Kapsam dışı. |
| mama sweatshirt ailesi | – | "MAMA", 11.08.2026'da giyimde tescil edildi (Reg. 8387670). |
| cool aunt, officially retired, work bestie (kupa), merry & bright, holly jolly, rainbow bridge | – | USPTO'da ilgili sınıfta canlı tescil var. |
| personalized mug with photo / custom tumbler with picture / personalized blanket with pictures | 125/22.1k, 12/8k, 42/43.8k | Bu kalıpların arama hacmi ihmal edilebilir düzeyde. |
| thanksgiving shirt (baş terim) | 14.2k/209.2k, VL | 209k ilan ve Very low dönüşüm. Yalnızca "turkey trot shirt" uzun kuyruğu tutuldu. |
| book lover gift (baş terim) | 98.4k/245.8k, VL, −49.5% | Dengesiz hacim ve "bookish" marka kalabalığı. Yalnızca sticker uzun kuyruğu tutuldu. |
| gardening gift for mom, nana gift personalized | 8 ve 7 arama | Talep yok. |

## Kopyalanabilir tablo (tüm 28 fırsat)

| ID | Score | Keyword | Product | Searches | Listings | Ratio | Conv | Period chg | Competition | New-shop access | POD cost (US) | Price for $10 contrib. | Price for $15 contrib. | Trend | Seasonality | Peak-risk | Evergreen | IP | Next step |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| #01 | 94 | engagement ornament | Printful Ceramic Ornament, 2-side (#900) | 10.6k | 51.9k | 0.204 | H | not shown | LOW | HIGH | $13.62 | $26.6 | $32.12 | EARLY SIGNAL | HIGH | MEDIUM | MEDIUM | LOW APPARENT | TEST NOW |
| #02 | 88 | first christmas married ornament | Printful Ceramic Ornament, 2-side (#900) | 6.7k | 33.8k | 0.198 | H | +11.4% | LOW | HIGH | $13.62 | $26.6 | $32.12 | VERIFIED CURRENT TREND | HIGH | HIGH | LOW | LOW APPARENT | TEST NOW |
| #03 | 87 | personalized christmas stocking | Printful Rustic Christmas Stocking (#1428) | 9.2k | 57.9k | 0.159 | VH | +30.3% | LOW | HIGH | $24.96 | $39.13 | $44.65 | VERIFIED CURRENT TREND | HIGH | HIGH | LOW | LOW APPARENT | TEST NOW |
| #04 | 84 | auntie mug | Printful White Glossy Mug 15oz (#19) | 1.8k | 7.9k | 0.228 | VH | not shown | LOW | HIGH | $15.40 | $28.56 | $34.09 | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | TEST NOW |
| #05 | 83 | custom pet pillow | Printful Custom Shaped Pillow 16x16 (#743) | 3.2k | 18.2k | 0.176 | VH | not shown | LOW | HIGH | $22.79 | $36.73 | $42.25 | EVERGREEN | MEDIUM | LOW | HIGH | LOW APPARENT | TEST NOW |
| #06 | 82 | baby's first christmas ornament | Printful Ceramic Ornament, 2-side (#900) | 8.2k | 88.9k | 0.092 | H | +4.9% | MEDIUM | MEDIUM | $13.62 | $26.6 | $32.12 | EARLY SIGNAL | HIGH | HIGH | MEDIUM | LOW APPARENT | TEST NOW |
| #07 | 82 | new house ornament | Printful Ceramic Ornament, 2-side (#900) | 2.5k | 19.8k | 0.126 | H | not shown | MEDIUM | MEDIUM | $13.62 | $26.6 | $32.12 | EARLY SIGNAL | HIGH | MEDIUM | HIGH | LOW APPARENT | TEST NOW |
| #08 | 81 | retirement gifts for women | Printful White Glossy Mug 15oz (#19) | 15.5k | 48.3k | 0.321 | L | not shown | LOW | MEDIUM | $15.40 | $28.56 | $34.09 | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | TEST NOW |
| #09 | 80 | family of 4 ornament | Printful Ceramic Ornament, 2-side (#900) | 1.7k | 10.8k | 0.157 | T | not shown | LOW | HIGH | $13.62 | $26.6 | $32.12 | EARLY SIGNAL | HIGH | HIGH | MEDIUM | LOW APPARENT | TEST NOW |
| #10 | 76 | teacher thank you gift | Printful Eco Tote EC8000 (#367) | 3k | 39.6k | 0.076 | VH | not shown | MEDIUM | MEDIUM | $20.56 | $34.27 | $39.79 | EVERGREEN | MEDIUM | LOW | HIGH | LOW APPARENT | TEST NOW |
| #11 | 73 | dog memorial gift | Printful Canvas 10x10 (#3) | 61.4k | 428.2k | 0.143 | H | not shown | HIGH | LOW | $23.62 | $37.65 | $43.17 | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #12 | 73 | auntie shirt | Printful Bella+Canvas 3001 tee (#71) | 3.8k | 45.7k | 0.083 | H | not shown | MEDIUM | MEDIUM | $16.87 | $30.19 | $35.71 | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #13 | 73 | bookish stickers | Printful Kiss-cut sticker 3x3 (#358) | 7.5k | 63.1k | 0.119 | T | not shown | MEDIUM | MEDIUM | $6.83 | $19.09 | $24.62 | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #14 | 72 | dog christmas stocking | Printful Rustic Christmas Stocking (#1428) | 2.4k | 27.4k | 0.088 | T | not shown | MEDIUM | MEDIUM | $24.96 | $39.13 | $44.65 | EARLY SIGNAL | HIGH | HIGH | LOW | LOW APPARENT | RESEARCH MORE |
| #15 | 70 | baptism ornament | Printful Ceramic Ornament, 2-side (#900) | 2.9k | 31.4k | 0.092 | T | not shown | MEDIUM | MEDIUM | $13.62 | $26.6 | $32.12 | EVERGREEN | MEDIUM | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #16 | 68 | custom dog shirt | Printful Bella+Canvas 3001 tee (#71) | 7.3k | 136.6k | 0.053 | VH | not shown | HIGH | LOW | $16.87 | $30.19 | $35.71 | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #17 | 67 | pregnancy ornament | Printful Ceramic Ornament, 2-side (#900) | 1.7k | 19.3k | 0.088 | L | not shown | MEDIUM | MEDIUM | $13.62 | $26.6 | $32.12 | EARLY SIGNAL | HIGH | HIGH | LOW | LOW APPARENT | RESEARCH MORE |
| #18 | 67 | cat memorial ornament | Printful Ceramic Ornament, 2-side (#900) | 3.2k | 46.7k | 0.069 | L | not shown | MEDIUM | MEDIUM | $13.62 | $26.6 | $32.12 | EVERGREEN | MEDIUM | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #19 | 66 | personalized bookmark | Bookmark (no Printful product; supplier NOT VERIFIED) | 6.5k | 34.2k | 0.19 | VH | not shown | LOW | HIGH | NOT VERIFIED | - | - | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #20 | 64 | client gift | Printful Ceramic Ornament, 2-side (#900) | 15.9k | 21.1k | 0.754 | VL | not shown | LOW | MEDIUM | $13.62 | $26.6 | $32.12 | EARLY SIGNAL | MEDIUM | MEDIUM | HIGH | LOW APPARENT | RESEARCH MORE |
| #21 | 64 | personalized grandma sweatshirt | Printful Gildan 18000 + sleeve print (#145) | 645 | 30.7k | 0.021 | VH | not shown | HIGH | LOW | $33.91 | $49.02 | $54.54 | EARLY SIGNAL | MEDIUM | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #22 | 64 | custom embroidered sweatshirt | Printful Gildan 18000, embroidery left chest (#145) | 11k | 111.2k | 0.099 | T | not shown | HIGH | LOW | $30.91 | $45.7 | $51.23 | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #23 | 63 | uncle mug | Printful White Glossy Mug 15oz (#19) | 591 | 8.6k | 0.069 | H | not shown | MEDIUM | MEDIUM | $15.40 | $28.56 | $34.09 | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #24 | 62 | turkey trot shirt | Printful Bella+Canvas 3001 tee (#71) | 878 | 5.4k | 0.163 | VL | not shown | LOW | MEDIUM | $16.87 | $30.19 | $35.71 | VERIFIED CURRENT TREND | HIGH | HIGH | LOW | LOW APPARENT | RESEARCH MORE |
| #25 | 62 | nurse sweatshirt | Printful Gildan 18000 crewneck, front print (#145) | 17.1k | 160.8k | 0.106 | L | not shown | HIGH | LOW | $27.96 | $42.44 | $47.97 | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #26 | 61 | new grandma mug | Printful White Glossy Mug 15oz (#19) | 405 | 28.2k | 0.014 | VH | not shown | HIGH | LOW | $15.40 | $28.56 | $34.09 | EVERGREEN | LOW | LOW | HIGH | LOW APPARENT | RESEARCH MORE |
| #27 | 59 | family christmas shirts | Printful Bella+Canvas 3001 tee (#71) | 6.1k | 121k | 0.05 | L | +17.5% | HIGH | LOW | $16.87 | $30.19 | $35.71 | VERIFIED CURRENT TREND | HIGH | HIGH | LOW | LOW APPARENT | RESEARCH MORE |
| #28 | 57 | christmas tree skirt | Printful Christmas Tree Skirt (#1427) | 7.2k | 14.5k | 0.497 | VL | not shown | LOW | MEDIUM | $51.74 | $68.72 | $74.24 | EARLY SIGNAL | HIGH | HIGH | LOW | LOW APPARENT | RESEARCH MORE |

TSV sürümü: `data/opportunities_copy.tsv` · Detaylı kartlar (master prompt'taki 20. bölüm formatında): `opportunities.md`

## Uyarılar
- Hiçbir fırsat için satış tahmini yapılmadı. "Evidence supports testing" anlamında okunmalı.
- IP sonuçları yalnızca bir ön eleme. Her listing metni yayından önce USPTO'da ve Google'da birebir aranmalı.
- Fotoğraf tabanlı ürünlerde alıcının fotoğraf hakkı olmalı. Üretim ortağı (Printful) Etsy'de beyan edilmeli. Nihai görselde AI kullanılırsa AI beyanı gerekir.
