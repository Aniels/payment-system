from django.db import models
from register.models import Account
from django.db import transaction


class Transaction(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='sender')
    recipient = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='receiver')
    amount = models.FloatField()
    time_stamp = models.DateTimeField(auto_now=True, null=True)

    @transaction.atomic
    def execute(self):
        if self.sender.balance > self.amount:
            self.sender.reduce_balance(self.amount)
            rate = self.recipient.currency/self.sender.currency
            self.recipient.increase_balance(self.amount*rate)