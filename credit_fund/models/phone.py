from django.db import models
from .fund import Fund


class Phone(models.Model):
    # شماره موبایل مرتبط با صندوق
    phone_number = models.CharField(max_length=20, verbose_name="شماره موبایل")

    # صندوق مربوطه
    fund = models.ForeignKey(Fund, related_name='phones', on_delete=models.CASCADE)

    def __str__(self):
        return f"شماره موبایل {self.phone_number} - صندوق: {self.fund.name}"

    class Meta:
        verbose_name = "موبایل"
        verbose_name_plural = "موبایل"
