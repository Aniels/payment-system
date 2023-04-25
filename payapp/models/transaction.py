from django.db import models
from register.models import Account
from django.db import transaction


class Transaction(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='sender')
    recipient = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='receiver')
    amount = models.FloatField()
    time_stamp = models.DateTimeField(auto_now=True, null=True)
    is_executed = models.BooleanField(default=False)
    is_request = models.BooleanField(default=False)

    @transaction.atomic
    def execute(self):
        sender = self.sender
        recipient = self.recipient
        if sender.balance > self.amount:
            sender.reduce_balance(self.amount)
            rate = recipient.currency.rate / sender.currency.rate
            recipient.increase_balance(self.amount * rate)
            self.is_executed = True
            self.save()
            return True
        else:
            return False
