from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from user.managers import UserManager
from . import constants as user_constants


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=255, db_index=True)
    phone = models.CharField(unique=True, max_length=255, db_index=True)
    email = models.EmailField(unique=True, null=True, blank=True, db_index=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.PositiveSmallIntegerField(
        choices=user_constants.USER_TYPE_CHOICES
    )

    REQUIRED_FIELDS = ["username", "email"]
    USERNAME_FIELD = "phone"

    objects = UserManager()
    
