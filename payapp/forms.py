from django import forms


class TransferForm(forms.Form):
    receiver = forms.CharField()
    sender = forms.FloatField()
