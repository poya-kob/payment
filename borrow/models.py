from django.db import models
from my_users.models import User


class Loan(models.Model):
    loan_code = models.UUIDField(auto_created=True, unique=True)
    term = models.IntegerField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    amount = models.DecimalField()
    status = models.CharField(max_length=50, choices=[
        ('pending', "در انتظار تایید"),
        ('approved', "تایید شده"),
        ('rejected', "رد شده"),
        ('paid', "پرداخت شده"),
        ('underwriting', "درحال پذیره نویسی"),
        ('default', "پیش فرض"),
    ])
