from django.db import models
from .fund import Fund


class Account(models.Model):
    # شماره کارت مرتبط با صندوق
    _card_number = models.CharField(max_length=30, verbose_name="شماره کارت")

    # صندوق مربوطه
    fund = models.ForeignKey(Fund, related_name='accounts', on_delete=models.CASCADE)

    def __str__(self):
        return f"شماره کارت  {self._card_number} - صندوق: {self.fund.name}"

    @property
    def card_number(self):
        if self._card_number:
            return '-'.join([self._card_number[i:i + 4] for i in range(0, len(self._card_number), 4)])
        return ""

    @card_number.setter
    def card_number(self, value):
        """Setter for card number. Validates the format before setting it."""
        if self.is_valid_card_number(value):
            self._card_number = value
        else:
            raise ValueError("فرمت کارت اشتباه است.")

    def is_valid_card_number(self, card_number):
        """Simple validation for card number format (e.g., 16 digits)."""
        return card_number.isdigit() and len(card_number) == 16

    class Meta:
        verbose_name = "شماره کارت"
        verbose_name_plural = "شماره کارت"
