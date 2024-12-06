from django.contrib import admin
from .models import Article, Category, Comment, Tag, Like, ArticleTag, UserProfile

# Register model Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Menampilkan nama kategori di daftar kategori
    search_fields = ('name',)  # Memungkinkan pencarian berdasarkan nama kategori

# Register model Article
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'category')  # Menampilkan atribut artikel
    search_fields = ('title', 'content', 'author__username')  # Memungkinkan pencarian berdasarkan judul, konten, atau penulis
    list_filter = ('category', 'created_at', 'author')  # Memungkinkan penyaringan berdasarkan kategori, tanggal, dan penulis
    prepopulated_fields = {'slug': ('title',)}  # Otomatis membuat slug berdasarkan judul artikel
    ordering = ('-created_at',)  # Mengurutkan artikel berdasarkan waktu pembuatan (terbaru di atas)

# Register model Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'created_at', 'content')  # Menampilkan atribut komentar
    search_fields = ('content', 'author__username', 'article__title')  # Memungkinkan pencarian berdasarkan konten, penulis, atau artikel

# Register model Like
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'created_at')  # Menampilkan artikel, user, dan waktu like
    search_fields = ('article__title', 'user__username')  # Memungkinkan pencarian berdasarkan artikel atau user

# Register model Tag
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Menampilkan nama tag
    search_fields = ('name',)  # Memungkinkan pencarian berdasarkan nama tag

# Register model ArticleTag (Many-to-Many relationship between Article and Tag)
@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('article', 'tag')  # Menampilkan artikel dan tag yang terkait
    search_fields = ('article__title', 'tag__name')  # Memungkinkan pencarian berdasarkan artikel atau tag

# Register model UserProfile (untuk menampilkan profil pengguna di admin)
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture')  # Menampilkan profil pengguna
    search_fields = ('user__username',)  # Memungkinkan pencarian berdasarkan nama pengguna
