# -*- coding: utf-8 -*-

def is_prime(n: int) -> bool:
    """
    Bir tam sayının asal olup olmadığını kontrol eder.

    Args:
        n (int): Kontrol edilecek sayı.

    Returns:
        bool: Sayı asalsa True (Doğru), değilse False (YANLIŞ) döner.
    """
    # Asal sayılar tanım gereği 1'den büyüktür.
    if n <= 1:
        return False

    # Verimlilik için sayının kareköküne kadar kontrol etmek yeterlidir.
    # 2'den başlayarak bu sınıra kadar olan sayılara bölünürse, asal değildir.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            
    # Eğer döngü boyunca hiç bölen bulunamazsa, sayı asaldır.
    return True


def sum_first_n_primes(n: int) -> int:
    """
    Parametre olarak verilen 'n' adedi kadar ilk asal sayıyı bulur ve 
    bu sayıların toplamını döndürür.

    Args:
        n (int): Bulunması istenen asal sayı adedi.

    Returns:
        int: Bulunan ilk 'n' adet asal sayının toplamı.
             Eğer n <= 0 ise 0 döner.
    """
    if n <= 0:
        return 0

    primes_found = []
    current_number = 2

    # İstenen 'n' adedinde asal sayı bulana kadar döngü devam eder.
    while len(primes_found) < n:
        # Yukarıda tanımlanan 'is_prime' fonksiyonunu kullanarak kontrol et.
        if is_prime(current_number):
            primes_found.append(current_number)
        
        current_number += 1
        
    # Bulunan asal sayıların listesini topla ve sonucu döndür.
    return sum(primes_found)


# --- Bu bölüm, dosya doğrudan çalıştırıldığında test amacıyla kullanılır ---
# Başka bir dosyadan import edildiğinde bu kod çalışmaz.
if __name__ == '__main__':
    # İlk 10 asal sayının toplamını test edelim
    # (2+3+5+7+11+13+17+19+23+29 = 129)
    toplam_10 = sum_first_n_primes(10)
    print(f"İlk 10 asal sayının toplamı: {toplam_10}")

    # Ana görev: İlk 50 asal sayının toplamını bulalım
    toplam_50 = sum_first_n_primes(50)
    print(f"İlk 50 asal sayının toplamı: {toplam_50}")
