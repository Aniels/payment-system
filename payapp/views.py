from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from register.models import Account
from .froms import Transaction_form


@login_required
def transfer(request):
    if request.method == 'POST':
        form = Transaction_form(request.POST)
        if form.is_valid():
            account = Account.objects.get(username=request.user.username)
            form.instance.sender = account
            form.instance.currency = account.currency
            instance = form.save()
            instance.execute()
            return redirect('profile')
