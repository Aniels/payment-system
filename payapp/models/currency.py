from django.db import models


class Currency(models.Model):
    symbol = models.CharField(max_length=3, primary_key=True, unique=True)
    country = models.CharField(max_length=30, unique=True)
    rate = models.FloatField()

    def __str__(self):
        return self.symbol
