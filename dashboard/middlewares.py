from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware:
    """
    این middleware بررسی می‌کند که آیا کاربر وارد سیستم شده است یا خیر.
    اگر کاربر وارد نشده باشد، او را به صفحه ورود هدایت می‌کند.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # مسیرهایی که باید برای کاربران لاگین‌شده باشند
        if request.path.startswith('/dashboard/'):  #  مسیرهایی که با '/dashboard/' شروع می‌شود
            if not request.user.is_authenticated:
                return redirect(reverse('user-login'))  # صفحه ورود را هدایت می‌کند

        response = self.get_response(request)
        return response
