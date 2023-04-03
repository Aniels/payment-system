from django.db import models


class Currency(models.Model):
    symbol = models.CharField(primary_key=True, required=True, unique=True)
    country = models.CharField(required=True, unique=True)
    rate = models.FloatField(required=True)
    verbose_name = country

    def __str__(self):
        return self.country


