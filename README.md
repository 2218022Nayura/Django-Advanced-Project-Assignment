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

### **Day 1: Setup Project and Model Creation**
#### Date: 20 Nov 2024
- **Setup Django Project**:
  - Initialized Django project using `django-admin startproject` and created the main application **articles** using `startapp`.
  
- **Model Creation**:
  - Created models for **UserProfile**, **Article**, and **Category**.
  - **UserProfile** is linked to Django's default **User** model.
  - **Article** includes fields such as `title`, `content`, `category`, `author`, `created_at`, and `updated_at`.
  - **Category** helps organize articles into categories.
  
- **Database Migration**:
  - Successfully performed database migration to align the models with the SQLite database.
  
- **Testing**:
  - Confirmed the Django project runs correctly on **http://127.0.0.1:8000/**, with models and database functioning as expected.

---

### **Day 2: Admin Panel and Dummy Data**
#### Date: 21 Nov 2024
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

---


