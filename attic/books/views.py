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
