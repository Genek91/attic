"""Обработчики URL запросов."""
from django.shortcuts import render
from books.models import Book


def index(request):
    """Главная страница."""
    return render(
        request,
        'books/index.html',
        {
            'books': Book.objects.all()
        }
    )


def genre(request, genre):
    """Страница с жанрами."""
    return render(
        request,
        'books/genre.html',
        {
            'genres': Book.objects.filter(genre=genre)
        }
    )
