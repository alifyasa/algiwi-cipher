# AlGiWi Cipher

Made by Alif, Gilang, and Willy untuk mata kuliah IF4020 Kriptografi. Program menggunakan React + Vite + Typescript untuk frontend dan Flask untuk backend yang dibuat untuk mengimplementasikan enkripsi dan dekripsi pada cipher block. Pengguna akan memberikan input berupa file atau pesan yang diketik, metode, dan key yang digunakan, lalu program akan mengeluarkan hasil enkripsi atau dekripsi pada layar.

## Desain Cipher

Block Cipher didesain untuk bekerja pada ukuran blok 128-bit dan ukuran kunci 128-bit. Cipher memanfaatkan Feistel Network dengan 16 ronde. Disetiap ronde, diterapkan fungsi ronde yaitu substitusi dan permutasi. Substitusi dilakukan dengan memetakan hasil XOR byte plaintext dengan subkey pada byte lain berdasarkan S-Box. Permutasi dilakukan dengan mengacak urutan bit berdasarkan P-Box.

Detail desain cipher dapat diakses pada [README berikut](src/api/utils/cipher/README.md).

## Requirement Program dan Instalasi

Pengunduhan Node.js dapat dilakukan melalui situs berikut.

https://nodejs.org/en/download/

Pengunduhan Python dapat dilakukan melalui situs berikut.

https://www.python.org/downloads/

## Cara Menggunakan Program

### Frontend

```
> cd frontend
> cp .env.example .env
> npm install
> npm run dev
```
Notes: Isi key VITE_API_URL pada .env untuk terhubung ke backend (e.g. http://localhost:5000/api)

### Backend

```
> cd backend
> pip install -r requirements.txt
> python3 app.py
```

# Anggota Kelompok

| Nama | NIM |
| ---- | --- |
| Muhammad Alif Putra Yasa | 13520135 |
| Muhammad Gilang Ramadhan | 13520137 |
| Willy Wilsen             | 13520160 |
