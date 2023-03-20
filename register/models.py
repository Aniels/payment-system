from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=36)
