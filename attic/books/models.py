"""Натройка моделей приложения books."""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Book(models.Model):
    """Модель Book для Attic."""

    class Meta:
        """Дефолтная сортировка модели Book."""
        ordering = ['-book_add_date']
        verbose_name = 'Книги'

    genre = models.TextField(
        verbose_name='Жанр книги',
        help_text='Жанр книги',
    )
    name = models.TextField(
        verbose_name='Название книги',
        help_text='Название книги',
    )
    text = models.TextField(
        verbose_name='Описание книги',
        help_text='Описание книги',
    )
    author = models.TextField(
        verbose_name='Автор книги',
        help_text='Автор книги',
    )
    pub_house = models.TextField(
        verbose_name='Издательство',
        help_text='Издательство',
    )
    pub_year = models.TextField(
        verbose_name='Год издания',
        help_text='Год издания',
    )
    '''
    image = models.ImageField(
        upload_to='books/',
        blank=True,
        verbose_name='Картинка',
    )
    '''
    book_add_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления книги',
    )

    def __str__(self):
        """Вывод поля name."""
        return self.name
