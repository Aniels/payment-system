from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from .models import Depositor


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and log in the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user_obj = User.objects.get(username=username)
                depositor = Depositor(account=user_obj)
                depositor.save()
                login(request, user)
                return render(request, 'authenticate/profile.html',
                              {'username': user_obj.get_username(), 'balance': depositor.balance})
    else:
        form = CustomUserCreationForm()
    return render(request, 'authenticate/register.html', {'form': form})
