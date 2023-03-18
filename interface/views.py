from django.shortcuts import render
from .forms import LogInForm, RegisterForm
import secrets


# Create your views here.
def wellcome(request):
    return render(request, 'authenticate/wellcome.html')


def login(request):
    form = LogInForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        login_cookie = secrets.token_hex(16)
        request.set_cookie('login_cookie', login_cookie)
        return render(request, 'authenticate/loading.html')


def login_client(request):
    if request.method == "POST":
        return login(request)
    form = LogInForm()
    return render(request, 'authenticate/clientLogin.html', {'form': form, 'url': 'login/client/'})


def login_admin(request):
    if request.method == "POST":
        return login(request)
    form = LogInForm()
    return render(request, 'authenticate/adminLogin.html', {'form': form, 'url': 'login/admin/'})


# @csrf_exempt
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
