from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request,'dashboard/welcomepage.html')

@login_required
def dashboard_index(request):
    return render(request, 'dashboard/index.html')


def user_accepted_loan(request):
    return request.user.user_accepted_loan()
