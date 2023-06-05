"""Обработчики URL запросов."""
from django.shortcuts import render
from books.models import Genre


def index(request):
    """Главная страница."""
    return render(
        request,
        'books/index.html'
    )


def subgenre(request, main_genre):
    """Страница с поджанрами."""
    genres = Genre.objects.filter(main_genre=main_genre)
    return render(
        request,
        'books/sub_genre.html',
        {
            'genres': genres
        }
    )
