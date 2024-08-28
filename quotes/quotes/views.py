from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm, AuthorForm, QuoteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Author, Quote


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('home')  # Перенаправление на главную страницу
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def home(request):
    return render(request, 'home.html')


@login_required
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу после создания автора
    else:
        form = AuthorForm()
    return render(request, 'create_author.html', {'form': form})


@login_required
def create_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу после создания цитаты
    else:
        form = QuoteForm()
    return render(request, 'create_quote.html', {'form': form})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author_detail.html', {'author': author})


def author_list(request):
    authors = Author.objects.all()  # Получаем всех авторов из базы данных
    return render(request, 'author_list.html', {'authors': authors})


def author_quotes(request, author_id):
    author = get_object_or_404(Author, pk=author_id)  # Получаем автора по его ID
    quotes = Quote.objects.filter(author=author)  # Фильтруем цитаты по автору
    return render(request, 'author_quotes.html', {'author': author, 'quotes': quotes})

