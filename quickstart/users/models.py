from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Django User model."""

    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
