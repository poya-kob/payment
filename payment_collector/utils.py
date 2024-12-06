import jdatetime

from .models import InstallmentRePayment


def calculate_monthly_installments(accepted_request_loan):
    """
    محاسبه تاریخ‌های اقساط ماهانه به صورت شمسی.
    :param accepted_request_loan: درخواست وام تایید شده
    :return: لیستی از تاریخ‌های اقساط (نوع jdatetime.date)
    """
    # تاریخ شروع پرداخت از مدل درخواست وام
    start_date = accepted_request_loan.pay_date  # jdatetime.date

    # تعداد اقساط
    num_installments = accepted_request_loan.loan.term

    # روز ثابت (روز قسط اول)
    fixed_day = start_date.day

    # لیست تاریخ‌های اقساط
    installments = []

    # محاسبه اقساط
    for i in range(num_installments):
        # اضافه کردن ماه‌ها
        next_date = start_date + jdatetime.timedelta(days=30 * i)

        try:
            fixed_date = next_date.replace(day=fixed_day)
        except ValueError:
            # اگر ماه کمتر از روز ثابت باشد، آخرین روز ماه
            fixed_date = next_date + jdatetime.timedelta(days=30)
            fixed_date = fixed_date.replace(day=1) - jdatetime.timedelta(days=1)

        installments.append(fixed_date)

    return installments


def create_monthly_installments(accepted_request_loan):
    """
    ایجاد اقساط ماهانه برای وام تاییدشده.
    :param accepted_request_loan: درخواست وام تایید شده
    """
    installments = calculate_monthly_installments(accepted_request_loan)

    for installment_date in installments:
        # ذخیره قسط در دیتابیس
        # print(installment_date)
        InstallmentRePayment.objects.create(
            requested_loan=accepted_request_loan,
            installment_due_date=installment_date,  # ذخیره مستقیم jdatetime.date
        )
