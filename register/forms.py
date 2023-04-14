from django import forms
from django.contrib.auth.forms import UserCreationForm
from register.models import Account


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'currency']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
