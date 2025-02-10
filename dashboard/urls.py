from django.urls import path

from .views import dashboard_index, welcome

urlpatterns = [
    path('welcome', welcome, name='welcome'),
    path('', dashboard_index, name='dashboard'),
]
