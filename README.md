# Web Kazıma (Scraping) Projelerim

Google Places/Maps API ve doğrudan HTML kazıma yöntemleriyle veri toplayan küçük web scraping betiklerinin bulunduğu repo.

## İçindekiler

| Dosya / Klasör | Açıklama |
|---|---|
| [`foto.py`](foto.py) | Google Places API ile bir üniversitenin/mekânın yer fotoğrafını çeken betik. |
| [`puan.py`](puan.py) | `universities.json` listesindeki üniversite adlarını işleyip, web kazıma ile puan/sıralama verisi toplayarak sonuçları pandas ile dışa aktaran betik. |
| [`uni_maps/`](uni_maps) | Türkiye'deki üniversitelerin çevresindeki KYK yurtlarını Google Maps API ile tespit edip Excel'e aktaran araç. Detaylar için [alt klasördeki README](uni_maps/Readme.md)'ye bakın. |

## Kurulum

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

Google API kullanan betikler için kendi `API_KEY` değerinizi ilgili dosya içine girmeniz gerekir (Geocoding API + Places API etkin olmalı).
