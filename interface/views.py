from django.shortcuts import render
from register.models import Account
from payapp.froms import Transaction_form


def home(request):
    return render(request, 'authenticate/home.html')


def profile(request):
    user = Account.objects.get(id=request.user.id)
    form = Transaction_form()
    return render(request, 'authenticate/profile.html', {'user': user, 'transaction_form': form})
