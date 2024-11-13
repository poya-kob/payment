from django.urls import path

from .views import  register_page,user_login

urlpatterns = [
    path('user-login/', user_login),
    path('user-register/', register_page)
]
