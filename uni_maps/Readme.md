# KYK Yurtları Tespit ve Listeleme Aracı

Bu Python projesi, Türkiye'deki üniversitelerin çevresinde bulunan KYK yurtlarını tespit eder. Google Maps API kullanarak üniversitelerin konum bilgileri alınır ve 30 km yarıçapındaki "KYK yurdu" anahtar kelimesine sahip yerler sorgulanır. Sonuçlar her üniversite için ayrı bir Excel dosyasına kaydedilir.

## 🔧 Özellikler

- Üniversitenin konumunu (enlem, boylam) Geocoding API ile alma
- Google Places API kullanarak KYK yurtlarını arama
- Sonuçları Excel (`.xlsx`) dosyası olarak dışa aktarma
- Üniversiteler listesi üzerinde toplu işleme imkanı

## 📦 Gereksinimler

Aşağıdaki kütüphanelerin kurulu olması gereklidir:

```bash
pip install requests pandas openpyxl
```

> Not: `openpyxl`, pandas'ın Excel'e yazma işlemi için gereklidir.

## 🗝️ Google API Key Alımı

1. [Google Cloud Console](https://console.cloud.google.com/) adresine gidin.
2. Yeni bir proje oluşturun veya mevcut bir projeyi kullanın.
3. **Geocoding API** ve **Places API** servislerini etkinleştirin.
4. API anahtarınızı oluşturun ve aşağıdaki kod bloğunda `API_KEY` kısmına yapıştırın.

## 📂 Kodun Kullanımı

Kodun başlangıcında `API_KEY` alanını kendi anahtarınızla doldurun:

```python
API_KEY = "BURAYA_OWN_GOOGLE_API_KEY_YAZ"
```

Kod tüm üniversite listesini döner ve her üniversite için:

- Konum bilgisi alır
- Yakın KYK yurtlarını sorgular
- Sonuçları şu formatta bir Excel dosyasına kaydeder:  
  `universite-adi_KYK_Yurtlari.xlsx`

## 📝 Çıktı Dosya Formatı

Her Excel dosyası şu sütunlara sahiptir:

| Üniversite | Üniversite Enlem | Üniversite Boylam | KYK Yurdu İsmi | KYK Yurdu Adresi | KYK Yurdu Enlem | KYK Yurdu Boylam |
|------------|------------------|-------------------|----------------|------------------|------------------|------------------|

> Eğer üniversite konumu bulunamazsa atlanır.  
> Eğer yurt bulunamazsa yine de dosya oluşturulur, yurt bilgileri `None` olur.

## 🚨 Dikkat Edilmesi Gerekenler

- Google API’lerinin ücretsiz sürümünde **günlük kota sınırı** vardır.
- Çok sayıda üniversite tarandığı için bazı API çağrıları kota aşımına neden olabilir.
- API anahtarınızın hem **Geocoding** hem de **Places API** için etkin olduğundan emin olun.
- Bazı KYK yurtları Google haritada “KYK yurdu” anahtar kelimesiyle listelenmeyebilir.

## 💡 Geliştirme Önerileri

- Sonuçları tek bir Excel dosyasında birleştirme
- Tüm sonuçları haritada görselleştirme (örneğin: `folium` veya `gmaps`)
- KYK dışındaki özel yurtları da kapsama alma
- Sonuçlara uzaklık bilgisi ekleme (üniversiteye olan mesafe)

geliştirebilir ve paylaşabilirsiniz.
