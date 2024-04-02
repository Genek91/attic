from django import forms

from books.models import Book, Comment


class BookForm(forms.ModelForm):
    """Форма создания/редактирования книг."""

    class Meta:
        model = Book
        fields = (
            'subgenre', 'name', 'text',
            'author', 'pub_house', 'pub_year',
            'image',
        )


class CommentForm(forms.ModelForm):
    """Форма создания/редактирования комментариев."""
    text = forms.CharField()

    class Meta:
        model = Comment
        fields = (
            'text',
        )
