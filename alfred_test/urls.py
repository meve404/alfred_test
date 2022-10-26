from django.contrib import admin
from django.urls import path, include
from jobs.updater import start_update_points

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('alfred-api/', include('dashboard.API.urls')),
]

start_update_points()