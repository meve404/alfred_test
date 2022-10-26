from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from dashboard.models import driver, orders
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .serializers import OrderSerial, DriverSerial
from django.db.models import Q
import json

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /alfred-api',
        'GET /alfred-api/get-orders/:date',
        'GET /alfred-api/get-driver-orders/:date/:driverId',
        'GET /alfred-api/search-driver/:lat/:long/:dateTime',

        'POST /alfred-api/make-order/:driverId/:deliveryTime/:pickUp/:deliverTo',
    ]
    return Response(routes)

@api_view(['GET'])
def search_driver(request, lat, long, dateTime):
    radius = 40
    lat_rad = radius + lat
    lng_rad = radius + long
    try:
        convert_datetime = datetime.strptime(dateTime, '%Y-%m-%d %H:%M:%S.%f%z') # converts from str to datetime format
    except:
        response = [
                {
                    'id' : 500,
                    'answer': 'Error',
                    'Menssage' : 'La fecha se debe enviar con el formato: año-mes-día hora:min:segundos.microsegundos Zona Horaria',
                }
        ]

        return Response(response)

    with open("jobs/points/points.json", "r+") as jsonFile: # to update the db with the json points (simulates the endpoint)
        data = json.load(jsonFile)
        data_alfreds = data['alfreds']
        for data in data_alfreds:
            update_driver = driver.objects.get(driversId=data['id'])
            update_driver.currentLat = int(data['lat'])
            update_driver.currentLng = int(data['lng'])
            update_driver.lastUpdate = data['lastUpdate']
            update_driver.save()

    available_drivers = driver.objects.filter(Q(currentLat__gte=lat)& # gets the drivers within the radius typed
                                              Q(currentLat__lte=lat_rad)&
                                              Q(currentLng__gte=long)&
                                              Q(currentLng__lte=lng_rad))

    final_av_drivers = []
    if available_drivers: # looks for available drivers that are available within the date time sent and counts the driver's active orders
        for av_driver in available_drivers:
            if convert_datetime >= av_driver.lastUpdate: # cause it makes sure the driver is still on that place
                driver_orders = orders.objects.filter(Q(driver=av_driver)&
                                                      Q(deliveryStatus='1')).count() # checks if the driver has orders in place
                if driver_orders < 3: # if driver has less than 3 orders
                    final_av_drivers.append(av_driver)
    
    if final_av_drivers: # if there are available drivers, it gets the first driver on list
        av_driver_data = final_av_drivers[0]
        av_driver_serializer = DriverSerial(av_driver_data, many=False)
        return Response(av_driver_serializer.data)

    else:
        response = [
                {
                    'id' : 200,
                    'answer': 'Success',
                    'message' : 'No hay conductores disponibles en esa locación, intente más tarde',
                }
        ]

        return Response(response)

@api_view(['GET'])
def get_driver_orders(request, date, driverId):
    try:
        convert_date = datetime.strptime(date, '%Y-%m-%d') # converts from str to datetime format
        driver_orders_data = orders.objects.filter(Q(created__date=convert_date.date()) &
                                                Q(driver__id=driverId)
                                                ).order_by('created__time__hour') # orders the query hourly
        driver_orders_serializer = OrderSerial(driver_orders_data, many=True) # many = False when is one element

        return Response(driver_orders_serializer.data)
    except:
        response = [
                {
                    'id' : 500,
                    'answer': 'Error',
                    'Menssage' : 'La fecha se debe enviar con el formato: año-mes-día',
                }
        ]
        return Response(response)

@api_view(['GET'])
def get_orders(request, date):
    try:
        convert_date = datetime.strptime(date, '%Y-%m-%d') # converts from str to datetime format
        orders_data = orders.objects.filter(created__date=convert_date.date()).order_by('created__time__hour') # orders the query hourly
        orders_serializer = OrderSerial(orders_data, many=True) # many = False when is one element

        return Response(orders_serializer.data)
    except:
        response = [
                {
                    'id' : 500,
                    'answer': 'Error',
                    'Menssage' : 'La fecha se debe enviar con el formato: año-mes-día',
                }
        ]
        return Response(response)

@api_view(['POST'])
def make_order(request, driverId, deliveryTime, pickUp, deliverTo):
    assigned_driver = get_object_or_404(driver, driversId=int(driverId))
    try:
        convert_datetime = datetime.strptime(deliveryTime, '%Y-%m-%d %H:%M:%S.%f%z') # converts from str to datetime format
        ordersName = f'{assigned_driver}, {convert_datetime.date()} {convert_datetime.time()}'
        new_order = orders(driver=assigned_driver, ordersName=ordersName, deliveryTime=convert_datetime, pickUp=pickUp, 
                        deliverTo=deliverTo, deliveryStatus='1')
        new_order.save()

        response = [
                {
                    'id' : 200,
                    'answer': 'Success',
                    'order' : ordersName,
                }
        ]
    except:
        response = [
                {
                    'id' : 500,
                    'answer': 'Error',
                    'Menssage' : 'La fecha se debe enviar con el formato: año-mes-día hora:min:segundos.microsegundos Zona Horaria',
                }
        ]
    return Response(response)