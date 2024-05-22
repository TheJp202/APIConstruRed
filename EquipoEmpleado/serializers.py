from rest_framework import serializers
from .models import EquipoEmpleado

class EquipoEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoEmpleado
        fields = '__all__'