"""Натройка моделей приложения books."""
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Genre(models.Model):
    """Модель Genre для Attic."""

    class Meta:
        """Дефолтная сортировка модели Genre."""
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    name = models.TextField(
        verbose_name='Жанр книги',
        help_text='Жанр книги',
    )

    def __str__(self):
        """Вывод поля genre."""
        return self.name


class SubGenre(models.Model):
    """Модель SubGenre для Attic."""

    class Meta:
        """Дефолтная сортировка модели SubGenre."""
        ordering = ['name']
        verbose_name = 'Поджанр'
        verbose_name_plural = 'Поджанры'

    name = models.TextField(
        verbose_name='Поджанр книги',
        help_text='Поджанр книги',
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name='subgenres',
        verbose_name='Жанр',
    )

    def __str__(self):
        """Вывод поля subgenre."""
        return self.name


class Book(models.Model):
    """Модель Book для Attic."""

    class Meta:
        """Дефолтная сортировка модели Book."""
        ordering = ['-book_add_date']
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'

    subgenre = models.ForeignKey(
        SubGenre,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='Поджанр',
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
    pub_year = models.PositiveIntegerField(
        verbose_name='Год издания',
        help_text='Год издания',
        validators=[
            MaxValueValidator(3000),
            MinValueValidator(1000)
        ],
    )
    image = models.ImageField(
        upload_to='books/',
        blank=True,
        verbose_name='Картинка',
    )
    book_add_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления книги',
    )

    def __str__(self):
        """Вывод поля name."""
        return self.name
