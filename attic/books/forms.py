from django import forms

from books.models import Book


class BookForm(forms.ModelForm):
    """Форма создания/редактирования книг."""

    class Meta:
        model = Book
        fields = (
            'subgenre', 'name', 'text',
            'author', 'pub_house', 'pub_year',
            'image'
        )
