"""Натройка URL приложения books"""
from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('subgenre/<int:id_genre>/', views.subgenre, name='subgenre'),
    path('books-list/<int:id_subgenre>/', views.books_list, name='book_list'),
    path('book/<int:id_book>/', views.book, name='book'),
    path('authors/', views.authors, name='authors'),
]
