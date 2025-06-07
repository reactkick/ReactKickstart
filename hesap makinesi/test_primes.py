# -*- coding: utf-8 -*-

# Testleri çalıştırmak için pytest kütüphanesini import etmeye gerek yoktur,
# ancak daha gelişmiş özellikler (örn: pytest.raises) için gerekebilir.
import pytest 

# Test edilecek fonksiyonları, aynı paketin içindeki primes modülünden import et.
# Baştaki '.' işareti, bu import'un bir "göreceli import" olduğunu belirtir.
from .primes import is_prime, sum_first_n_primes

# --- 'is_prime' Fonksiyonu İçin Testler ---

def test_is_prime_ile_asal_sayilar():
    """is_prime fonksiyonunun bilinen asal sayılar için True döndürdüğünü doğrula."""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(7) is True
    assert is_prime(29) is True
    assert is_prime(97) is True

def test_is_prime_ile_asal_olmayan_sayilar():
    """is_prime fonksiyonunun asal olmayan sayılar için False döndürdüğünü doğrula."""
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(100) is False
    assert is_prime(25) is False

def test_is_prime_ile_sinir_durumlari():
    """is_prime fonksiyonunun sınır durumları (0, 1, negatif) için False döndürdüğünü doğrula."""
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-10) is False


# --- 'sum_first_n_primes' Fonksiyonu İçin Testler ---

def test_sum_first_n_primes_temel_durum():
    """İstemde özellikle belirtilen temel durumu (n=10) test et."""
    # İlk 10 asal sayı: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
    # Bu sayıların toplamı: 129
    assert sum_first_n_primes(10) == 129

def test_sum_first_n_primes_tek_asal():
    """Sadece bir adet asal sayı istendiğinde (n=1) doğru sonucu verdiğini test et."""
    # İlk asal sayı 2'dir.
    assert sum_first_n_primes(1) == 2

def test_sum_first_n_primes_daha_buyuk_sayi():
    """Daha büyük bir n değeri ile (n=50) doğru sonucu verdiğini test et."""
    # İlk 50 asal sayının toplamı 5117'dir.
    assert sum_first_n_primes(50) == 5117

def test_sum_first_n_primes_sinir_durumlari():
    """Fonksiyonun sınır durumları (n=0, negatif n) için 0 döndürdüğünü doğrula."""
    assert sum_first_n_primes(0) == 0
    assert sum_first_n_primes(-5) == 0
