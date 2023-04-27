from django.shortcuts import render, redirect, Http404
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from payapp.models.currency import Currency


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            currency_code = form.cleaned_data.get('currency')
            print(currency_code)
            if currency_code != 'GBP':
                print(currency_code)
                form.instance.balance = form.instance.balance * Currency.objects.get(currency_code=currency_code).rate
            form.save()
            return redirect('login')
        return redirect('register')
    else:
        return render(request, 'authenticate/register.html', {'register_form': RegistrationForm()})


def admin_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.instance.is_staff = True
            form.save()
            return redirect('profile')
        return Http404


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    form = LoginForm()
    return render(request, 'authenticate/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
