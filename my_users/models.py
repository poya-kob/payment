from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = None
    phone_number = models.CharField(max_length=11, unique=True)
    user_code = models.UUIDField(auto_created=True, unique=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
