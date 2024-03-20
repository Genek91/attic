"""Натройка URL приложения about"""
from django.urls import path

from about import views

app_name = 'about'

urlpatterns = [
    path('site/', views.AboutSiteView.as_view(), name='site'),
]
