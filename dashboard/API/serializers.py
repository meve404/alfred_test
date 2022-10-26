from rest_framework.serializers import ModelSerializer
from dashboard.models import driver, orders

class OrderSerial(ModelSerializer):
    class Meta:
        model = orders
        fields = '__all__'

class DriverSerial(ModelSerializer):
    class Meta:
        model = driver
        fields = '__all__'