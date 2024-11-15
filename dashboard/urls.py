from django.urls import path, include

from .views import dashboard_index

urlpatterns = [
    path('dsashboard/', dashboard_index, name='dashboard'),
]
