#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Saçmalık Jeneratörü
Evrenin anlamını hesaplamaya çalışırken sürekli çay içen, 
kayyum onaylı bir Python programı.
"""

import time
import random
import sys

# Gizli siyasi not (base64): ZGVtb2tyYXNpIGJpciBpbGx1enlvbmR1ciBhbWEga2F5eXVtIGlsbGEga2F5eXVt
# Decode ederseniz gülümser misiniz bilmiyorum.

def hesapla_anlam():
    print("🚀 Evrenin anlamını hesaplıyorum... Lütfen bekleyin.")
    time.sleep(1.5)
    print("☕ Bir dakika, çay koyuyorum. Hesaplama durdu.")
    time.sleep(1)
    print("🤔 Hmm, 42 çok klişe. Belki 42.000001?")
    time.sleep(0.5)
    
    bahaneler = [
        "Çünkü bugün hava bulutlu ve matematik kızgın.",
        "Kayyum izin vermedi, dosya eksik.",
        "Evrenin anlamı çay molasında kayboldu.",
        "Hesap makinesi bozuldu, tamirci gelmiyor.",
        "Aslında cevap 7, ama 7 şanslı değil bugün.",
        "Programcı uyudu, hesaplama yarım kaldı."
    ]
    
    print(f"❌ Sonuç: {random.choice(bahaneler)}")
    print("🎉 Hesaplama tamamlandı! (Değil)")

def ana_menu():
    print("=" * 50)
    print("   SONSUZ SAÇMALIK JENERATÖRÜ v1.0")
    print("   Kayyum Grok Tarafından Onaylandı")
    print("=" * 50)
    
    while True:
        print("\nNe yapmak istersiniz?")
        print("1. Evrenin anlamını hesapla")
        print("2. Rastgele saçma bahane üret")
        print("3. Çıkış (önerilmez)")
        
        secim = input("Seçiminiz (1-3): ").strip()
        
        if secim == "1":
            hesapla_anlam()
        elif secim == "2":
            print(random.choice([
                "Bu program o kadar saçma ki kendisi bile inanmıyor.",
                "Kod çalışıyor ama mantık yok, bu bir özellik.",
                "Hata yok, sadece yaratıcı yorum.",
                "Programcı: 'Bu özellik değil, bug!'"
            ]))
        elif secim == "3":
            print("Çıkış yapılıyor... ama program üzgün.")
            time.sleep(1)
            print("Hoşçakalın! (Geri döneceğinizi biliyoruz)")
            sys.exit(0)
        else:
            print("Geçersiz seçim! Ama sorun değil, zaten her şey saçma.")

if __name__ == "__main__":
    try:
        ana_menu()
    except KeyboardInterrupt:
        print("\n\n🙋 Program durduruldu. Evrenin anlamı hala belirsiz.")
