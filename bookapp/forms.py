from django import forms
from .models import BookSearch
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class bookSearchForm(forms.ModelForm):

    name_of_book = forms.CharField(max_length=100, widget = forms.TextInput(attrs= {
        'class': 'form-control me-2', 
        'placeholder': 'Enter name of Book',
    }))

    class Meta:
        model = BookSearch
        fields = ['name_of_book']

class CreateUserForm(UserCreationForm):
    email =forms.CharField(max_length=255, widget=forms.EmailInput(attrs={
        'class': 'form-control',

        'placeholder' : 'Enter email address'
    }))
    password1 = forms.CharField(max_length=255, widget= forms.PasswordInput(attrs = {
        'class': 'form-control',

        'placeholder': 'Enter a strong Password',
    }))
    password2 = forms.CharField(max_length=255, widget= forms.PasswordInput(attrs = {
        'class': 'form-control',

        'placeholder': 'Re-confirm Password',
    }))
    username = forms.CharField(max_length=255, widget= forms.TextInput(attrs = {
        'class': 'form-control',
        'id': 'pwd',
        'placeholder': 'Enter Username',
    }))
    class Meta:
        model = User
        fields = [ 'email', 'username', 'password1', 'password2']