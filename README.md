# UTS Load Balancing Podman + Nginx

## Deskripsi
Project ini menggunakan Podman untuk menjalankan 2 container backend dan Nginx sebagai load balancer.

## Arsitektur
- app1 → localhost:8081
- app2 → localhost:8082
- nginx-lb → localhost:8080

## Teknologi
- Podman
- Nginx

## Cara Kerja
Nginx akan membagi request ke app1 dan app2 secara round robin.

## Hasil
Load balancing berhasil ditunjukkan dengan perubahan response saat refresh halaman 8080.
