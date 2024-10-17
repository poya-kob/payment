from django.db import models

from my_users.models import User
from borrow.models import Loan


class InstallmentRePayment(models.Model):
    """
    بازپرداخت اقساط
    """
    User = models.ForeignKey(User, on_delete=models.PROTECT)
    loan = models.ForeignKey(Loan, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="")
    payment = models.DecimalField()
    pay_date = models.DateField()
    upload_date = models.DateField()
    is_verified = models.BooleanField(default=False)
