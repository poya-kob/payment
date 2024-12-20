from django.db import models


class Fund(models.Model):
    # فیلد نام صندوق
    name = models.CharField(max_length=100, verbose_name="نام صندوق")
    # تاریخ ایجاد صندوق (تاریخ و زمان ایجاد رکورد)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    # تاریخ آخرین بروزرسانی صندوق (در صورت تغییر موجودی یا سایر اطلاعات)
    last_modified = models.DateTimeField(auto_now=True, verbose_name="تاریخ آخرین بروزرسانی")
    # موجودی کل صندوق
    balance = models.DecimalField(
        max_digits=12,  # حداکثر تعداد ارقام (برای عدد کامل)
        decimal_places=2,  # تعداد اعشار
        default=0.00,  # مقدار پیش‌فرض
        verbose_name="موجودی صندوق"
    )
    # فیلد برای توضیحات اضافی
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    # فیلد برای وضعیت صندوق (فعال یا غیرفعال)
    status = models.BooleanField(default=False, verbose_name="وضعیت صندوق")
    __old_subscription_fee = None
    subscription_fee = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00, verbose_name="هزینه اشتراک ماهانه صندوق")

    def __str__(self):
        """
        نمایش اطلاعات صندوق در نمایش‌های مختلف
        """
        return f"{self.name} - موجودی: {self.balance}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__old_subscription_fee = self.subscription_fee

    def save(self, *args, **kwargs):
        if self.__old_subscription_fee != self.subscription_fee:
            from .subscription_history import SubscriptionHistory
            SubscriptionHistory.objects.create(
                fund=self,
                old_fee=self.__old_subscription_fee,
                new_fee=self.subscription_fee,
            )
        super(Fund, self).save(*args, **kwargs)

    def deposit(self, amount):
        """
        متد برای واریز وجه به صندوق
        """
        if amount > 0:
            self.balance += amount
            self.save()
        else:
            raise ValueError("مبلغ واریز باید مثبت باشد.")

    def withdraw(self, amount):
        """
        متد برای برداشت وجه از صندوق
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.save()
        else:
            raise ValueError("مبلغ برداشت باید مثبت باشد و موجودی کافی باشد.")

    class Meta:
        verbose_name = "صندوق"
        verbose_name_plural = "صندوق‌ها"
