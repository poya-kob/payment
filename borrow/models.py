from django.db import models
from my_users.models import User
from django_jalali.db import models as jmodels


class Loan(models.Model):
    """
    تعریف وام
    """
    loan_code = models.UUIDField(auto_created=True, unique=True)
    term = models.IntegerField(null=True, blank=True)
    start_date = jmodels.jDateField()
    end_date = jmodels.jDateField()
    amount = models.DecimalField()
    status = models.CharField(max_length=50, choices=[
        ('end', "پایان یافته"),
        ('underwriting', "درحال پذیره نویسی"),
        ('default', "پیش فرض"),
    ])
    number_of_loan_payable = models.SmallIntegerField()


class RequestLoan(models.Model):
    """
    درخواست وام
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    loan = models.ForeignKey(Loan, on_delete=models.PROTECT)
    request_date = jmodels.jDateField()
    refund_amount = models.DecimalField(default=None)  # باقیمانده بازپرداخت
    status = models.CharField(max_length=50, choices=[
        ('pending', "در انتظار تایید"),
        ('approved', "تایید شده"),
        ('rejected', "رد شده"),
        ('paid', "پرداخت شده"),
        ('default', "پیش فرض"),
    ])
