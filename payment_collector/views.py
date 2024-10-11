from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import PaymentForm
from my_users.models import User


@login_required
def upload_pay(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
    else:
        form = PaymentForm()
    return render(request, "", {'form': form})


@login_required
def user_payment_list(request):
    return render(request, "")


@login_required
def admin_control_panel(request):
    users = User.objects.all()
    return render(request, "", {'users': users})
