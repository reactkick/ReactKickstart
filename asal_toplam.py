# -*- coding: utf-8 -*-

def asal_mi(sayi: int) -> bool:
    """
    Bir tam sayının asal olup olmadığını kontrol eder.

    - 1'den küçük veya 1'e eşit sayılar asal değildir.
    - Bir sayının asal olması için sadece 1'e ve kendisine tam bölünmesi gerekir.
    - Verimlilik için, bir sayının bölenlerini kendi kareköküne kadar
      kontrol etmek yeterlidir.

    Args:
        sayi: Kontrol edilecek tam sayı.

    Returns:
        Eğer sayı asalsa True, değilse False değerini döndürür.
    """
    # Asal sayı tanımı gereği 1'den büyük olmalıdır.
    if sayi <= 1:
        return False

    # 2'den başlayarak sayının kareköküne kadar olan sayılara bölünüp bölünmediğini kontrol et
    for i in range(2, int(sayi**0.5) + 1):
        # Eğer sayı bu aralıktaki herhangi bir sayıya tam bölünüyorsa, asal değildir.
        if sayi % i == 0:
            return False
            
    # Eğer döngü biter ve hiç bölen bulunamazsa, sayı asaldır.
    return True

# --- Ana Program ---
if __name__ == "__main__":
    
    bulunan_asallar = []  # Bulduğumuz asal sayıları saklamak için boş bir liste
    sayi = 2              # Asal sayıları aramaya 2'den başlıyoruz
    
    # 'bulunan_asallar' listesinde 50 eleman olana kadar döngüye devam et
    while len(bulunan_asallar) < 50:
        # 'sayi' değişkeninin asal olup olmadığını 'asal_mi' fonksiyonu ile kontrol et
        if asal_mi(sayi):
            # Eğer sayı asalsa, listeye ekle
            bulunan_asallar.append(sayi)
        
        # Bir sonraki sayıyı kontrol etmek için değeri bir artır
        sayi += 1
        
    # Listede biriken 50 asal sayının toplamını hesapla
    toplam = sum(bulunan_asallar)
    
    # İstenen sonucu konsola yazdır
    print(toplam)
