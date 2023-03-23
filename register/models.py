from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    balance = models.FloatField()
    token = models.CharField(max_length=36)
#     overwrite the fields
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Operation(models.Model):
    sending_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    receiving_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    time = models.DateTimeField(auto_now_add=True)


