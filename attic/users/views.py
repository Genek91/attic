"""Обработчики URL запросов."""
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm


class SignUp(CreateView):
    """Переадресация пользователя после авторизации."""
    form_class = CreationForm
    success_url = reverse_lazy('attic:index')
    template_name = 'users/signup.html'


def authorized_only(func):
    """Проверка авторизации пользователя."""
    def check_user(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect('/auth/login/')
    return check_user
