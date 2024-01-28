from django.contrib.auth.models import BaseUserManager
from . import constants as user_constants

class UserManager(BaseUserManager):
    def create_user(self, phone, email, username, password, **extra_fields):
        if not phone:
            raise ValueError("The phone must be set")
        if not username:
            raise ValueError("The username must be set")
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("user_type", user_constants.STUDENT)
        email = self.normalize_email(email)
        user = self.model(phone=phone,username=username,email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, username, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("user_type", user_constants.SUPERUSER)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(phone, username, email, password, **extra_fields)

