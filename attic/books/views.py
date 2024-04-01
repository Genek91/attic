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


def books_list(request, id_subgenre):
    """Страница со списком книг."""
    books = Book.objects.filter(sub_genre=id_subgenre)
    return render(
        request,
        'books/books_list.html',
        {
            'books': books
        }
    )


def new_books_list(request):
    books = Book.objects.all()[:10]
    return render(
        request,
        'books/books_list.html',
        {
            'books': books
        }
    )


def book(request, id_book):
    book = Book.objects.get(id=id_book)
    return render(
        request,
        'books/book.html',
        {
            'book': book
        }
    )


def authors(request):
    authors = Book.objects.values('author')
    return render(
        request,
        'books/authors.html',
        {
            'authors': authors
        }
    )
