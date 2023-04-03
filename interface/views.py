from django.shortcuts import render
from .forms import LogInForm, RegisterForm
import secrets


# Create your views here.
def home_page(request):
    return render(request, 'authenticate/home.html')


def loading(request):
    return render(request, 'authenticate/profile.html')
