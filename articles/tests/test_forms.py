import sys
import os

# Menambahkan path aplikasi 'articles' ke dalam sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from django.test import TestCase
from django.contrib.auth.models import User
from articles.forms import RegisterForm, ArticleForm, CommentForm
from articles.models import Category, Article


class RegisterFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'username': 'testuser', 'email': 'testuser@example.com', 'password1': 'password123', 'password2': 'password123'}
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_password_mismatch(self):
        form_data = {'username': 'testuser', 'email': 'testuser@example.com', 'password1': 'password123', 'password2': 'password456'}
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

class ArticleFormTest(TestCase):
    def test_valid_form(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        category = Category.objects.create(name="Tech")
        form_data = {'title': 'New Article', 'category': category.id, 'content': 'Article content'}
        form = ArticleForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_title(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        category = Category.objects.create(name="Tech")
        form_data = {'title': '', 'category': category.id, 'content': 'Article content'}
        form = ArticleForm(data=form_data)
        self.assertFalse(form.is_valid())

class CommentFormTest(TestCase):
    def test_valid_form(self):
        article = Article.objects.create(title="Test Article", content="Test content", author_id=1, category_id=1)
        form_data = {'content': 'This is a comment'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_content(self):
        form_data = {'content': ''}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())
