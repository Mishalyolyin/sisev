# 📊 Django Docker Stats App

Aplikasi web statistik pengguna dan course berbasis **Django + SQLite**, dikembangkan menggunakan **Docker**. Cocok untuk latihan Web Framework & ORM dengan data dinamis.

---

## 🧩 Fitur Statistik

Akses di: [http://localhost:8000/stats/](http://localhost:8000/stats/)

Statistik yang ditampilkan:
- ✅ Jumlah user yang membuat course
- ✅ Jumlah user yang tidak memiliki course
- ✅ Rata-rata jumlah course yang diikuti oleh satu user
- ✅ User yang mengikuti course terbanyak
- ✅ List user yang tidak mengikuti course sama sekali

---

## 👤 Fitur Manajemen User

- **List Semua User**:  
  🔗 [http://localhost:8000/users/](http://localhost:8000/users/)

- **Tambah User Baru**:  
  🔗 [http://localhost:8000/add-user/](http://localhost:8000/add-user/)

- **Edit User**:  
  Tombol ✏️ tersedia di halaman list user

- **Hapus User**:  
  Tombol ❌ tersedia di halaman list user

---

## 🚀 Cara Menjalankan (Docker)

```bash
docker-compose up
