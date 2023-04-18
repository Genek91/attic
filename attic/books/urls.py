"""Натройка URL приложения books"""
from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('genre/<str:genre>/', views.genre, name='genre'),
]
