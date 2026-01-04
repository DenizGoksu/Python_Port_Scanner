# 🕵️ PortScanner v2.0 (Dockerized)

Ağ güvenliği analizi ve port tarama süreçlerini otomatize eden, Python tabanlı bir siber güvenlik aracıdır. v2.0 ile birlikte proje tamamen Dockerize edilerek platform bağımsız hale getirilmiştir.

## 🚀 Öne Çıkan Özellikler
- **Konteyner Desteği:** Docker sayesinde kütüphane kurulumu derdi bitti.
- **Düşük Seviyeli Analiz:** `Scapy` kütüphanesi ile TCP paketleri üzerinden tarama yapar.
- **Renkli Çıktı:** `Colorama` entegrasyonu ile okunaklı ve hızlı terminal sonuçları.

## 🐳 Docker ile Hızlı Başlangıç

Bu aracı hiçbir kurulum yapmadan çalıştırmak için şu iki adımı izlemeniz yeterlidir:

### 1. İmajı Oluşturun (Build)
```bash docker build -t port-scanner . ```

2. Taramayı Başlatın (Run)
```bash
docker run --rm port-scanner -t 192.168.1.1
