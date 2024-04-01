"""Обработчики URL запросов."""
from django.shortcuts import render, redirect
from django.urls import reverse

from users.views import authorized_only
from books.forms import BookForm
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


@authorized_only
def create_book(request):
    form = BookForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect(reverse('books:index'))
    return render(request, 'books/create_book.html', {'form': form})


def authors(request):
    authors = Book.objects.values('author')
    return render(
        request,
        'books/authors.html',
        {
            'authors': authors
        }
    )
