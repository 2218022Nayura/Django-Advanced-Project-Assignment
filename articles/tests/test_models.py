import unittest
from django.contrib.auth.models import User
from articles.models import Article, Category, Comment

class ArticleModelTest(unittest.TestCase):

    def test_article_creation(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        category = Category.objects.create(name="Technology")
        article = Article.objects.create(title="Test Article", content="Test Content", author=user, category=category)

        self.assertEqual(article.title, "Test Article")
        self.assertEqual(article.content, "Test Content")
        self.assertEqual(article.author.username, "testuser")
        self.assertEqual(article.category.name, "Technology")

    def test_comment_count(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        category = Category.objects.create(name="Technology")
        article = Article.objects.create(title="Test Article", content="Test Content", author=user, category=category)
        comment = Comment.objects.create(article=article, author=user, content="Test Comment")

        self.assertEqual(article.comment_count(), 1)  # Test the comment count method


class CategoryModelTest(unittest.TestCase):

    def test_category_creation(self):
        category = Category.objects.create(name="Technology")
        self.assertEqual(category.name, "Technology")

