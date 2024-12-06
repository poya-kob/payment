from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter

# You need to import this for adding jalali calendar widget
import django_jalali.admin as jadmin

from .models import Loan, RequestLoan


class LoanAdmin(admin.ModelAdmin):
    list_filter = (
        ('start_date', JDateFieldListFilter),
        ('end_date', JDateFieldListFilter),
    )


class RequestLoadnAdmin(admin.ModelAdmin):
    list_filter = (
        ('request_date', JDateFieldListFilter),
        ('pay_date', JDateFieldListFilter),
    )


admin.site.register(Loan, LoanAdmin)
admin.site.register(RequestLoan, RequestLoadnAdmin)
