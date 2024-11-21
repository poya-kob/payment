from django.db import models
from django.contrib.auth import get_user_model

from django_jalali.db import models as jmodels

User = get_user_model()


class InstallmentRePayment(models.Model):
    """
    بازپرداخت اقساط
    """
    requested_loan = models.ForeignKey('borrow.RequestLoan', on_delete=models.PROTECT)
    image = models.ImageField(upload_to="", null=True, blank=True)
    payment = models.DecimalField(decimal_places=3, max_digits=10, null=True, blank=True)
    installment_due_date = jmodels.jDateField()  # تاریخ سررسید قسط
    upload_date = jmodels.jDateField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = "قسط"
        verbose_name_plural = verbose_name
