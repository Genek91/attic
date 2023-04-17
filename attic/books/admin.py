from django.contrib import admin

from books.models import Book


class PostAdmin(admin.ModelAdmin):
    """Основной класс для админки."""

    list_display = (
        'pk',
        'name',
        'text',
        'author',
        'pub_house',
        'pub_year',
        'book_add_date',
    )
    search_fields = ('text',)
    list_filter = ('book_add_date',)
    empty_value_display = '-пусто-'


admin.site.register(Book)
