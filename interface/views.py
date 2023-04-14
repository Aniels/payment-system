from django.shortcuts import render
from register.models import Account
from payapp.models.transaction import Transaction
from payapp.froms import Transaction_form
from register.forms import RegistrationForm


def home(request):
    return render(request, 'authenticate/home.html')


def profile(request):
    user_id = request.user.id
    user = Account.objects.get(id=user_id)
    if user.is_staff:
        registration_form = RegistrationForm()
        payments = Transaction.objects.all()
        accounts = Account.objects.all()
        context = {'user': user, 'form': registration_form, 'payments': payments, 'accounts': accounts}
        return render(request, 'authenticate/admin.html', context)
    else:
        payments = Transaction.objects.filter(sender=user_id)
        transaction_form = Transaction_form()
        context = {'user': user, 'form': transaction_form, 'payments': payments}
        return render(request, 'authenticate/customer.html', context)

