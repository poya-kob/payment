import uuid
from django.contrib.auth import get_user_model

from django.db import models
from django_jalali.db import models as jmodels

from payment_collector.utils import create_user_refund

User = get_user_model()


class Loan(models.Model):
    """
    تعریف وام
    """
    loan_code = models.UUIDField(auto_created=True, unique=True, default=uuid.uuid4)
    term = models.IntegerField(null=True, blank=True)  # تعداد ماه های اقساط
    start_date = jmodels.jDateField()  # تاریخ شروع پذیره نویسی
    end_date = jmodels.jDateField()  # تاریخ پایان پذیره نویسی
    amount = models.DecimalField(default=None, max_digits=10, decimal_places=2)  # مبلغ کل وام
    status = models.CharField(max_length=50, choices=[
        ('end', "پایان یافته"),
        ('underwriting', "درحال پذیره نویسی"),
        ('default', "پیش فرض"),
    ])
    number_of_loan_payable = models.SmallIntegerField()  # تعداد وام های قابل پرداخت

    class Meta:
        verbose_name = 'وام'
        verbose_name_plural = "وام"


class RequestLoan(models.Model):
    """
    درخواست وام
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    loan = models.ForeignKey(Loan, on_delete=models.PROTECT)
    request_date = jmodels.jDateField(auto_now_add=True)
    pay_date = jmodels.jDateField(null=True, blank=True)  # تاریخ پرداخت وام
    refund_amount = models.DecimalField(default=None, max_digits=10, decimal_places=2, null=True,
                                        blank=True)  # باقیمانده بازپرداخت
    status = models.CharField(max_length=50, default='warning', choices=[
        ('warning', "درحال بررسی"),
        ('danger', "رد شده"),
        ('success', "تایید شده"),
    ])
    __orginal_status = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_status = self.status

    def save(self, *args, **kwargs):
        if self.__original_status != self.status:
            if self.status == 'success':
                self.refund_amount = self.loan.amount / self.loan.number_of_loan_payable
                create_user_refund(self)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'درخواست '
        verbose_name_plural = "درخواست"
