from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Model untuk UserProfile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    # Menambahkan validasi ukuran gambar profil (maks 2MB)
    def clean(self):
        if self.profile_picture:
            filesize = self.profile_picture.size
            limit = 2 * 1024 * 1024  # 2MB
            if filesize > limit:
                raise ValidationError("File size should be less than 2MB.")

# Model untuk Category
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

# Model untuk Article
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)  # Field slug ditambahkan
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')

    def save(self, *args, **kwargs):
        if not self.slug:  # Jika slug belum ada, buat slug dari title
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # Menambahkan method untuk menghitung jumlah komentar
    def comment_count(self):
        return self.comments.count()

    # Menambahkan method untuk menghitung jumlah likes
    def like_count(self):
        return self.likes.count()

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-created_at']  # Urutkan artikel berdasarkan waktu pembuatan (terbaru di atas)

# Model untuk Comment
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.article.title}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['created_at']  # Urutkan komentar berdasarkan waktu dibuat (terbaru di atas)

# Model untuk Like
class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['article', 'user']  # Untuk memastikan satu user hanya bisa like satu artikel sekali
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self):
        return f"Like by {self.user.username} on {self.article.title}"

# Model untuk Tag
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

# Model untuk menghubungkan Tag dan Article (Many-to-Many relationship)
class ArticleTag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return f"{self.article.title} - {self.tag.name}"

    class Meta:
        verbose_name = "Article Tag"
        verbose_name_plural = "Article Tags"
