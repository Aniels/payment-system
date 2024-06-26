from django.contrib.auth.models import AbstractUser


from django.db import models


from payapp.models.currency import Currency

from .managers import CustomUserManager


class Account(AbstractUser):
    currency = models.ForeignKey(
        Currency, on_delete=models.DO_NOTHING, related_name='account_currency', default=1
    )
    balance = models.FloatField(default=1000.00)
    objects = CustomUserManager()

    def __str__(self):
        return self.get_username()

    def increase_balance(self, amount: float) -> None:
        self.balance += amount
        self.balance = self.balance.__round__(2)
        self.save()

    def reduce_balance(self, amount: float) -> None:
        self.balance -= amount
        self.balance = self.balance.__round__(2)
        self.save()