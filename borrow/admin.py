from django.contrib import admin

from .models import Loan, RequestLoan

admin.site.register(Loan)
admin.site.register(RequestLoan)
