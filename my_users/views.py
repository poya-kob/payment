from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model

from .forms import LoginForm, RegisterForm

User = get_user_model()


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():
        phone_number = login_form.cleaned_data.get('phone_number')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, password=password, username=phone_number)

        if user is not None:
            login(request, user)
    return render(request, "loginpage.html", {'form': LoginForm})


def logout_page(request):
    logout(request)
    return redirect("/")


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        phone = register_form.cleaned_data.get('phone_number')
        password = register_form.cleaned_data.get('password')
        first_name = register_form.cleaned_data.get('first_name')
        last_name = register_form.cleaned_data.get('last_name')
        user = User.objects.create_user(phone, password, is_active=False, first_name=first_name,
                                        last_name=last_name)
        return redirect('/')
    return render(request, "registerpage.html", {'form': register_form})
