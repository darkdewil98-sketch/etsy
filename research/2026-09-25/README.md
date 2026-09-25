# Etsy POD ikincil veri araştırması — 25 Eylül 2026

**Kapsam:** Master prompt'taki "3. seçenek". Bu bir Etsy talep analizi **değildir**. Marketplace Insights
ve Etsy arama sayfalarına bu ortamdan erişilemedi (Etsy 403 döndü, satıcı oturumu yok). Burada yalnızca
**ikincil** kanıtlar var:

1. Google Trends (ABD, web araması): mevsimsellik, zirve zamanı, büyüme, yükselen sorgular
2. Printful herkese açık katalog API'si ve kargo sayfası: doğrulanmış taban maliyet ve ABD kargo ücreti
3. USPTO marka veritabanı (tmsearch): aday ifadeler için canlı marka taraması
4. Etsy ücretleri: Etsy'nin kendi sayfası 403 verdi, rakamlar yalnızca üçüncü taraf kaynaklardan

Hiçbir Etsy arama hacmi, ilan sayısı, fiyat ya da satış rakamı bu raporda yok. Bunlar Marketplace
Insights verisi gelene kadar **NOT VERIFIED**.

Erişilemeyen kaynaklar: Etsy (arama, `/market`, Seller Handbook, yardım/ücret sayfaları), Gelato
fiyat sayfası (403), Printify katalog (fiyat verisi olmayan JS sayfası), Printful kargo API'si (yetki
gerekiyor).

---

## 1. Google Trends bulguları

### Veri kalitesi uyarısı (önemli)

5 yıllık ABD verisinde **Şubat–Haziran 2026 arasında tüm terimlerde aynı anda 3–7 katlık ani bir
sıçrama** var, sonra Temmuz 2026'da eski seviyeye dönüyor. Örneğin `custom sweatshirt` için haftalık
değerler 2026-04-05'te 95, 2026-07-12'de 5. Bu, gerçek talep değil, Google Trends veri anomalisi. Bu yüzden:

- Mevsimsellik ve seviye **Eyl 2021 – Ara 2025** (temiz dönem) verisinden hesaplandı.
- Güncel büyüme yalnızca **Tem–Eyl 2026'nın Tem–Eyl 2025 ile** karşılaştırılmasıyla ölçüldü.
- Ham grup medyanı 5'in altındaki terimler düşük çözünürlüklü. Oranları gösterge niteliğinde, kesin değil.

### Yöntem

- ABD, tüm kategoriler, haftalık. 11 grup × 5 terim. Her grupta referans terim `custom sweatshirt`.
- **Endeks:** referansın 2023–2025 ortalaması = 100. Gruplar arası karşılaştırma bu referansla ölçeklendi.
- **Kas–Ara / Q3:** 2025 Kasım–Aralık ortalamasının 2025 Temmuz–Eylül ortalamasına oranı (Q4 kaldıracı).
- **2x rampa:** 2025'te değerin ilk kez Q3 ortalamasının 2 katını geçtiği hafta.
- Tekrar üretmek için: `scripts/trends_pull.py` (5 yıllık), aynı betik `timeframe="2021-09-01 2025-12-31"`
  ile (temiz dönem), `scripts/trends_analyze.py`.

### Tablo (endekse göre sıralı, seçilmiş terimler)

| Terim | Endeks 2023–25 | 2025 / 2024 | Kas–Ara / Q3 | Zirve haftaları 2022/23/24/25 | 2x rampa (2025) | Q3'26 / Q3'25 | Sinyal |
|---|---|---|---|---|---|---|---|
| custom hoodie | 540 | +2% | 2.1x | 12-04/12-03/12-01/12-07 | 11-09 | +7% | Yaygın, genel baskı terimi |
| fishing gift | 295 | **+42%** | 2.9x | 12-11/12-10/12-08/12-14 | 11-23 | **+14%** | Büyüyen hobi + Q4 |
| pet portrait | 271 | +18% | 1.8x | 11-27/11-26/12-01/12-07 | 11-23 | +10% | Kalıcı talep + Q4 artışı |
| pregnancy announcement | 162 | +24% | 1.6x | karışık | 09-14 | **−21%** | Q4'e bağlı değil |
| dad shirt | 127 | −7% | 1.3x | Haziran (her yıl) | – | 0% | Babalar Günü, Q4 değil |
| anniversary gift | 116 | −2% | 0.7x | Haz–Ağu | – | −6% | Mevsimsel değil |
| custom mug | 101 | +9% | 2.4x | Aralık başı | 11-23 | **+19%** | Kalıcı talep + Q4 |
| custom sweatshirt (referans) | 100 | +1% | 2.2x | 12-04/12-03/12-08/11-30 | 11-02 | +5% | Kalıcı talep + Q4 |
| personalized blanket | 93 | +1% | 2.2x | Aralık başı | 11-09 | +1% | Kalıcı talep + Q4 |
| personalized ornament | 89 | +1% | **8.8x** | 12-04/12-03/12-01/11-30 | **09-28** | +36%* | Güçlü Q4, **rampa şimdi başlıyor** |
| boss gift | 89 | +14% | 4.1x | 12-11/12-17/12-15/12-14 | **10-12** | −3% | Q4 (Ekim ortası ilk sıçrama) |
| pet ornament | 78 | −10% | **20.5x** | Aralık başı | **09-21** | 0%* | Çok mevsimsel, rampa şimdi |
| gardening gift | 75 | **+52%** | 3.7x | Mayıs + Aralık | 11-16 | +150%* | Büyüyen, çift zirve |
| engagement gift | 71 | +34% | 1.2x | karışık | – | −5% | Mevsimsel değil |
| custom tumbler | 62 | −5% | 1.8x | Aralık başı | 11-16 | +26% | Kalıcı talep + Q4 |
| coworker gift | 60 | +18% | 3.4x | 12-11/12-10/12-15/12-07 | 11-09 | **+17%** | Büyüyen Q4 |
| teacher gift | 42 | +16% | 3.1x | Mayıs (her yıl) | 11-16 | +5% | Ana zirve Mayıs, Aralık ikincil |
| book lover gift | 37 | +26% | **55x** | Aralık | 10-19 | * | Neredeyse yalnızca Q4 |
| personalized apron | 32 | +22% | 4.7x | Aralık | 09-14 | * | Q4, düşük hacim |
| mama sweatshirt | 23 | **−34%** | 2.9x | Kas sonu/Ara | 11-09 | +5% | Düşüşte (+ marka riski, §3) |
| retirement gift | 20 | +24% | 1.6x | Mayıs; 2025'te 11-30 | 11-30 | +3% | Mayıs ağırlıklı |
| grandma gift | 12 | +5% | 4.1x | Aralık + Mayıs | 11-09 | −5% | Q4 + Anneler Günü |
| baby first christmas ornament | 9 | +11% | 11.7x | Kas sonu/Ara başı | **09-21** | −20%* | Çok mevsimsel, rampa şimdi |
| grandma sweatshirt | 6 | −7% | 14.1x | Aralık | 09-14 | * | Q4, düşük hacim |
| new home ornament | 5 | +16% | 19.1x | Kas sonu | **09-21** | * | Çok mevsimsel |
| stocking stuffers | 5 | +2% | 33.9x | Aralık ortası | 09-28 | * | Yalnızca Q4 |
| dog mom sweatshirt | 6 | **−48%** | – | – | – | – | Düşüşte |
| cat mom shirt | 4 | −33% | – | – | – | – | Düşüşte |

\* Düşük çözünürlük (ham grup medyanı < 5). Yüzde değişimler güvenilir değil.

Google Trends'te ölçülemeyecek kadar düşük hacimli terimler: `thanksgiving shirt`,
`family christmas shirts`, `couples ornament`, `memorial ornament`, `book club gift`, `bride sweatshirt`,
`bachelorette shirts`, `memorial gift`. **Bu, Etsy'de talep olmadığı anlamına gelmez.** Google verisi bu
terimler için yetersiz, Marketplace Insights'ta ölçülmeleri gerekir.

### Zamanlama çıkarımları (yalnızca Google verisi)

- **Süs/ornament ailesi:** 2x rampası geçen yıl 21–28 Eylül'de başladı ve zirve 30 Kasım – 4 Aralık
  haftasında geldi. Bugün 25 Eylül 2026, yani rampa başlamak üzere. Test için en dar zaman penceresi bu aile.
- **Boss gift:** ilk sıçrama 12 Ekim civarı (muhtemelen Boss's Day), ana zirve Aralık ortası.
- **Coworker, fishing, pet portrait, custom mug/sweatshirt/blanket:** rampa Kasım başı–ortası, zirve Aralık başı.
- **Teacher ve retirement gift:** asıl zirve Mayıs. Q4 ikincil ama evergreen potansiyeli yüksek.
- **Mama / dog mom / cat mom giyim:** yıllık düşüşte (−34% / −48% / −33%).

### Yükselen sorgular (son 3 ay, ABD) — IP filtresinden geçenler

Marka içeren veya konu dışı sorgular çıkarıldı: Walgreens, CVS, Yeti, Stanley, Caden Lane, Hugo Boss,
Marc Jacobs, Blick, YSL, Custom Ink ve "pet care tips", "museums" gibi alakasız sorgular.

| Kök | Yükselen / öne çıkan (IP-temiz) | Not |
|---|---|---|
| personalized ornament | personalized christmas ornaments (+750%), baby's first christmas ornament personalized (+350%), personalized photo ornament, personalized family ornament, dog ornament personalized | Fotoğraf, aile ve evcil hayvan kişiselleştirmesi öne çıkıyor |
| custom sweatshirt | mockneck sweatshirt (+250%), custom embroidery (+140%), custom pet sweatshirt | **"etsy" sorgusu +450%** |
| personalized blanket | personalized baby blankets (+300%), personalized blanket with pictures (+150%), personalized name blanket, personalized dog blanket | **"etsy" sorgusu +300%** |
| custom tumbler | custom tumbler with pictures (+140%) | Kalan yükselenlerin çoğu marka (reddedildi) |
| custom mug | custom mug with picture, personalized mug | Yükselenlerin çoğu "near me" ve eczane zincirleri |
| mama sweatshirt | mama sweatshirt with names on sleeve, boy mama sweatshirt, with baby clothes | Marka riski için §3'e bakın |
| grandma gift | new grandma gift ideas (+140%), personalized gift for grandma, christmas gift for grandma | |
| retirement gift | retirement gift for women / woman (birden fazla yükselen), retirement gift ideas for mom / for men | Kadın alıcıya yönelik güçlü sinyal |
| coworker gift | coworker christmas gift ideas (+120%), coworker leaving/going away gift | |
| teacher gift | halloween teacher gift (+130%), teacher christmas / appreciation | |
| boss gift | gift for male boss (+90%), boss day gift | |
| nurse gift | nurse gift basket ideas (+350%), graduation gift for nurse | |

---

## 2. Tedarikçi maliyetleri (Printful, 25.09.2026, canlı)

- **Taban fiyat:** `api.printful.com/products/{id}` (herkese açık katalog). Standart ön baskı dahil
  (API'de ek ücreti yok). Diğer baskı alanları ek ücretli, örneğin sweatshirt kolu +$5.95, arka +$5.95,
  nakış göğüs +$2.95.
- **Kargo:** `printful.com/shipping` sayfasındaki ABD sabit ücretleri, ham HTML'den okundu. Not: otomatik
  özetleyici sweatshirt/hoodie kargosunu yanlış satırdan okumuştu. Ham metne göre standart giyimde
  **$8.79**; $8.29 olan satır "all-over print" giyime ait.
- Printify ve Gelato fiyatları: **SUPPLIER COST NOT VERIFIED**.

### Birim ekonomisi

Varsayımlar:
- Ücretsiz kargo: alıcı yalnızca ürün fiyatını öder, kargoyu satıcı üstlenir.
- Etsy ücretleri: %6.5 işlem + %3 + $0.25 ödeme işleme + $0.20 listeleme (üçüncü taraf kaynaklar, §4).
- Dahil değil: offsite ads, indirimler, satış vergisinin ödeme ücretine etkisi.

Formül: `fiyat = (hedef katkı + maliyet + 0.45) / 0.905`

| Ürün (Printful ID) | Taban | ABD kargo (ilk / ek) | Maliyet | Başabaş fiyat | $10 katkı için | $15 katkı için |
|---|---|---|---|---|---|---|
| Sweatshirt Gildan 18000 (145) | $19.17 | $8.79 / +$2.50 | $27.96 | $31.39 | $42.44 | $47.97 |
| + kol baskısı (isim kolda) | $25.12 | $8.79 / +$2.50 | $33.91 | $37.97 | $49.02 | $54.54 |
| Sweatshirt Comfort Colors 1566 (839) | $30.59 | $8.79 / +$2.50 | $39.38 | $44.01 | $55.06 | $60.59 |
| Hoodie Gildan 18500 (146) | $22.63 | $8.79 / +$2.50 | $31.42 | $35.22 | $46.27 | $51.79 |
| T-shirt Bella+Canvas 3001 (71) | $11.92 | $4.95 / +$2.20 | $16.87 | $19.14 | $30.19 | $35.71 |
| T-shirt Comfort Colors 1717 (586) | $15.60 | $4.95 / +$2.20 | $20.55 | $23.20 | $34.25 | $39.78 |
| Çocuk sweatshirt 18000B (677) | $17.64 | $4.69 / +$2.00 | $22.33 | $25.17 | $36.22 | $41.75 |
| Bebek zıbın 100B (308) | $13.79 | $4.69 / +$2.00 | $18.48 | $20.92 | $31.97 | $37.49 |
| Kupa 11oz (19) | $6.07 | $6.69 / +$3.50 | $12.76 | $14.60 | $25.65 | $31.17 |
| Kupa 15oz (19) | $8.11 | $7.29 / +$4.00 | $15.40 | $17.51 | $28.56 | $34.09 |
| Kupa içi renkli 11oz (403) | $8.11 | $6.69 / +$3.50 | $14.80 | $16.85 | $27.90 | $33.43 |
| Seramik süs, tek yüz (881) | $6.34 | $5.49 / +$0.80 | $11.83 | $13.57 | $24.62 | $30.14 |
| Seramik süs, çift yüz (900) | $7.73 | $5.89 / +$0.70 | $13.62 | $15.55 | $26.60 | $32.12 |
| Metal yılbaşı süsü (901) | $4.61 | $5.89 / +$0.70 | $10.50 | $12.10 | $23.15 | $28.67 |
| Ahşap süs (634) | $8.37 | $5.19 / +$1.00 | $13.56 | $15.48 | $26.53 | $32.06 |
| Akrilik süs (793) | $7.80 | $5.49 / +$0.80 | $13.29 | $15.18 | $26.23 | $31.76 |
| Battaniye 50x60 (395) | $29.36 | $8.29 / +$2.50 | $37.65 | $42.10 | $53.15 | $58.67 |
| Sherpa battaniye 50x60 (711) | $35.76 | $13.99 / +$4.00 | $49.75 | $55.47 | $66.52 | $72.04 |
| Nakışlı sherpa 50x60 (536) | $46.82 | $13.99 / +$4.00 | $60.81 | $67.69 | $78.74 | $84.27 |
| Paslanmaz tumbler 20oz (909) | $24.97 | $6.69 / +$2.00 | $31.66 | $35.48 | $46.53 | $52.06 |
| Pipetli termos tumbler 20oz (742) | $20.76 | $6.69 / +$2.00 | $27.45 | $30.83 | $41.88 | $47.40 |
| Organik tote (367) | $15.87 | $4.69 / +$2.00 | $20.56 | $23.22 | $34.27 | $39.79 |
| Nakışlı önlük (297) | $17.64 | $4.69 / +$2.00 | $22.33 | $25.17 | $36.22 | $41.75 |
| Rustik yılbaşı çorabı (1428) | $17.17 | $7.79 / +$3.75 | $24.96 | $28.08 | $39.13 | $44.65 |
| Poster 12x12 (1) | $9.07 | $4.99 / +$0.40 | $14.06 | $16.03 | $27.08 | $32.61 |
| Kanvas 10x10 (3) | $16.83 | $6.79 / +$6.49 | $23.62 | $26.60 | $37.65 | $43.17 |
| Sticker 3x3 (358) | $2.34 | $4.49 / +$0.05 | $6.83 | $8.04 | $19.09 | $24.62 |

**Etsy'deki gerçek rakip fiyatları: NOT VERIFIED.** Bu tablo yalnızca "bu ürün en az kaça satılmalı"
sorusunu cevaplar. Bir ürünün bu fiyata satılıp satılamayacağı, Etsy ilk sayfa fiyatları gelince netleşir.

Maliyet gözlemleri (hesaplama, tahmin değil):
- Süslerde ek ürün kargosu çok düşük ($0.70–$1.00). Çoklu süs setleri, sipariş başına kargo payını
  belirgin şekilde azaltır.
- Sweatshirt'te "kolda isimler" kişiselleştirmesi maliyete $5.95 ekler (Gildan 18000'de $27.96 → $33.91).

---

## 3. USPTO marka taraması (25.09.2026, canlı, tmsearch)

Yöntem: kelime markasında (WM) tam ifade eşleşmesi, yalnızca canlı (alive) kayıtlar. İlgili sınıflar:
025 giyim, 021 kupa/bardak, 016 kâğıt/sticker, 024 tekstil/battaniye, 028 süs/oyuncak, 020 ev,
014 takı, 018 çanta. Ham sonuçlar `data/tm_results.csv` dosyasında.

**Yöntem uyarısı:** "merry and bright" aramasında 0 sonuç çıktı, ama "MERRY & BRIGHT" onlarca canlı
kayıt veriyor. "&" / "and", kesme işareti ve noktalama farkları yanlış negatif üretiyor. Çok yaygın
kelimelerde de (mama, nana, retirement) ilk 200 kayıt tarandı. Yani **"kayıt bulunamadı" sonucu
güvenli olduğu anlamına gelmez.** Bu yalnızca ilk eleme. Her finalist ifade yine elle kontrol edilmeli.

### Reddedilenler (ilgili sınıfta canlı tescil veya başvuru var)

| İfade | Kayıt | Sınıf / kapsam | Sonuç |
|---|---|---|---|
| **MAMA** | Reg. 8387670 (**11.08.2026**) | 025: tişört, sweatshirt, hoodie, şapka | Tek başına "MAMA" giyim tasarımı reddedildi (MEDIUM+). Etkisi: "mama sweatshirt" kümesi |
| MERRY & BRIGHT | Reg. 7459888 (024 battaniye), 7869231 (025 pijama), 3990175 (014 takı), 99724815 (025 çorap, başvuru) | 024 / 025 / 014 | Battaniye ve giyimde reddedildi |
| COOL AUNT | Reg. 7232375 | 025: tişört, sweatshirt | Reddedildi |
| OFFICIALLY RETIRED | Reg. 5201467 | 014 / 016 / 025 / 021 | Reddedildi |
| WORK BESTIE | Reg. 7024986 | 021: kupa, tumbler | Kupa ve tumblerda reddedildi |
| REEL COOL | Reg. 8317165 (23.06.2026) | 025 | Giyimde reddedildi ("Reel Cool Dad" dahil) |
| MY FIRST CHRISTMAS | Reg. 4530374 (025 bebek giyimi: önlük, patik, çorap, şapka), Reg. 2040424 (028 peluş) | 025 / 028 | Birebir ifade reddedildi. Bebek giyiminde kullanılmamalı |
| GLAMMA | Reg. 4132245 | 014 takı, 018 çanta/tote | Tote ve takıda reddedildi |
| NANA / MIMI | Başvurular 99536254, 99914164 | 025 | Tek başına isim olarak kullanılmamalı |
| GIGI | Birden fazla kayıt (018 / 020 / 016 / 021 / 024) | çeşitli | Tek başına kullanılmamalı |
| BOOKISH (+ BOOKISH AF vb.) | 9 canlı kayıt | çeşitli | Kalabalık alan, kaçınılmalı |
| "... era" kalıbı | IP marka kaydı değil | – | Belirgin bir ünlü/tur çağrışımı var. Prompt'taki IP filtresine göre reddedildi |

### İlk elemeden geçenler (ilgili sınıflarda canlı birebir kayıt bulunamadı)

`boy mama`, `girl mama`, `dog mama`, `cat mom`, `cat mama`, `aunt life`, `grandma est`, `grandma life`,
`new grandma`, `baby's first christmas`, `our first christmas`, `first christmas married`,
`our first home`, `retired not my problem anymore`, `teacher off duty`, `teach love inspire`,
`teacher life`, `crazy plant lady`, `just one more chapter`, `coffee lover`, `mama claus`, `mom est`,
`dad est`, `grandpa est`, `retirement squad`.

Bu ifadeler en fazla **LOW APPARENT IP RISK adayı** sayılabilir. Google'da birebir aranmadı, Etsy'de
kontrol edilemedi, ayrıca "&" varyantları ve tasarım (logo) markaları ayrıca taranmalı. Ek not:
`dog mom` içeren 8 canlı kayıt var (DOG MOM SOCIAL CLUB, CERTIFIED DOG MOM vb.). "Dog mom" kalıbı
Google'da da düşüşte (−48%).

---

## 4. Etsy ücretleri

Etsy'nin kendi ücret ve yardım sayfaları bu ortamdan 403 verdi. Aşağıdaki rakamlar **üçüncü taraf**
kaynaklardan (Printify blog, Craftybase, SellerFeeCalc vb.), resmi olarak doğrulanmadı:

- $0.20 listeleme ücreti (her satışta yeniden)
- %6.5 işlem ücreti (ürün + kargo + hediye paketi toplamı üzerinden)
- ABD ödeme işleme ücreti: %3 + $0.25
- Offsite Ads: yıllık $10.000 üzeri satıcılar için zorunlu. **Oranı NOT VERIFIED**, tabloya dahil edilmedi.

Etsy'nin 21.05.2026 tarihli SEC 8-K dosyası ücret değişikliği içermiyor (Depop satışıyla ilgili).

---

## 5. Marketplace Insights için önerilen 15 arama

Marketplace Insights linki (her zaman bunu kullanın):
https://www.etsy.com/your/shops/me/marketplace-insights?ref=seller-platform-mcnav

Bu sıralama yalnızca yukarıdaki ikincil kanıtlara dayanıyor: zamanlama, büyüme ve marka elemesi. Etsy
talebini varsaymıyor, sadece haftalık aramaların nereye harcanacağını öneriyor.

| # | Arama | Neden | Tür |
|---|---|---|---|
| 1 | personalized ornament | Ornament ailesinin kökü. Rampa 21–28 Eylül'de başlıyor, Kas–Ara/Q3 = 8.8x | Keşif |
| 2 | dog ornament personalized | Yükselen alt sorgu. Pet ornament Q4 kaldıracı 20.5x | Keşif |
| 3 | baby's first christmas ornament | +350% yükselen. "My First Christmas" ifadesinden kaçının | Keşif |
| 4 | new home ornament | Q4 kaldıracı 19.1x, 2025/2024 +16% | Keşif |
| 5 | personalized photo ornament | Öne çıkan alt sorgu, kişiselleştirme odaklı | Keşif |
| 6 | boss gift | Ekim ortası ilk sıçrama, 2025/2024 +14% | Keşif |
| 7 | coworker christmas gift | Yükselen (+120%). Coworker gift Q3 +17% | Keşif |
| 8 | fishing gift | En güçlü büyüme (2025/2024 +42%, Q3 +14%), yüksek hacim | Keşif |
| 9 | gardening gift | 2025/2024 +52%, çift zirve (Mayıs + Aralık) | Keşif |
| 10 | custom pet portrait | Kalıcı talep (+18%) + Q4 artışı, yüksek hacim | Keşif |
| 11 | retirement gift for women | Birden fazla yükselen sorgu, evergreen (Mayıs zirvesi) | Keşif |
| 12 | new grandma gift | Yükselen (+140%), "grandma" kümesinin girişi | Keşif |
| 13 | teacher christmas gift | Aralık ikincil zirve, "halloween teacher gift" yükseliyor | Doğrulama |
| 14 | personalized christmas stocking | Q4, düşük ek kargo, Google verisi yetersiz | Doğrulama |
| 15 | personalized blanket with pictures | Yükselen (+150%). "etsy" sorgusu bu kategoride +300% | Doğrulama |

Her arama için şu değerler kaydedilmeli: aylık arama sayısı, ilan sayısı, ilgili aramalar, ayrıca 1.
sayfadaki fiyat aralığı ve yorum sayıları (ekran görüntüsü yeterli). Bu veri gelince master prompt'taki
tam puanlama (Bölüm 19–22) bu klasördeki maliyet ve marka verisiyle birleştirilecek.

---

## Dosyalar

- `data/trends_5y.csv`: ham 5 yıllık Trends (anomali dahil)
- `data/trends_clean.csv`: Eyl 2021 – Ara 2025 temiz dönem
- `data/trends_summary.csv`: hesaplanmış metrikler
- `data/rising.json`: 15 kök için yükselen ve öne çıkan sorgular (ham, filtresiz)
- `data/printful_unit_economics.csv`: maliyet ve fiyat tabanları
- `data/tm_results.csv`: USPTO ilk eleme sonuçları
- `scripts/`: veriyi yeniden üretmek için kullanılan betikler

## Kaynaklar

- Google Trends (pytrends), ABD, 25.09.2026'da çekildi
- Printful katalog API'si: https://api.printful.com/products , kargo: https://www.printful.com/shipping
- USPTO Trademark Search: https://tmsearch.uspto.gov/
- Etsy ücretleri (üçüncü taraf): https://printify.com/blog/how-much-does-etsy-take-per-sale/ ,
  https://craftybase.com/blog/the-complete-guide-to-etsy-fees ,
  https://sellerfeecalc.com/blog/etsy-fees-explained-2026
- Etsy SEC 8-K (21.05.2026): https://www.sec.gov/Archives/edgar/data/0001370637/000137063726000054/etsy-20260521.htm
