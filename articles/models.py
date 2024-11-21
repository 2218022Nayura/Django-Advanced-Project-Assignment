from django.db import models
from django.contrib.auth.models import User

# Model untuk UserProfile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

# Model untuk Category
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Model untuk Article
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Model untuk Comment
class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=1)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.user.username} on {self.article.title}"

# Model untuk Tag
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Model untuk ArticleTag (Many to Many Relationship)
class ArticleTag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.article.title} - {self.tag.name}"

# Model untuk ProfilePicture
class ProfilePicture(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return f"Profile Picture for {self.user_profile.user.username}"

# Model untuk AuthorBio
class AuthorBio(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return f"Bio of {self.user_profile.user.username}"
