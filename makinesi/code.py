import time
import random
from elevenlabs import generate, play, set_api_key

# API anahtarlarınızı buraya girin
set_api_key("YOUR_ELEVENLABS_API_KEY")
# OPENAI_API_KEY = "YOUR_OPENAI_API_KEY" # Eğer bilgileri canlı üretecekseniz

# 1. Adım: Önceden ürettiğiniz bilgileri dosyadan okuyun
with open('facts_database.txt', 'r', encoding='utf-8') as f:
    all_facts = f.readlines()

while True:
    try:
        # 2. Adım: Rastgele bir bilgi seçin
        random_fact = random.choice(all_facts).strip()
        print(f"Yeni Bilgi: {random_fact}")

        # 3. Adım: Seçilen bilgiyi OBS'in okuduğu dosyaya yazın
        # Bu sayede ekrandaki yazı anında güncellenir
        with open('current_fact.txt', 'w', encoding='utf-8') as f:
            f.write(random_fact)

        # 4. Adım (Opsiyonel ama çok etkili): Bilgiyi seslendirin
        # ElevenLabs API'sini kullanarak metni sese çevirip çalın
        audio = generate(
            text=random_fact,
            voice="Rachel", # İstediğiniz bir sesi seçin
            model="eleven_multilingual_v2"
        )
        play(audio)

        # 5. Adım: Bir sonraki bilgi için bekleyin
        time.sleep(30) # 30 saniye bekle

    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        time.sleep(10) # Hata durumunda kısa bir süre bekle ve devam et
