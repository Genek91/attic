"""Обработчики URL запросов."""
from django.shortcuts import render
from books.models import Book, Genre, SubGenre


def index(request):
    """Главная страница."""
    genres = Genre.objects.all()
    return render(
        request,
        'books/index.html',
        {
            'genres': genres
        }
    )


def subgenre(request, id_genre):
    """Страница с поджанрами."""
    sub_genres = SubGenre.objects.filter(genre=id_genre)
    return render(
        request,
        'books/sub_genre.html',
        {
            'sub_genres': sub_genres
        }
    )


def books(request, id_subgenre):
    """Страница с книгами."""
    books = Book.objects.filter(sub_genre=id_subgenre)
    return render(
        request,
        'books/books.html',
        {
            'books': books
        }
    )
