import math

def is_prime(number: int) -> bool:
    """
    Bir sayının asal olup olmadığını verimli bir şekilde kontrol eder.

    Args:
        number: Kontrol edilecek tam sayı.

    Returns:
        Sayı asalsa True, değilse False döner.
    """
    # Kural 1: 1 ve daha küçük sayılar asal değildir.
    if number <= 1:
        return False
    
    # Kural 2: 2 tek çift asal sayıdır.
    if number == 2:
        return True

    # Kural 3: 2 dışındaki tüm çift sayılar asal değildir.
    # Bu kontrol, döngüdeki adımları azaltır.
    if number % 2 == 0:
        return False

    # Kural 4: Sayıyı, 3'ten başlayarak kendi kareköküne kadar olan
    # sadece tek sayılara bölmeyi deneriz. Bu, en verimli yöntemlerden biridir.
    # (Bir sayının böleni varsa, en az biri karekökünden küçük veya eşittir.)
    limit = int(math.sqrt(number))
    for i in range(3, limit + 1, 2):
        if number % i == 0:
            return False
            
    # Eğer yukarıdaki döngüde hiç bölen bulunamazsa, sayı asaldır.
    return True

def find_sum_of_first_n_primes(n: int):
    """
    İlk n adet asal sayıyı bulur ve toplamlarını ekrana yazdırır.
    
    Args:
        n: Bulunacak asal sayı adedi.
    """
    if n <= 0:
        print("Lütfen pozitif bir sayı girin.")
        return

    primes_found = []
    current_number = 2 # Kontrol edilecek ilk sayı
    
    # İstenen sayıda asal sayı bulunana kadar döngü devam eder.
    while len(primes_found) < n:
        if is_prime(current_number):
            primes_found.append(current_number)
        
        # Bir sonraki sayıyı kontrol et
        current_number += 1
        
    # Asal sayıların toplamını hesapla
    total_sum = sum(primes_found)
    
    print(f"İlk {n} asal sayı bulundu.")
    # print(f"Bulunan sayılar: {primes_found}") # Sayıları görmek isterseniz bu satırı aktif edin
    print(f"Bu sayıların toplamı: {total_sum}")


# --- Ana Program Başlangıcı ---
if __name__ == "__main__":
    # İlk 50 asal sayının toplamını bulmak için fonksiyonu çağır
    find_sum_of_first_n_primes(50)
