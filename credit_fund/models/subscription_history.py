from django.db import models
from .fund import Fund


class SubscriptionHistory(models.Model):
    # صندوق مربوطه
    fund = models.ForeignKey(Fund, related_name='subscription_history', on_delete=models.CASCADE)

    # هزینه قبلی و فعلی
    old_fee = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="هزینه اشتراک قبلی")
    new_fee = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="هزینه اشتراک جدید")

    # تاریخ تغییرات
    changed_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ تغییر")

    def __str__(self):
        return f"هزینه اشتراک از {self.old_fee} به {self.new_fee} درتاریخ {self.changed_at} تغییر کرد."

    class Meta:
        verbose_name = "هزینه اشتراک"
        verbose_name_plural = "هزینه اشتراک"
        ordering = ['-changed_at']  # مرتب سازی بر اساس آخرین تغییرات
