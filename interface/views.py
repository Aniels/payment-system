from django.shortcuts import render
from register.views import registration as register
from register.views import login as lg
from register.models import Depositor


def home_page(request):
    return render(request, 'authenticate/home.html')


def profile(request):
    user = request.user
    depositor =
    # need a payload to display
    return render(request, 'authenticate/profile.html', {'user': request.user})


def registration(request):
    return register(request)


def login(request):
    return lg(request)


def gpt(request):
    return render(request, 'authenticate/gpt.html')
