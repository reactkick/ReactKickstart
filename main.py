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
