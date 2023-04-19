"""Обработчики URL запросов."""
from django.shortcuts import render
from books.models import Book


def index(request):
    """Главная страница."""
    return render(
        request,
        'books/index.html'
    )


def subgenre(request, genre):
    """Страница с жанрами."""
    print('>>>>>>>>>>>>', genre)
    subgenre = Book.objects.filter(genre=genre)
    print('>>>>>>>>>>>>', subgenre)
    return render(
        request,
        'books/genre_list.html',
        {
            'subgenres': subgenre
        }
    )
