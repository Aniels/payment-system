from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from register.models import Account
from .froms import Transaction_form, Request_form


@login_required
def transfer(request):
    if request.method == 'POST':
        form = Transaction_form(request.POST)
        if form.is_valid():
            sender = Account.objects.get(username=request.user.username)
            form.instance.sender = sender
            form.instance.currency = sender.currency
            instance = form.save()
            if instance.execute():
                return redirect('profile')
            else:
                return redirect('home')


@login_required
def require_transfer(request):
    if request.method == 'POST':
        form = Request_form(request.POST)
        if form.is_valid():
            recipient = Account.objects.get(username=request.user.username)
            form.instance.recipient = recipient
            form.instance.currency = recipient.currency
            form.instance.is_request = True
            form.save()
            return redirect('profile')
        return redirect('/')
    return HttpResponse('method should be POST')


@login_required
def execute_requirement(request):
    from payapp.models.transaction import Transaction

    aws = Transaction.objects.get(pk=22)

    print(request.POST)
    aws.execute()

    return redirect('profile')

