import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = None
    phone_number = models.CharField(max_length=11, validators=[MinLengthValidator(11)], unique=True)
    user_code = models.UUIDField(auto_created=True, unique=True, default=uuid.uuid4)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def return_full_name(self):
        return f"{self.first_name} {self.last_name}"
