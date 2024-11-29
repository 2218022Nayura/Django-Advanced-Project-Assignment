from django import forms
from django.contrib.auth.models import User
from .models import Article, Comment

# Form untuk registrasi pengguna baru
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Konfirmasi Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')  # Memasukkan field username dan email

    # Validasi password
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password tidak cocok.")
        return password2

    # Menyimpan data form
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

# Form untuk membuat atau mengedit artikel
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'content']  # Field artikel yang dapat diisi

# Form untuk menambahkan komentar pada artikel
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Field komentar yang dapat diisi
