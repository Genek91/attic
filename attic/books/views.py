"""Обработчики URL запросов."""
from django.shortcuts import render
from books.models import Book, Genre


def index(request):
    """Главная страница."""
    return render(
        request,
        'books/index.html'
    )


def subgenre(request, main_genre):
    """Страница с жанрами."""
    print('>>>>>>>>>>>>', main_genre)
    genres = Genre.objects.filter(main_genre=main_genre)
    print('>>>>>>>>>>>>', genres)
    return render(
        request,
        'books/genre_list.html',
        {
            'genres': genres
        }
    )
