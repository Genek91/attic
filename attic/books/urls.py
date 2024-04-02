"""Натройка URL приложения books"""
from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('subgenre/<int:id_genre>/', views.subgenre, name='subgenre'),
    path('books-list/<int:id_subgenre>/', views.books_list, name='books_list'),
    path('new-books-list/', views.new_books_list, name='new_books_list'),
    path('book/<int:id_book>/', views.book, name='book'),
    path('create-book/', views.create_book, name='create_book'),
    path('update-book/<int:id_book>', views.update_book, name='update_book'),
    path('authors/', views.authors, name='authors'),
    path(
        'author-books-list/<str:author>',
        views.author_books_list,
        name='author_books_list'
    ),
]
