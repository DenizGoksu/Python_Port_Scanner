# Python Port Scanner

Bu proje, bir Junior Yazılım Geliştirici ve Siber Güvenlik meraklısı olarak, ağ protokollerinin (TCP/IP) temellerini ve Python `socket` kütüphanesini anlamak amacıyla geliştirdiğim ilk araçtır.

# Öne Çıkan Özellikler

- Bağlantı Denetimi: `socket.connect_ex()` metodunu kullanarak TCP bağlantı denemeleri yapar.
- Hız Optimizasyonu: `s.settimeout(0.1)` ile tarama süresini minimize ettim (Junior seviyesinde hız/doğruluk dengesini öğrenmek için kritik bir adım).
- Servis Analizi: Açık portların hangi standart servislere (80: HTTP, 22: SSH vb.) ait olduğunu otomatik tespit eder.
- Güvenli Çıkış: `KeyboardInterrupt` (CTRL+C) yakalaması sayesinde kullanıcı taramayı istediği an çökme olmadan durdurabilir.

# Nasıl Kullanılır?

Kodun çalışması için herhangi bir ek kütüphane gerekmez, standart Python 3 kütüphaneleriyle çalışır.

1. Terminali açın.
2. Klasöre gidin.
3. Şu komutu çalıştırın:
   ```bash
   python3 port_scanner.py