from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article, Category

# CBV untuk daftar artikel
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'

# CBV untuk detail artikel
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

# FBV untuk artikel berdasarkan kategori
def article_list(request):
    categories = Category.objects.all()  # Mengambil semua kategori
    articles = Article.objects.all()  # Mengambil semua artikel
    return render(request, 'article_list.html', {'articles': articles, 'categories': categories})

# View untuk menampilkan artikel berdasarkan kategori
def article_list_by_category(request, pk):
    category = Category.objects.get(pk=pk)  # Mendapatkan kategori berdasarkan ID
    articles = Article.objects.filter(category=category)  # Mengambil artikel berdasarkan kategori
    return render(request, 'article_list.html', {'articles': articles, 'category': category})