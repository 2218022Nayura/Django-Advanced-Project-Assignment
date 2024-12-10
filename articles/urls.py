from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from . import views
from .views import CustomLogoutView

urlpatterns = [
    # Article Routes
    path('', views.ArticleListView.as_view(), name='home'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/comment/', views.add_comment, name='add_comment'),    # Route untuk menambahkan komentar
    path('category/<int:pk>/', views.article_list_by_category, name='article_list_by_category'),

    # Authentication Routes
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Menggunakan CustomLogoutView
    path('logout-success/', TemplateView.as_view(template_name='logout_success.html'), name='logout_success'),
    path('welcome/', TemplateView.as_view(template_name='welcome.html'), name='welcome'),

    # Article Management Routes
    path('create-article/', views.create_article, name='create_article'),
    path('article/edit/<int:pk>/', views.article_edit, name='article_edit'),



]
