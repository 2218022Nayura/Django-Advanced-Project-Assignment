from django.contrib import admin
from .models import Article, Category, UserProfile

# Kustomisasi admin untuk model Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')  # Menampilkan kolom artikel
    list_filter = ('category', 'created_at')  # Filter berdasarkan kategori dan tanggal
    search_fields = ('title', 'content')  # Pencarian berdasarkan judul dan konten
    ordering = ('-created_at',)  # Urutkan berdasarkan tanggal terbaru

admin.site.register(Article, ArticleAdmin)

# Kustomisasi admin untuk model Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Menampilkan nama kategori
    search_fields = ('name',)  # Pencarian berdasarkan nama kategori

admin.site.register(Category, CategoryAdmin)

# Kustomisasi admin untuk model UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')  # Menampilkan user dan bio
    search_fields = ('user__username',)  # Pencarian berdasarkan username user

admin.site.register(UserProfile, UserProfileAdmin)
