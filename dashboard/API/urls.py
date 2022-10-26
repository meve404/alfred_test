from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('get-orders/<str:date>', views.get_orders),
    path('get-driver-orders/<str:date>/<str:driverId>', views.get_driver_orders),
    path('search-driver/<int:lat>/<int:long>/<str:dateTime>', views.search_driver),

    #-----------POST-----------------
    path('make-order/<str:driverId>/<str:deliveryTime>/<str:pickUp>/<str:deliverTo>', views.make_order),
]