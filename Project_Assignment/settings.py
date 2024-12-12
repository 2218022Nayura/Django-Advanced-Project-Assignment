from pathlib import Path
import os  # Ditambahkan untuk penggunaan environment variables

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Sebaiknya simpan SECRET_KEY di environment variables
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-l1m9(bl_nil%@5sxj+poj=wtxa0$g$%uc$cf#@h!%sm@m4c8!8')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS: pastikan ini diubah untuk produk ke domain yang valid
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.herokuapp.com']  # Tambahkan domain Heroku

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles',  # Aplikasi Saya
    'django_extensions',

    # REST API ENDPOINT
    'rest_framework',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Menambahkan WhiteNoise untuk file statis
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Project_Assignment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Pastikan direktori template sudah benar
        'APP_DIRS': True,  # Pencarian template dalam aplikasi
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Project_Assignment.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Gunakan SQLite untuk pengembangan
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = 'static/'

# Menambahkan direktori untuk static files
STATICFILES_DIRS = [BASE_DIR / "static"]

# Menetapkan STATIC_ROOT untuk Heroku
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (images, etc.)
MEDIA_URL = '/media/'  # URL yang dapat diakses oleh pengguna untuk mengakses file media
MEDIA_ROOT = BASE_DIR / 'media'  # Direktori tempat file media disimpan

# Pengaturan Login dan Logout Redirect
LOGIN_REDIRECT_URL = '/'  # Redirect ke homepage setelah login
LOGOUT_REDIRECT_URL = 'welcome'  # Redirect ke halaman welcome setelah logout

# Pengaturan Login URL untuk pengguna yang belum login
LOGIN_URL = 'login'  # Pastikan ini mengarah ke URL login Anda

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS (Cross-Origin Resource Sharing) settings
# Untuk aplikasi yang membutuhkan request dari domain lain
# CORS_ALLOW_ALL_ORIGINS = True  # Bisa menambah jika menggunakan CORS
