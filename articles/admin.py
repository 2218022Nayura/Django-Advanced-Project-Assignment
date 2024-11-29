from django.contrib import admin
from .models import Article, Category, UserProfile, Comment, Like, Tag, ArticleTag, ArticleView

# Kustomisasi admin untuk model Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'created_at')  # Menampilkan artikel, pengarang, dan waktu pembuatan komentar
    search_fields = ('article__title', 'author__username', 'content')  # Pencarian berdasarkan artikel, pengarang, dan konten
    list_filter = ('created_at',)  # Filter berdasarkan tanggal pembuatan komentar
    raw_id_fields = ('article', 'author')  # Menggunakan raw_id untuk artikel dan author agar lebih cepat

admin.site.register(Comment, CommentAdmin)

# Kustomisasi admin untuk model UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')  # Menampilkan user dan bio
    search_fields = ('user__username',)  # Pencarian berdasarkan username user

admin.site.register(UserProfile, UserProfileAdmin)

# Kustomisasi admin untuk model Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Menampilkan nama kategori
    search_fields = ('name',)  # Pencarian berdasarkan nama kategori

admin.site.register(Category, CategoryAdmin)

# Kustomisasi admin untuk model Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')  # Menampilkan kolom artikel
    list_filter = ('category', 'created_at')  # Filter berdasarkan kategori dan tanggal
    search_fields = ('title', 'content')  # Pencarian berdasarkan judul dan konten
    ordering = ('-created_at',)  # Urutkan berdasarkan tanggal terbaru
    list_editable = ('category', 'author')  # Mengizinkan pengeditan kategori dan author langsung dari daftar
    inlines = []  # Menambahkan inline jika diperlukan untuk model terkait (misalnya Comment)

admin.site.register(Article, ArticleAdmin)

# Kustomisasi admin untuk model Like
class LikeAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'created_at')  # Menampilkan artikel, pengguna, dan waktu pemberian like
    search_fields = ('article__title', 'user__username')  # Pencarian berdasarkan artikel dan pengguna

admin.site.register(Like, LikeAdmin)

# Kustomisasi admin untuk model Tag
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Menampilkan nama tag
    search_fields = ('name',)  # Pencarian berdasarkan nama tag

admin.site.register(Tag, TagAdmin)

# Kustomisasi admin untuk model ArticleTag
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('article', 'tag')  # Menampilkan artikel dan tag
    search_fields = ('article__title', 'tag__name')  # Pencarian berdasarkan artikel dan tag
    raw_id_fields = ('article', 'tag')  # Menampilkan ID artikel dan tag untuk mempercepat pemilihan

admin.site.register(ArticleTag, ArticleTagAdmin)

# Kustomisasi admin untuk model ArticleView
class ArticleViewAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'viewed_at')  # Menampilkan artikel, pengguna, dan waktu tampilan
    search_fields = ('article__title', 'user__username')  # Pencarian berdasarkan artikel dan pengguna
    raw_id_fields = ('article', 'user')  # Menampilkan ID artikel dan pengguna untuk mempercepat pemilihan

admin.site.register(ArticleView, ArticleViewAdmin)
