# Django Article Hub (DAH) - Project Assignment Django Advanced
### Application Title: Django Article Hub (DAH)

## Konsep Aplikasi:
Django Article Hub (DAH) adalah aplikasi berbasis web untuk mengelola artikel. Platform ini dirancang untuk memungkinkan pengguna membaca artikel yang tersedia secara publik, membuat artikel baru, mengedit artikel yang sudah ada, dan menghapus artikel milik mereka. Artikel dikelompokkan berdasarkan kategori untuk mempermudah navigasi. Admin panel kustom juga disediakan untuk pengelolaan data seperti kategori, pengguna, dan artikel.

## Spesifikasi Aplikasi:
- **Backend Framework**: Django
- **Frontend**: Django Template Engine, Bootstrap
- **Database**: SQLite
- **Programming Language**: Python
- **Libraries**: Pillow, Django REST Framework (direncanakan untuk fitur API)

## PROGRESS 
### 20/11/2024
- **Judul dan Konsep Aplikasi** telah ditentukan.
- **Setup Proyek Django**:
  - Menginisialisasi proyek Django dengan perintah `django-admin startproject` dan membuat aplikasi utama **articles** menggunakan `startapp`.
  
- **Membuat Model Utama**:
  - **UserProfile**: Menambahkan model untuk profil pengguna, yang terkait dengan model **User** milik Django.
  - **Article**: Membuat model artikel dengan fields seperti `title`, `content`, `category`, `author`, `created_at`, dan `updated_at`.
  - **Category**: Membuat model kategori untuk mengelompokkan artikel.

- **Migrasi Database**: 
  - Berhasil melakukan migrasi database untuk mencocokkan model yang telah dibuat dengan database SQLite.
  
- **Pengecekan**:
  - Proyek telah berhasil dijalankan pada **http://127.0.0.1:8000/** dan memastikan bahwa model dan database berfungsi dengan baik.

