from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'authors','published_year', 'genres']
        widgets = {
            'authors': forms.CheckboxSelectMultiple(),
            'genres': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'authors': 'Автор(ы)',
            'published_year': 'Год публикации',
            'genres': 'Жанр(ы)',
        }

class AuthorForm(forms.ModelForm):
    birth_date = forms.DateField(
        required=False,
        input_formats=['%d.%m.%Y'],  # здесь формат день.месяц.год
        widget=forms.DateInput(attrs={'placeholder': 'ДД.ММ.ГГГГ'})
    )
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birth_date']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']