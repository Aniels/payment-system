from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.db import models


class DepositorManager(BaseUserManager):
    # Your custom user manager implementation
    pass


class Depositor(AbstractBaseUser):

    account = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    balance = models.FloatField(default=1000.00)
    is_staff = models.BooleanField(default=False)
    username = User.get_username(self=account)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.account.username




