import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os
import time

# JSON dosyasını oku
with open('universities.json', 'r', encoding='utf-8') as f:
    slug_list = json.load(f)

# "universitesi" kelimesine kadar olan kısmı al
uni_names = []
for slug in slug_list:
    parts = slug.split('-')
    if 'universitesi' in parts:
        idx = parts.index('universitesi')
        uni_name = '-'.join(parts[:idx + 1])  # "universitesi" dahil
        uni_names.append(uni_name)
    else:
        uni_names.append(slug)  # Eğer "universitesi" yoksa tüm slug'ı al

# Excel dosyalarının kaydedileceği klasör
os.makedirs('uni_excel', exist_ok=True)

# Her üniversite için tabloyu çek ve kaydet
for i, uni_slug in enumerate(uni_names):
    url = f'https://www.universitego.com/{uni_slug}-2024-taban-puanlari-ve-basari-siralamalari/'
    print(f"🔍 Veri çekiliyor: {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')

        if not table:
            print(f"⚠ Tablo bulunamadı: {uni_slug}")
            continue

        rows = table.find_all('tr')
        data = []
        for row in rows[1:]:  # Başlık satırını atla
            cols = row.find_all('td')
            cols = [col.text.strip().replace('\xa0', ' ') for col in cols]
            data.append(cols)

        # Başlık kontrolü (tabloda eksik sütun olabilir)
        max_cols = max(len(row) for row in data)
        columns = ['Üniversite Adı', 'Bölüm', 'Puan Türü', 'Kontenjan (2023-20)', 'Taban Puanı (2023-20)', 'Başarı Sırası (2023-20)']
        df = pd.DataFrame(data, columns=columns[:max_cols])

        # Dosya adını belirle
        dosya_adi = f'uni_excel/{uni_slug}.xlsx'
        df.to_excel(dosya_adi, index=False)
        print(f"✅ Kaydedildi: {dosya_adi}")

    except Exception as e:
        print(f"❌ Hata oluştu ({uni_slug}): {e}")

    time.sleep(1)  # Sunucuyu yormamak için bekle

print("✅ Tüm işlemler tamamlandı.")
