from django.shortcuts import render
from register.models import Account
from payapp.models.transaction import Transaction
from payapp.froms import Transaction_form, Request_form
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
        transaction = Transaction.objects.filter(sender=user_id)
        payments = transaction.filter(is_executed=True)
        require_transfers = transaction.filter(is_request=True, is_executed=False)
        transaction_form = Transaction_form()
        request_form = Request_form()
        context = {'user': user,
                   'form': transaction_form,
                   'payments': payments,
                   'request_form': request_form,
                   'require_transfer': require_transfers
                   }
        return render(request, 'authenticate/customer.html', context)

