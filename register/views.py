from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate and log in the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return render('authenticate/profile.html', {'user': user})
    else:
        form = CustomUserCreationForm()
    return render(request, 'authenticate/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'authenticate/login.html'
    success_url = 'authenticate/profile.html'

