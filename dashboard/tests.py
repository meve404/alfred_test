from django.test import TestCase
import requests
from django.utils import timezone
from datetime import datetime
import random

class EndPointsTest(TestCase):
    def test_make_order_point_success(self): # Se logra crear una orden
        now = timezone.now()
        driver = random.randint(1, 20)
        pickUpCoordinates = [22,6]
        deliverToCoordinates = [18,14]
        response = requests.post(f'http://dummyweb.live/alfred-api/make-order/{driver}/{now}/{pickUpCoordinates}/{deliverToCoordinates}')
        Translate_response = response.json()
        print('\nRespuesta_servidor_hacer_orden:',Translate_response, '\n')
        check_response_id = Translate_response[0]['id']
        self.assertEqual(check_response_id, 200) # el id debe ser 200
    
    def test_make_order_point_fail(self): # El formato no de DateTime no es el esperado
        now = '2022-10-21'
        driver = 8
        pickUpCoordinates = [92,23]
        deliverToCoordinates = [83,4]
        response = requests.post(f'http://dummyweb.live/alfred-api/make-order/{driver}/{now}/{pickUpCoordinates}/{deliverToCoordinates}')
        Translate_response = response.json()
        print('\nRespuesta_servidor_fallar_hacer_orden:',Translate_response, '\n')
        check_response_id = Translate_response[0]['answer']
        self.assertEqual(check_response_id, 'Error') # La variable answer debe ser error
    
    def test_get_orders_success(self): # se logra conseguir las ordenes
        date = '2022-10-25'
        response = requests.get(f'http://dummyweb.live/alfred-api/get-orders/{date}')
        Translate_response = response.json()
        print('\nRespuesta_servidor_obtener_orden:',Translate_response, '\n')
        check_response_id = Translate_response[0]['id']
        self.assertEqual(check_response_id, 1) # Debe conseguir la orden 1 para esta fecha
    
    def test_get_orders_fail(self): # El formato no de Date no es el esperado
        date = '25-10-2022'
        response = requests.get(f'http://dummyweb.live/alfred-api/get-orders/{date}')
        Translate_response = response.json()
        print('\nRespuesta_servidor_fallar_obtener_orden:',Translate_response, '\n')
        check_response_id = Translate_response[0]['answer']
        self.assertEqual(check_response_id, 'Error') # La variable answer debe ser error
    
    def test_get_driver_orders_success(self): # se logran conseguir las ordenes del conductor assignado
        date = '2022-10-25'
        driver = 15
        response = requests.get(f'http://dummyweb.live/alfred-api/get-driver-orders/{date}/{driver}') 
        Translate_response = response.json()
        print('\nRespuesta_servidor_obtener_orden_conduct:',Translate_response, '\n')
        check_response_id = Translate_response[0]['ordersName']
        # Debe conseguir el nombre de la orden del conductor Juan (1) hecha el 2022-10-24 20:56:14
        self.assertEqual(check_response_id, 'David, 2022-10-25 22:50:16.055323')
    
    def test_get_driver_orders_fail(self): # El formato no de Date no es el esperado
        date = '25-10-2022'
        driver = 1
        response = requests.get(f'http://dummyweb.live/alfred-api/get-driver-orders/{date}/{driver}') 
        Translate_response = response.json()
        print('\nRespuesta_servidor_fallar_obtener_orden_conduct:',Translate_response, '\n')
        check_response_id = Translate_response[0]['answer']
        self.assertEqual(check_response_id, 'Error') # La variable answer debe ser error
    
    def test_search_driver_success(self): #se consigue un conductor dependiendo de su locacion y la fecha/hora
        now = timezone.now()
        lat = 20
        lng = 60
        response = requests.get(f'http://dummyweb.live/alfred-api/search-driver/{lat}/{lng}/{now}')
        Translate_response = response.json()
        print('\nRespuesta_servidor_buscar_conductor:',Translate_response, '\n')
        check_response_id = Translate_response['id']
        self.assertEqual(type(check_response_id), type(1))
    
    def test_search_driver_fail_date(self): # El formato no de Date/time no es el esperado
        now = '24-10-2022'
        lat = 10
        lng = 70
        response = requests.get(f'http://dummyweb.live/alfred-api/search-driver/{lat}/{lng}/{now}')
        Translate_response = response.json()
        print('\nRespuesta_servidor_fallar_buscar_conductor_fecha:',Translate_response, '\n')
        check_response_id = Translate_response[0]['answer']
        self.assertEqual(check_response_id, 'Error') # La variable answer debe ser error

    def test_search_driver_fail_search(self): # no se consigue un conductor
        zone = timezone.now().tzinfo
        now = datetime(year=2022, month=10, day=22, hour=23, minute=0, second=0, microsecond=233, tzinfo=zone)
        lat = 70
        lng = 90
        response = requests.get(f'http://dummyweb.live/alfred-api/search-driver/{lat}/{lng}/{now}')
        Translate_response = response.json()
        print('\nRespuesta_servidor_fallar_buscar_conductor_404:',Translate_response, '\n')
        check_response_id = Translate_response[0]['message']
        # el mensaje que muestra que no hay conductores disponibles
        self.assertEqual(check_response_id, 'No hay conductores disponibles en esa locación, intente más tarde')