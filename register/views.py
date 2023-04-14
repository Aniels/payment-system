from django.shortcuts import render, redirect, Http404
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from payapp.models.currency import Currency


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data.get('currency')
            if symbol != 'GBP':
                form.instance.balance = form.instance.balance * Currency.objects.get(symbol=symbol).rate
            form.save()
            return redirect('login')
    else:
        register_form = RegistrationForm()
    return render(request, 'authenticate/register.html', {'register_form': register_form})


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
    # return Http404()


def logout_view(request):
    logout(request)
    return redirect('home')
