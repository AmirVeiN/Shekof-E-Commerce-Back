# Generated by Django 5.0.6 on 2024-07-04 23:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_phonecode_expiration_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonecode',
            name='expiration_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 4, 23, 15, 34, 918928, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]