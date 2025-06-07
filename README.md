# ReactKickstart

# Asal Sayı Hesaplayıcı Modülü

Bu proje, asal sayılarla ilgili temel hesaplamaları yapmak için oluşturulmuş basit bir Python modülüdür.

## Özellikler

*   Verilen bir sayının asal olup olmadığını kontrol eder (`is_prime`).
*   İstenen adetteki ilk asal sayıların toplamını hesaplar (`sum_first_n_primes`).

## Gereksinimler

*   Python 3.x

## Nasıl Çalıştırılır?

Bu modülü kullanmanın iki yolu vardır:

### 1. Doğrudan Betik Olarak Çalıştırma (Test Amaçlı)

Modülün doğru çalıştığını test etmek için `primes.py` dosyasını terminal üzerinden doğrudan çalıştırabilirsiniz. Bu, dosyanın içindeki test kodunu tetikler.

```bash
# Projenin ana dizinindeyken bu komutu çalıştırın
python "hesap makinesi/primes.py"
```

**Örnek Çıktı:**

Bu komutu çalıştırdığınızda konsolda şu çıktıyı göreceksiniz:

```console
İlk 10 asal sayının toplamı: 129
İlk 50 asal sayının toplamı: 5117
```

### 2. Başka Bir Python Dosyasında Modül Olarak Kullanma

Bu modülün asıl amacı, fonksiyonlarını başka projelerde kullanmaktır. İşte bir örnek:

`main.py` adında yeni bir dosya oluşturun ve içine şunları yazın:

```python
# 'hesap makinesi' modülünden ilgili fonksiyonu içe aktar
from "hesap makinesi".primes import sum_first_n_primes, is_prime

# İlk 200 asal sayının toplamını bulalım
toplam = sum_first_n_primes(200)
print(f"İlk 200 asal sayının toplamı: {toplam}")

# Belirli bir sayının asal olup olmadığını kontrol edelim
sayi1 = 97
sayi2 = 100

print(f"{sayi1} asal bir sayı mı? -> {is_prime(sayi1)}")
print(f"{sayi2} asal bir sayı mı? -> {is_prime(sayi2)}")
```

Bu `main.py` dosyasını çalıştırdığınızda, `primes.py` içindeki fonksiyonları kullanarak yeni hesaplamalar yapabilirsiniz.
