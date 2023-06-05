from django.contrib import admin

from books.models import Book, Genre


class BookAdmin(admin.ModelAdmin):
    """Основной класс для админки модели Book."""

    list_display = (
        'pk',
        'genre',
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

    def show_genre(self, obj):
        result = Genre.objects.filter(sub_genre=obj)
        return result['genre']


class GenreAdmin(admin.ModelAdmin):
    """Основной класс для админки модели Genre."""

    list_display = (
        'main_genre',
        'sub_genre',
    )
    search_fields = ('sub_genre',)
    list_filter = ('main_genre',)


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
