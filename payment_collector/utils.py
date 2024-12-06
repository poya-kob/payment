from jdatetime import timedelta

from .models import InstallmentRePayment


def create_user_refund(accepted_request_loan):
    for _ in range(accepted_request_loan.loan.term):
        InstallmentRePayment.objects.create(requested_loan=accepted_request_loan,
                                            installment_due_date=accepted_request_loan.pay_date + timedelta(
                                                days=30 * (_ + 1)))
