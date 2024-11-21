from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),  # Home page menampilkan artikel
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),  # Detail artikel
    path('category/<int:pk>/articles/', views.article_list_by_category, name='article_list_by_category'),  # FBV untuk artikel berdasarkan kategori

    # Halaman utama untuk menampilkan daftar artikel
    path('', views.article_list, name='home'),  # Home page menampilkan artikel

    # Halaman artikel berdasarkan kategori
    path('category/<int:pk>/articles/', views.article_list_by_category, name='article_list_by_category'),  # FBV untuk artikel berdasarkan kategori
]
