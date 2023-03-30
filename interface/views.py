from django.shortcuts import render
from register.views import registration as register


def home_page(request):
    return render(request, 'authenticate/home.html')


def profile(request):
    return render(request, 'authenticate/profile.html')


def registration(request):
    return register(request)


def gpt(request):
    return render(request, 'authenticate/gpt.html')
