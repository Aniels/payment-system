from django.shortcuts import render
from forms import TransferForm


def transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            pass
    else:
        form = TransferForm()
    return render(request, '/register.html', {'form': form})


def something_else(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        ...
    else:
        # Do something for anonymous users.
        ...
