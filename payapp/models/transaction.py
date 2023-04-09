from django.db import models
from register.models import Account
from payapp.models.currency import Currency
from django.core.validators import MinValueValidator


class Transaction(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='sender')
    recipient = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='receiver')
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, related_name='Currency')
    amount = models.FloatField()
