from django.db import models
from register.models import User
from django.utils.timezone import now


# Create your models here.
class Record(models.Model):

    payment_method = (
        ('T', 'transform'),
        ('C', 'credit'),
    )

    time_stamp = models.DateTimeField(default=now, blank=True)
    amount = models.FloatField()
    method = models.CharField(max_length=1, choices=payment_method, blank=False)  # Not null


class Operation(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    time = models.DateTimeField(auto_now_add=True)
