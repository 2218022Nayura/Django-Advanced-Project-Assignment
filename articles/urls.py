from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Article Routes
    path('', views.ArticleListView.as_view(), name='home'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('category/<int:pk>/', views.article_list_by_category, name='article_list_by_category'),

    # Authentication Routes
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/welcome/'), name='logout'),  # Custom redirect to /welcome
    path('logout-success/', TemplateView.as_view(template_name='logout_success.html'), name='logout_success'),

    # Article Management Routes
    path('create-article/', views.create_article, name='create_article'),
    path('article/edit/<int:pk>/', views.article_edit, name='article_edit'),
]
