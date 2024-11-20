from django.http import HttpResponse  # Menambahkan import untuk HttpResponse
from django.shortcuts import render
from .models import Article

# Tampilan untuk menampilkan daftar artikel
def home(request):
    return render(request, 'home.html')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, pk):
    # Mengambil artikel berdasarkan primary key (pk)
    article = Article.objects.get(pk=pk)
    return render(request, 'article_detail.html', {'article': article})