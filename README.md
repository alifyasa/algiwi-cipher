# AlGiWi Cipher

Made by Alif, Gilang, and Willy untuk mata kuliah IF4020 Kriptografi. Program menggunakan React + Vite + Typescript untuk frontend dan Flask untuk backend yang dibuat untuk mengimplementasikan enkripsi dan dekripsi pada cipher block. Pengguna akan memberikan input berupa file atau pesan yang diketik, metode, dan key yang digunakan, lalu program akan mengeluarkan hasil enkripsi atau dekripsi pada layar.

## Requirement program dan instalasi

Pengunduhan Python dapat dilakukan melalui situs berikut.

https://www.python.org/downloads/

Pengunduhan Node.js dapat dilakukan melalui situs berikut.

https://nodejs.org/en/download/

## Cara menggunakan program

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
