# Generated by Django 4.1 on 2023-04-14 15:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("payapp", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="time_stamp",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
