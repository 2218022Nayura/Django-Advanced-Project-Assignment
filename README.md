20/11/24 
Project Assignment Django Advanced
Application Title: Django Article Hub (DAH)
----------------------------------------------
# Konsep Aplikasi :
Django Article Hub (DAH) adalah aplikasi berbasis web untuk mengelola artikel.
Platform ini dirancang untuk memungkinkan pengguna membaca artikel yang tersedia secara publik, membuat artikel baru, mengedit artikel yang sudah ada, dan menghapus artikel milik mereka. 
Artikel dikelompokkan berdasarkan kategori untuk mempermudah navigasi. Admin panel kustom juga disediakan untuk pengelolaan data seperti kategori, pengguna, dan artikel.

# Spesifikasi Aplikasi
Backend Framework: Django
Frontend: Django Template Engine, Bootstrap
Database: SQLite
Programming Language: Python
Libraries: Pillow, Django REST Framework (direncanakan untuk fitur API)

# PROGRESS Day 1: Setup Proyek dan Pembuatan Model (20/11/2024) 
- Judul dan Konsep Aplikasi
- Setup proyek Django.
- Buat aplikasi utama (articles).
- Membuat model utama (User Profile, Article, Category).
- Migrasi database.

## Day 2: Admin Panel and Dummy Data (21 Nov 2024)
- **Admin Panel Customization**:
  - Created models for **Article**, **Category**, and **UserProfile**.
  - Customized admin panel to display, filter, and search articles.
  - Articles are ordered by creation date for easy management.

- **Dummy Data Added**:
  - Added dummy categories: `Tech`, `Lifestyle`, and `Testing`.
  - Added dummy articles: `Tech Article 1`, `Lifestyle Article 1`, and `Test 1`.

- **Testing**:
  - Successfully tested adding, editing, and deleting articles and categories via the Django admin panel.

- **Git Commit**:
  - Commit message: **"Customize admin panel and add dummy data"**
  - Pushed to GitHub to track progress.
