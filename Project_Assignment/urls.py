from django.contrib import admin
from django.urls import path, include
from articles import views  # Import views dari aplikasi articles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),  # URL untuk aplikasi articles
    path('', views.home, name='home'),  # Menampilkan home.html URL untuk halaman utama
]
