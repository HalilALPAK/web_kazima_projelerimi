import requests
import pandas as pd

API_KEY = "" #API GİRMEN LAZIM 

def get_coordinates(place_name):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place_name}&key={API_KEY}"
    response = requests.get(url)
    results = response.json().get("results", [])
    if results:
        loc = results[0]["geometry"]["location"]
        return loc["lat"], loc["lng"]
    return None

def get_nearby_kyk_yurtlari(lat, lng):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lng}",
        "radius": 30000,
        "keyword": "KYK yurdu",
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    results = response.json().get("results", [])
    yurtlar = []
    for place in results:
        yurtlar.append({
            "isim": place["name"],
            "adres": place.get("vicinity", "Adres bilgisi yok"),
            "lat": place["geometry"]["location"]["lat"],
            "lng": place["geometry"]["location"]["lng"]
        })
    return yurtlar

# Üniversite listesi
universiteler = [
    "abdullah-gul-universitesi-agu",
    "acibadem-mehmet-ali-aydinlar-universitesi",
    "ada-kent-universitesi",
    "adana-alparslan-turkes-bilim-ve-teknoloji-universitesi-atu",
    "adiyaman-universitesi-adyu",
    "afyon-kocatepe-universitesi-aku",
    "afyonkarahisar-saglik-bilimleri-universitesi-afsu",
    "agri-ibrahim-cecen-universitesi-aicu",
    "akdeniz-karpaz-universitesi",
    "akdeniz-universitesi-akdu",
    "aksaray-universitesi-asu",
    "alanya-alaaddin-keykubat-universitesi-alku",
    "alanya-universitesi",
    "altinbas-universitesi",
    "amasya-universitesi",
    "anadolu-universitesi-anau",
    "ankara-bilim-universitesi",
    "ankara-haci-bayram-veli-universitesi-ahbvu",
    "ankara-medipol-universitesi",
    "ankara-muzik-ve-guzel-sanatlar-universitesi",
    "ankara-sosyal-bilimler-universitesi-asbu",
    "ankara-universitesi-au",
    "ankara-yildirim-beyazit-universitesi-aybu",
    "antalya-belek-universitesi",
    "antalya-bilim-universitesi",
    "ardahan-universitesi-aru",
    "arkin-yaratici-sanatlar-ve-tasarim-universitesi",
    "artvin-coruh-universitesi-acu",
    "ataturk-universitesi-atauni",
    "atilim-universitesi",
    "avrasya-universitesi",
    "aydin-adnan-menderes-universitesi-adu",
    "azerbaycan-devlet-pedagoji-universitesi",
    "bahcesehir-kibris-universitesi",
    "bahcesehir-universitesi",
    "balikesir-universitesi-baun",
    "bandirma-onyedi-eylul-universitesi-banu",
    "bartin-universitesi",
    "baskent-universitesi",
    "batman-universitesi-batu",
    "bayburt-universitesi-bayu",
    "istanbul-beykent-universitesi",
    "beykoz-universitesi",
    "bezm-i-alem-vakif-universitesi",
    "bilecik-seyh-edebali-universitesi-bseu",
    "bingol-universitesi-bu",
    "biruni-universitesi",
    "bitlis-eren-universitesi-beu",
    "bogazici-universitesi-boun",
    "bolu-abant-izzet-baysal-universitesi-aibu",
    "burdur-mehmet-akif-ersoy-universitesi-maku",
    "bursa-teknik-universitesi-btu",
    "bursa-uludag-universitesi",
    "cag-universitesi",
    "canakkale-onsekiz-mart-universitesi-comu",
    "cankaya-universitesi",
    "cankiri-karatekin-universitesi-caku",
    "cukurova-universitesi-cu",
    "demiroglu-bilim-universitesi",
    "dicle-universitesi-du",
    "dogu-akdeniz-universitesi",
    "dogus-universitesi",
    "dokuz-eylul-universitesi-deu",
    "duzce-universitesi-du",
    "ege-universitesi-eu",
    "erciyes-universitesi-eru",
    "erzincan-binali-yildirim-universitesi-ebyu",
    "erzurum-teknik-universitesi-etu",
    "eskisehir-osmangazi-universitesi-esogu",
    "eskisehir-teknik-universitesi-etu",
    "fatih-sultan-mehmet-vakif-universitesi",
    "fenerbahce-universitesi",
    "firat-universitesi-fu",
    "galatasaray-universitesi-gsu",
    "gazi-universitesi-gu",
    "gaziantep-islam-bilim-ve-teknoloji-universitesi",
    "gaziantep-universitesi-gaun",
    "gebze-teknik-universitesi-gtu",
    "giresun-universitesi-gru",
    "girne-amerikan-universitesi",
    "girne-universitesi",
    "gumushane-universitesi-gsu",
    "hacettepe-universitesi",
    "hakkari-universitesi",
    "halic-universitesi",
    "harran-universitesi",
    "hasan-kalyoncu-universitesi",
    "hatay-mustafa-kemal-universitesi-mku",
    "hitit-universitesi-hitu",
    "hoca-ahmet-yesevi-uluslararasi-turk-kazak-universitesi",
    "igdir-universitesi-igdu",
    "isparta-uygulamali-bilimler-universitesi-isubu",
    "isik-universitesi",
    "ibn-haldun-universitesi",
    "ihsan-dogramaci-bilkent-universitesi",
    "inonu-universitesi-inu",
    "iskenderun-teknik-universitesi-iste",
    "istanbul-29-mayis-universitesi",
    "istanbul-arel-universitesi",
    "istanbul-atlas-universitesi",
    "istanbul-aydin-universitesi",
    "istanbul-bilgi-universitesi",
    "istanbul-esenyurt-universitesi",
    "istanbul-galata-universitesi",
    "istanbul-gedik-universitesi",
    "istanbul-gelisim-universitesi",
    "istanbul-kent-universitesi",
    "istanbul-kultur-universitesi",
    "istanbul-medeniyet-universitesi-imu",
    "istanbul-medipol-universitesi",
    "istanbul-okan-universitesi",
    "istanbul-rumeli-universitesi",
    "istanbul-sabahattin-zaim-universitesi",
    "istanbul-saglik-ve-teknoloji-universitesi",
    "istanbul-teknik-universitesi-itu",
    "istanbul-ticaret-universitesi",
    "istanbul-topkapi-universitesi",
    "istanbul-universitesi-iu",
    "istanbul-universitesi-cerrahpasa-iuc",
    "istanbul-yeni-yuzyil-universitesi",
    "istinye-universitesi",
    "izmir-bakircay-universitesi",
    "izmir-demokrasi-universitesi-idu",
    "izmir-ekonomi-universitesi",
    "izmir-katip-celebi-universitesi-ikcu",
    "izmir-kavram-meslek-yuksekokulu",
    "izmir-tinaztepe-universitesi",
    "izmir-yuksek-teknoloji-enstitusu-universitesi-iytu",
    "kadir-has-universitesi",
    "kafkas-universitesi-kau",
    "kahramanmaras-istiklal-universitesi-kiu",
    "kahramanmaras-sutcu-imam-universitesi-ksu",
    "kapadokya-universitesi",
    "karabuk-universitesi-kbu",
    "karadeniz-teknik-universitesi-ktu",
    "karamanoglu-mehmetbey-universitesi-kmu",
    "kastamonu-universitesi-ku",
    "kayseri-universitesi-kayu",
    "kibris-amerikan-universitesi",
    "kibris-bati-universitesi",
    "kibris-ilim-universitesi",
    "kibris-saglik-ve-toplum-bilimleri-universitesi",
    "kirgizistan-turkiye-manas-universitesi",
    "kirikkale-universitesi-kku",
    "kirklareli-universitesi-klu",
    "kirsehir-ahi-evran-universitesi-kaeu",
    "kilis-7-aralik-universitesi-kiyu",
    "kocaeli-saglik-ve-teknoloji-universitesi",
    "kocaeli-universitesi-kou",
    "koc-universitesi",
    "konya-gida-ve-tarim-universitesi",
    "konya-teknik-universitesi-ktun",
    "kto-karatay-universitesi",
    "kutahya-dumlupinar-universitesi-dpu",
    "kutahya-saglik-bilimleri-universitesi-ksbu",
    "lefke-avrupa-universitesi",
    "lokman-hekim-universitesi",
    "malatya-turgut-ozal-universitesi-mtu",
    "maltepe-universitesi",
    "manisa-celal-bayar-universitesi-mcbu",
    "mardin-artuklu-universitesi-mau",
    "marmara-universitesi-mu",
    "mef-universitesi",
    "mersin-universitesi-meu",
    "mimar-sinan-guzel-sanatlar-universitesi-msgsu",
    "mudanya-universitesi",
    "mugla-sitki-kocman-universitesi-msku",
    "munzur-universitesi-munu",
    "mus-alparslan-universitesi-msu",
    "necmettin-erbakan-universitesi-neu",
    "nevsehir-haci-bektas-veli-universitesi-nevu",
    "nigde-omer-halisdemir-universitesi-ohu",
    "istanbul-nisantasi-universitesi",
    "nuh-naci-yazgan-universitesi",
    "ondokuz-mayis-universitesi-omu",
    "ordu-universitesi-odu",
    "orta-dogu-teknik-universitesi-odtu",
    "osmaniye-korkut-ata-universitesi-oku",
    "ostim-teknik-universitesi",
    "ozyegin-universitesi",
    "pamukkale-universitesi-pau",
    "piri-reis-universitesi",
    "rauf-denktas-universitesi",
    "recep-tayyip-erdogan-universitesi-rteu",
    "sabanci-universitesi",
    "saglik-bilimleri-universitesi-sbu",
    "sakarya-uygulamali-bilimler-universitesi",
    "sakarya-universitesi-sau",
    "samsun-universitesi-samu",
    "sanko-universitesi",
    "selcuk-universitesi-su",
    "siirt-universitesi-siu",
    "sinop-universitesi-snu",
    "sivas-bilim-ve-teknoloji-universitesi-sbtu",
    "sivas-cumhuriyet-universitesi-scu",
    "suleyman-demirel-universitesi-sdu",
    "sirnak-universitesi-su",
    "tarsus-universitesi",
    "ted-universitesi",
    "tekirdag-namik-kemal-universitesi-nku",
    "tobb-ekonomi-ve-teknoloji-universitesi",
    "tokat-gaziosmanpasa-universitesi-togu",
    "toros-universitesi",
    "trabzon-universitesi-tru",
    "trakya-universitesi-tu",
    "turk-hava-kurumu-universitesi",
    "turk-alman-universitesi-tau",
    "ufuk-universitesi",
    "uluslararasi-balkan-universitesi",
    "uluslararasi-final-universitesi",
    "uluslararasi-kibris-universitesi",
    "uluslararasi-saraybosna-universitesi",
    "usak-universitesi-uu",
    "uskudar-universitesi",
    "van-yuzuncu-yil-universitesi-yyu",
    "yakin-dogu-universitesi",
    "yalova-universitesi-yu",
    "yasar-universitesi",
    "yeditepe-universitesi",
    "yildiz-teknik-universitesi-ytu",
    "yozgat-bozok-universitesi-yobu",
    "yuksek-ihtisas-universitesi",
    "zonguldak-bulent-ecevit-universitesi-beun"
]
for uni in universiteler:
    print(f"{uni} için işlem yapılıyor...")
    coords = get_coordinates(uni)
    if coords is None:
        print(f"{uni} için konum bulunamadı.")
        continue
    
    uni_lat, uni_lng = coords
    yurtlar = get_nearby_kyk_yurtlari(uni_lat, uni_lng)

    # Eğer KYK yurdu bulunamazsa boş DataFrame oluşturuyoruz yine de
    if not yurtlar:
        df = pd.DataFrame([{
            "Üniversite": uni,
            "Üniversite Enlem": uni_lat,
            "Üniversite Boylam": uni_lng,
            "KYK Yurdu İsmi": None,
            "KYK Yurdu Adresi": None,
            "KYK Yurdu Enlem": None,
            "KYK Yurdu Boylam": None
        }])
    else:
        # Her KYK yurdu için bir satır, üniversite bilgileri tekrarlanacak
        data = []
        for yurt in yurtlar:
            data.append({
                "Üniversite": uni,
                "Üniversite Enlem": uni_lat,
                "Üniversite Boylam": uni_lng,
                "KYK Yurdu İsmi": yurt["isim"],
                "KYK Yurdu Adresi": yurt["adres"],
                "KYK Yurdu Enlem": yurt["lat"],
                "KYK Yurdu Boylam": yurt["lng"]
            })
        df = pd.DataFrame(data)

    # Excel dosyasına kaydet
    dosya_adi = uni.replace(" ", "_") + "_KYK_Yurtlari.xlsx"
    df.to_excel(dosya_adi, index=False)
    print(f"{dosya_adi} oluşturuldu.")

print("Tüm işlemler tamamlandı.")
