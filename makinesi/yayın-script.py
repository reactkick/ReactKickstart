import json
import time
import random
import os
# ElevenLabs API'si için kütüphaneyi yüklemeniz gerekir: pip install elevenlabs
from elevenlabs import generate, play, set_api_key

# API Anahtarınızı buraya girin (Örnek)
# set_api_key("YOUR_ELEVENLABS_API_KEY")

# 1. Kur'an veritabanını yükle
with open('kuran.json', 'r', encoding='utf-8') as f:
    kuran_data = json.load(f)

# 2. Tüm ayetleri tek bir listeye topla
all_verses = []
for sure in kuran_data:
    for ayet in sure['verses']:
        all_verses.append({
            "sure_adi": sure['name'],
            "ayet_no": ayet['id'],
            "arapca": ayet['text'],
            "meal": ayet['translation']
        })

print(f"Toplam {len(all_verses)} ayet yüklendi.")

# 3. Sonsuz yayın döngüsü
while True:
    try:
        # Rastgele bir ayet seç
        secilen_ayet = random.choice(all_verses)

        sure_adi = secilen_ayet['sure_adi']
        ayet_no = secilen_ayet['ayet_no']
        arapca_metin = secilen_ayet['arapca']
        meal_metni = secilen_ayet['meal']

        # Ekranda gösterilecek bilgileri formatla
        sure_ayet_bilgisi = f"{sure_adi} Suresi, {ayet_no}. Ayet"
        
        print("--- YENİ AYET ---")
        print(sure_ayet_bilgisi)
        print(meal_metni)

        # 4. OBS'in okuduğu metin dosyalarını güncelle
        with open('sure_ayet.txt', 'w', encoding='utf-8') as f:
            f.write(sure_ayet_bilgisi)
        
        with open('arapca.txt', 'w', encoding='utf-8') as f:
            f.write(arapca_metin)

        with open('meal.txt', 'w', encoding='f') as f:
            f.write(meal_metni)

        # 5. (İsteğe bağlı) Meali AI ile seslendir
        # audio = generate(
        #     text=f"{sure_ayet_bilgisi}. {meal_metni}",
        #     voice="Bella",  # İstediğiniz bir sesi seçin
        #     model="eleven_multilingual_v2"
        # )
        # play(audio) # Bu komut sesi doğrudan çalar. OBS'e göndermek için farklı yöntemler gerekir.
        
        # 6. Bir sonraki ayet için bekleme süresi
        # Örneğin, 1 dakika bekle
        time.sleep(60)

    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        time.sleep(10) # Hata durumunda 10 saniye bekle ve devam et
