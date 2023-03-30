from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    balance = models.FloatField(default=1000.00)
    is_staff = models.BooleanField(default=False)
#     overwrite the fields
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)




