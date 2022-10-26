from django.db import models

DelStatus = (
    ('1', 'Creado'),
    ('2', 'Entregado'),
)

class driver(models.Model):
    driverName = models.CharField(verbose_name="Nombre del conductor", max_length=200)
    driversId = models.PositiveSmallIntegerField(verbose_name='id del conductor')
    currentLat = models.PositiveSmallIntegerField(verbose_name="Latitud")
    currentLng = models.PositiveSmallIntegerField(verbose_name="Longitud")
    lastUpdate = models.DateTimeField(verbose_name="última actualización")

    def __str__(self):
        return self.driverName
    
class orders(models.Model):
    #Relationships
    driver = models.ForeignKey(driver, on_delete=models.CASCADE, verbose_name="conductor")

    ordersName = models.CharField(verbose_name="Nombre de la orden", max_length=200)
    deliveryTime = models.DateTimeField(verbose_name="Tiempo de entrega")
    pickUp = models.CharField(verbose_name="Recogida", max_length=200)
    deliverTo = models.CharField(verbose_name="Destino", max_length=200)
    deliveryStatus = models.CharField(verbose_name="Estado", max_length=200, choices=DelStatus)

    updated = models.DateTimeField(auto_now=True) #takes a snapshot everytime the field is updated
    created = models.DateTimeField(auto_now_add=True) #takes a snapshot when the instance is created

    def __str__(self):
        return self.ordersName