# Generated by Django 5.0.6 on 2024-06-11 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonecode',
            name='expiration_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 11, 12, 45, 52, 333614, tzinfo=datetime.timezone.utc)),
        ),
    ]
