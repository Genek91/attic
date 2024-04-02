"""Обработчики URL запросов."""
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)
from django.urls import reverse

from books.forms import BookForm
from books.models import Book, Genre, SubGenre
from users.views import authorized_only


def index(request):
    """Главная страница."""
    genres = get_list_or_404(Genre)
    return render(
        request,
        'books/index.html',
        {
            'genres': genres
        }
    )


def subgenre(request, id_genre):
    """Страница с поджанрами."""
    subgenres = get_list_or_404(SubGenre, genre=id_genre)
    return render(
        request,
        'books/subgenre.html',
        {
            'subgenres': subgenres
        }
    )


def books_list(request, id_subgenre):
    """Страница со списком книг."""
    books = get_list_or_404(Book, subgenre=id_subgenre)
    return render(
        request,
        'books/books_list.html',
        {
            'books': books
        }
    )


def author_books_list(request, author):
    author_books = get_list_or_404(Book, author=author)
    return render(
        request,
        'books/books_list.html',
        {
            'books': author_books
        }
    )


def new_books_list(request):
    books = get_list_or_404(Book)[:10]
    return render(
        request,
        'books/books_list.html',
        {
            'books': books
        }
    )


def book(request, id_book):
    book = get_object_or_404(Book, id=id_book)
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


@authorized_only
def update_book(request, id_book):
    book = get_object_or_404(Book, id=id_book)
    form = BookForm(
        request.POST or None,
        files=request.FILES or None,
        instance=book
    )

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(reverse('books:index'))
    return render(
        request,
        'books/create_book.html',
        {
            'form': form,
            'is_edit': True,
        }
    )


def authors(request):
    authors = sorted(list(set(Book.objects.values_list('author', flat=True))))
    return render(
        request,
        'books/authors.html',
        {
            'authors': authors
        }
    )
