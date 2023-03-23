from django.shortcuts import render
from .forms import LogInForm, RegisterForm
import secrets


# Create your views here.
def home_page(request):
    return render(request, 'authenticate/home.html')


def login(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            login_cookie = secrets.token_hex(18)
            request.set_cookie('login_cookie', login_cookie)
            return render(request, 'authenticate/loading.html')
    form = LogInForm()
    return render(request, 'authenticate/clientLogin.html', {'form': form, 'url': 'login/client/'})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process to register
            return render(request, 'authenticate/loading.html')
    form = RegisterForm()
    return render(request, 'authenticate/register.html', {'form': form})


def loading(request):
    return render(request, 'authenticate/loading.html')


def gpt(request):
    return render(request, 'authenticate/gpt.html')