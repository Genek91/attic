"""Обработчики URL запросов."""
# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Главная страница."""
    return HttpResponse('Главная страница')
