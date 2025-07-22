import requests

API_KEY = ''  # Google API anahtarını buraya koy

def get_place_photo(university_name):
    # 1. Place ID almak için textsearch kullanıyoruz
    search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    search_params = {
        'query': university_name,
        'key': API_KEY
    }
    search_response = requests.get(search_url, params=search_params)
    search_data = search_response.json()

    if not search_data.get('results'):
        print("Place bulunamadı.")
        return

    place_id = search_data['results'][0]['place_id']

    # 2. Place Details ile fotoğraf referansı al
    details_url = 'https://maps.googleapis.com/maps/api/place/details/json'
    details_params = {
        'place_id': place_id,
        'fields': 'photos',
        'key': API_KEY
    }
    details_response = requests.get(details_url, params=details_params)
    details_data = details_response.json()

    photos = details_data.get('result', {}).get('photos')
    if not photos:
        print("Fotoğraf bulunamadı.")
        return

    photo_ref = photos[0]['photo_reference']

    # 3. Fotoğrafı çek
    photo_url = f'https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={photo_ref}&key={API_KEY}'
    photo_response = requests.get(photo_url)

    if photo_response.status_code == 200:
        with open('universite_fotografi.jpg', 'wb') as f:
            f.write(photo_response.content)
        print("Fotoğraf kaydedildi: universite_fotografi.jpg")
    else:
        print("Fotoğraf çekilirken hata oluştu.")

if __name__ == "__main__":
    get_place_photo("Bursa Uludağ Üniversitesi")
