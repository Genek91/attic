from django.contrib import admin

from books.models import Book, Genre, SubGenre


class BookAdmin(admin.ModelAdmin):
    """Основной класс для админки модели Book."""

    list_display = (
        'pk',
        'sub_genre',
        'name',
        'text',
        'author',
        'pub_house',
        'pub_year',
        'book_add_date',
    )
    search_fields = ('name',)
    list_filter = ('book_add_date',)
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    """Основной класс для админки модели Genre."""

    list_display = (
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)


class SubGenreAdmin(admin.ModelAdmin):
    """Основной класс для админки модели Genre."""

    list_display = (
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(SubGenre, SubGenreAdmin)
