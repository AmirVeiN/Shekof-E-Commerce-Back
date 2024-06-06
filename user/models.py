from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from user.managers import UserManager
from . import constants as user_constants
from datetime import timedelta
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json


class User(AbstractUser):
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.PositiveSmallIntegerField(
        choices=user_constants.USER_TYPE_CHOICES
    )

    USERNAME_FIELD = "phone"

    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return f"{self.phone}"


class PhoneCode(models.Model):
    phone = models.IntegerField()
    code = models.IntegerField()
    run_at = models.DateTimeField(auto_now_add=True)
    expiration_at = models.DateTimeField(default=timezone.now() + timedelta(minutes=5))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        delete_schedule, _ = IntervalSchedule.objects.get_or_create(
            every=5, period=IntervalSchedule.MINUTES
        )
        PeriodicTask.objects.create(
            interval=delete_schedule,
            name=f"Delete_UserPhoneCode_{self.code}_at_{self.expiration_at} ",
            task="user.tasks.delete_phone_code_verification",
            args=json.dumps([self.pk, self.code]),
            one_off=True,
            start_time=timezone.now() + timedelta(minutes=5),
        )

    def __str__(self):
        return f"{self.phone} -- {self.code}"
