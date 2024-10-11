from django.db import models

from my_users.models import User


class Payment(models.Model):
    User = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="")
    amount = models.IntegerField()
    pay_date = models.DateField()
    upload_date = models.DateField()
    is_verified = models.BooleanField(default=False)

