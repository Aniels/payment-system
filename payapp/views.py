from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .froms import Transaction_form
from register.models import Account


@login_required
@transaction.atomic
def transfer(request):
    if request.method == 'POST':
        form = Transaction_form(request.POST)
        if form.is_valid():
            account = Account.objects.get(username=request.user.username)
            form.instance.sender = account
            form.instance.currency = account.currency
            form.save()
            return redirect('profile')
