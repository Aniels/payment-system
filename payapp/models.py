from django.db import models
from django.utils.timezone import now


# Create your models here.
class Record(models.Model):

    payment_method = (
        ('T', 'transform'),
        ('C', 'credit'),
    )

    time_stamp = models.DateTimeField(default=now, blank=True)
    amount = models.FloatField()
    method = models.CharField(max_length=1, choices=payment_method)  # Not null




