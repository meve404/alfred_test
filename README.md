# alfred_test
Para ejecutar:
- Clonar este repo.
- En la carpeta en el que se encuentra manage.py ejectuar: python manage.py test (para ejecutar todos los modulos del unitTest al mismo tiempo)
- Para ejecutar uno a uno los modulos: python manage.py test dashboard.tests.EndPointsTest.(nombre del modulo que se quiere ejecutar)
- Ejemplo: python manage.py test dashboard.tests.EndPointsTest.test_get_orders_success
- Los nombres de los modulos son: 
- test_make_order_point_success (para crear una orden nueva)
- test_make_order_point_fail (Si el usuario envía la fecha con un formato diferente a año-mes-día hora:min:segundos.microsegundos Zona Horaria)
- test_get_orders_success (para obtener las ordenes dependiendo de la fecha)
- test_get_orders_fail (Si el usuario envía la fecha con un formato diferente a año-mes-día)
- test_get_driver_orders_success (para conseguir las ordenes del conductor elegido)
- test_get_driver_orders_fail (Si el usuario envía la fecha con un formato diferente a año-mes-día)
- test_search_driver_success (para localizar un conductor dependiendo de su locación, la fecha/hora y si tiene menos de 3 domicilios)
- test_search_driver_fail_date (Si el usuario envía la fecha con un formato diferente a año-mes-día hora:min:segundos.microsegundos Zona Horaria)
- test_search_driver_fail_search (si no hay conductores disponibles)
