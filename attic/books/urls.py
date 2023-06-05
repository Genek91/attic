"""Натройка URL приложения books"""
from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('genre/<int:id_genre>/', views.subgenre, name='id_genre'),
    path('subgenre/<int:id_subgenre>/', views.books, name='books'),
]
