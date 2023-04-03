from django.shortcuts import render
from .forms import LogInForm, RegisterForm
import secrets


# Create your views here.
def home(request):
    return render(request, 'authenticate/home.html')


def profile(request):
    return render(request, 'authenticate/profile.html')
