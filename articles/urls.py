from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),  # URL untuk daftar artikel
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),  # URL untuk detail artikel
]
