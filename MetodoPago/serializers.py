from rest_framework import serializers
from .models import MetodoPago

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'