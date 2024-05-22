from rest_framework import serializers
from .models import EquipoProyecto

class EquipoProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoProyecto
        fields = '__all__'