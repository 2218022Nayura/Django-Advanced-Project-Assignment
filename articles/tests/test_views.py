from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from articles.models import Article, Category
from articles.forms import RegisterForm, ArticleForm, CommentForm


# CBV for Article List
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 10  # Adding pagination

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Adding categories to the context
        return context


# CBV for Article Detail
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()  # Adding comment form to context
        return context


# CBV for Article Create
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'create_article.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})


# CBV for Article Update
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_edit.html'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})


# CBV for Article Delete
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    context_object_name = 'article'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('article_list')  # Redirect to the article list page after delete


# CBV for Category List
class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 10  # Adding pagination

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Adding categories to the context
        return context


# CBV for Article List by Category
class ArticleListByCategoryView(ListView):
    model = Article
    template_name = 'article_list_by_category.html'
    context_object_name = 'articles'

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Article.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, pk=self.kwargs['pk'])
        return context


# FBV for Register
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user object
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# FBV for Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.GET.get('next', 'home'))  # Redirect to the intended page or home
    else:
        form = AuthenticationForm()

    next_url = request.GET.get('next', 'home')
    return render(request, 'login.html', {'form': form, 'next_url': next_url})


# Articles accessible only by logged-in users
@login_required
def article_list_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    articles = category.articles.all()
    return render(request, 'articles/article_list_by_category.html', {'category': category, 'articles': articles})


# Articles accessible only by admin users
@login_required
@staff_member_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)  # Redirect to article detail after edit
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article_edit.html', {'form': form})


# Add comment to article
@login_required
def add_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('article_detail', pk=article.pk)

    return redirect('article_detail', pk=article.pk)


# Create a new article, only for logged-in users
@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)  # Added request.FILES for image uploads
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user  # Associate article with the logged-in user
            article.save()
            return redirect('article_detail', pk=article.pk)  # Redirect to the newly created article
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})


# Custom Logout View to redirect after logout
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('welcome')  # Redirect to the welcome page after logout
