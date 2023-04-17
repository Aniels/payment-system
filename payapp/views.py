from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from register.models import Account
from .froms import Transaction_form


@login_required
def transfer(request):
    if request.method == 'POST':
        form = Transaction_form(request.POST)
        if form.is_valid():
            sender = Account.objects.get(username=request.user.username)
            form.instance.sender = sender
            form.instance.currency = sender.currency
            instance = form.save()
            instance.execute()
            return redirect('profile')


@login_required
def require_transfer(request):
    if request.method == 'POST':
        form = Transaction_form(request.POST)
        if form.is_valid():
            recipient = Account.objects.get(username=request.user.username)
            form.instance.sender = recipient
            form.instance.currency = recipient.currency
            form.save()
            return redirect('profile')
