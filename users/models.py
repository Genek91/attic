from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField


class User(AbstractUser):
    """Модель пользователей"""
    username = CharField(
        verbose_name='Логин',
        max_length=150,
        unique=True,
        blank=False,
    )
    email = EmailField(
        verbose_name='Почта',
        max_length=254,
        unique=True,
        blank=False,
    )
    first_name = CharField(
        verbose_name='Имя',
        max_length=150,
        blank=False,
    )
    last_name = CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=False,
    )
