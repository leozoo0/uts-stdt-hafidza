
Nama : Hafidza Nur Afifah  
NIM : 235410012  
Kelas : Informatika 1  

---
# LOAD BALANCING FLASK + NGINX MENGGUNAKAN PODMAN (WINDOWS)

---

# 1. STRUKTUR FOLDER

Struktur folder project:

```

C:\Users\LEOZ\uts-hafidza\loadbalancing-podman
│
├── app.py
├── requirements.txt
├── Dockerfile
├── nginx.conf
└── README.md

```

<p align="center">
<img src="https://github.com/user-attachments/assets/ea5bcd25-19a6-4442-97fc-0528d58450ce" width="700"/>
</p>

<p align="center"><b>Gambar 1. Struktur Folder Project</b></p>

---

# 2. APP.PY

File Flask utama yang dijalankan di setiap container backend.
<p align="center">
<img width="975" height="649" alt="gambar" src="https://github.com/user-attachments/assets/020cee7f-41b9-40d2-897f-ebec85ccd4e3" />
<p align="center"><b>Gambar 2. Source Code app.py</b></p>

---

# 3. REQUIREMENTS.TXT

Dependency Python:

<p align="center">
<img src="https://github.com/user-attachments/assets/e37c3993-82af-42b5-ade7-2a64d663e8e4" width="700"/>
</p>

<p align="center"><b>Gambar 3. requirements.txt</b></p>

---

# 4. DOCKERFILE

Dockerfile untuk build image Flask:

<p align="center">
<img src="https://github.com/user-attachments/assets/87f3dc3b-40b6-49ae-92d4-376aef3b90e5" width="700"/>
</p>

<p align="center"><b>Gambar 4. Dockerfile Aplikasi</b></p>

---

# 5. NGINX.CONF (LOAD BALANCER)

Konfigurasi Nginx untuk load balancing ke 3 backend:

<p align="center">
<img src="https://github.com/user-attachments/assets/f8a84c86-e0ef-40c1-b6bf-6e6a8c332ef8" width="700"/>
</p>

<p align="center"><b>Gambar 5. Konfigurasi nginx.conf (Load Balancer)</b></p>

---

# 6. STEP PODMAN

## Masuk folder project

```

cd C:\Users\LEOZ\uts-hafidza\loadbalancing-podman

```

<p align="center">
<img src="https://github.com/user-attachments/assets/53c9694a-f28f-41c0-a5ff-7ac2224c754e" width="700"/>
</p>

<p align="center"><b>Gambar 6. Masuk ke Directory Project</b></p>

---

## Build image Flask

```

podman build -t flask-app .

```

<p align="center">
<img src="https://github.com/user-attachments/assets/bf464c1e-14b5-4bbf-8e53-fdb669eeb66d" width="700"/>
</p>

<p align="center"><b>Gambar 7. Build Image Flask</b></p>

---

## Buat network

```

podman network create lbnet

```

<p align="center">
<img src="https://github.com/user-attachments/assets/a3910270-c424-44b2-a2a5-fe229ace93d4" width="700"/>
</p>

<p align="center"><b>Gambar 8. Membuat Network Podman</b></p>

---

## Jalankan 3 backend container

```

podman run -d --name app1 --network lbnet -e APP_NAME=APP1 flask-app
podman run -d --name app2 --network lbnet -e APP_NAME=APP2 flask-app
podman run -d --name app3 --network lbnet -e APP_NAME=APP3 flask-app

```

<p align="center">
<img src="https://github.com/user-attachments/assets/f9f4175d-5f45-4f65-a308-cb681ee03bed" width="700"/>
</p>

<p align="center"><b>Gambar 9. Menjalankan 3 Container Backend</b></p>

---

## Jalankan Nginx Load Balancer

```

podman run -d --name nginx-lb --network lbnet -p 8080:80 ^
-v C:\Users\LEOZ\uts-hafidza\loadbalancing-podman\nginx.conf:/etc/nginx/nginx.conf:ro nginx:latest

```

<p align="center">
<img src="https://github.com/user-attachments/assets/8285b1f2-980b-4791-a56f-e6e46650c0c6" width="700"/>
</p>

<p align="center"><b>Gambar 10. Menjalankan Nginx Load Balancer</b></p>

---

# 7. TESTING HASIL

Akses browser:

```

[http://localhost:8080](http://localhost:8080)

```

---

## TESTING 1

Request pertama masuk ke APP1

<p align="center">
<img src="https://github.com/user-attachments/assets/3e7e7ad8-e0cd-4939-96f2-2917cdf23bf1" width="700"/>
</p>

<p align="center"><b>Gambar 11. Hasil Response dari APP1</b></p>

---

## TESTING 2

Request kedua masuk ke APP2

<p align="center">
<img src="https://github.com/user-attachments/assets/546f17a4-d9b4-4b37-8543-6b6a83ac316a" width="700"/>
</p>

<p align="center"><b>Gambar 12. Hasil Response dari APP2</b></p>

---

## TESTING 3

Request ketiga masuk ke APP3

<p align="center">
<img src="https://github.com/user-attachments/assets/3c2c4a79-7e40-4a76-a94a-1b0a02a9d2cd" width="700"/>
</p>

<p align="center"><b>Gambar 13. Hasil Response dari APP3</b></p>

---

# KESIMPULAN

Load balancing menggunakan Nginx dan Podman berhasil membagi request ke 3 container Flask (APP1, APP2, APP3). Hal ini membuktikan konsep High Availability (HA) berjalan dengan baik.
