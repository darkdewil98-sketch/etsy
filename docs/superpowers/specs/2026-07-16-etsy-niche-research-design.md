# Etsy Ürün/Niş Araştırma Motoru — Tasarım

**Tarih:** 2026-07-16
**Durum:** Onaylandı, uygulama planına geçilecek
**Kapsam:** Etsy tam otomasyon pipeline'ının 1. alt sistemi (araştırma aşaması)

## Bağlam

Kullanıcı, Etsy'de önce organik sonra reklamla desteklenen ürün satışı için uçtan uca bir otomasyon
pipeline istiyor: (1) ürün/niş araştırması, (2) Canva MCP + Claude Code ile tasarım/mockup üretimi,
(3) Etsy'e toplu listing yükleme, (4) reklam otomasyonu. Bu dört alt sistem birbirinden bağımsız
olduğu için ayrı ayrı tasarlanıp inşa edilecek. Bu doküman yalnızca **1. alt sistemi** (araştırma) kapsar.

## Amaç ve Kapsam

Haftalık olarak otomatik çalışan, POD kategorilerinde (giyim, ev/dekor, dijital indirilebilir ürünler)
**gerçek veriye dayalı** (tahmini değil), düşük rekabetli/yükselen niş fırsatlarını tespit eden bir sistem.
Çıktı hem insan tarafından okunabilir bir CSV/Excel raporu, hem de pipeline'ın sonraki aşamasının
(Canva mockup üretimi) tüketeceği JSON dosyası olarak üretilir.

**Bu aşamada YOK (ayrı spec'lere ertelendi):**
- Etsy resmi API entegrasyonu — kullanıcının henüz API key/OAuth'u yok, başvuru sürecinde.
  Bu tasarımda yalnızca bir adaptör arayüzü/stub olarak yer tutulacak.
- Etsy sayfalarının scraping'i — ToS riski nedeniyle bilinçli olarak dışarıda bırakıldı.
- Mockup/tasarım üretimi, listing yükleme, reklam otomasyonu — ayrı alt sistemler.

## Veri Kaynakları ve Prensip

- **Google Trends** (`pytrends` kütüphanesi üzerinden): gerçek, ölçülen arama ilgisi verisi.
- **Etsy API** (gelecekte, onay sonrası): gerçek listing sayısı / rekabet verisi.
- **Prensip:** Skorlama tamamen deterministik ve veriye dayalıdır. AI hiçbir şekilde "bu ürün trend
  olur" gibi bir tahmin üretmez; yalnızca gerçek kaynaklardan çekilen sayısal verilerle hesaplama yapar.

## Mimari ve Bileşenler

Teknoloji: **Python** (Google Trends erişimi, veri işleme, CSV/JSON çıktısı için olgun ekosistem;
Windows Task Scheduler ile kolay zamanlama).

1. **Seed Keyword Config** (`seeds.yaml`)
   Her kategori için birkaç geniş başlangıç terimi içerir (ör. giyim: "t-shirt design", "hoodie print";
   ev/dekor: "wall art", "mug design"; dijital: "planner printable", "svg bundle"). Elle bakım
   gerektirmez — yeni nişler otomatik keşfedilir (bkz. Trends Client).

2. **Trends Client** (`trends_client.py`)
   `pytrends` ile Google Trends'e bağlanır. Her seed terim için:
   - Zaman içindeki ilgi trendini çeker (gerçek sayısal büyüme/düşüş).
   - "Related/Rising Queries" ile o seed'e bağlı yükselen alt-nişleri otomatik keşfeder.
   - Rate-limit'e karşı exponential backoff ve istekler arası bekleme içerir.

3. **Etsy Data Adapter** (`etsy_adapter.py`)
   Şimdilik `NotAvailable` döndüren bir arayüz/stub. Etsy API onayı gelince gerçek listing
   sayısı/rekabet verisi bu adaptör üzerinden entegre edilecek; diğer bileşenler değişmeyecek.

4. **Scorer** (`scorer.py`)
   Deterministik formül: `fırsat_skoru = trend_büyüme_oranı × trend_hacim_normalize`.
   Etsy verisi eklendiğinde rekabet terimi de formüle girecek (ör. `/ listing_sayısı`).

5. **Report Writer** (`report_writer.py`)
   Skorlanmış sonuçları hem `reports/YYYY-WW.csv` (insan için) hem `data/opportunities.json`
   (sonraki pipeline aşaması için) olarak yazar.

6. **Orchestrator** (`run_research.py`)
   Yukarıdaki bileşenleri sırayla çalıştıran ana script. Windows Task Scheduler ile haftalık
   tetiklenecek.

## Veri Akışı

```
seeds.yaml → Trends Client (pytrends: trend + rising queries)
           → [gelecekte: Etsy Adapter → gerçek listing/rekabet]
           → Scorer (deterministik formül)
           → Report Writer → reports/*.csv + data/opportunities.json
```

## Hata Yönetimi

- Google Trends rate-limit'e (429) çarparsa: exponential backoff ile yeniden dener; tamamen
  başarısız olursa yalnızca o seed atlanır, tüm çalışma durmaz.
- Bir seed için veri gelmezse (ör. çok niş terim), sıfır/None olarak işaretlenir; rapor yine
  üretilir (kısmi sonuç, sessiz çökme yok).
- Her çalışma `logs/YYYY-WW.log` dosyasına özet yazar: kaç seed tarandı, kaç yeni fırsat bulundu,
  kaç hata oluştu.

## Zamanlama

Haftalık, Windows Task Scheduler üzerinden `run_research.py` tetiklenir.

## Test Stratejisi

- `scorer.py`: sahte/sabit trend verisiyle birim testleri — formülün doğru hesapladığını
  doğrular, gerçek ağ çağrısı yapmaz.
- `trends_client.py`: gerçek Google Trends'e karşı tek seferlik manuel smoke test — otomatik
  CI'da çalıştırılmaz (rate-limit riski nedeniyle).

## Sonraki Alt Sistemler (bu spec'in kapsamı dışında)

1. Canva MCP + Claude Code ile tasarım/mockup üretimi — `data/opportunities.json`'ı girdi alacak.
2. Etsy'e toplu listing yükleme — Etsy API onayı gerektirir.
3. Reklam otomasyonu (Etsy Ads) — organik satış verisine dayalı.
