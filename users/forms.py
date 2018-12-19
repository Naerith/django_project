from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User #model which will be affected by is User, when we do a form.save it will save it into User model.
        fields = ['username', 'email', 'password1', 'password2'] #fields that we want in the form and in what order

class
