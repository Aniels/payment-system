from django.db import models


class Currency(models.Model):
    currency_code = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=10)
    country = models.CharField(max_length=30, unique=True)
    rate = models.FloatField()

    def __str__(self):
        return self.currency_code
