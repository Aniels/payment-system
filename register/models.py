from django.db import models
from django.contrib.auth.models import AbstractUser
from payapp.models.currency import Currency
from .managers import CustomUserManager


class Account(AbstractUser):
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, default='GBP', related_name='account_currency')
    balance = models.FloatField(default=1000.00)
    objects = CustomUserManager()

    def __str__(self):
        return self.get_username()

    def increase_balance(self, amount):
        self.balance += amount
        self.save()

    def reduce_balance(self, amount):
        self.balance -= amount
        self.save()

