from django import forms
from payapp.models.transaction import Transaction


class Transaction_form(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['recipient', 'amount']
        widgets = {'amount': forms.NumberInput(attrs={'min': 0.00})}

