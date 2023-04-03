from django.db import models
from django.contrib.auth.models import User
from payapp.models import Currency
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency_symbol = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, default='GBP')
    balance = models.FloatField(default=1000.00)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
