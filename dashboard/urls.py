from . import views
from django.urls import path

urlpatterns = [
    path('', views.DashHome, name='dashboard-home'),
]