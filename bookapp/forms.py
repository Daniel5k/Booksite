from django import forms
from .models import BookSearch

class bookSearchForm(forms.ModelForm):

    name_of_book = forms.CharField(max_length=100, widget = forms.TextInput(attrs= {
        'class': 'form-control me-2', 
        'placeholder': 'Enter name of Book',
    }))

    class Meta:
        model = BookSearch
        fields = ['name_of_Books',]