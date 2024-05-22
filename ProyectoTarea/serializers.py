from rest_framework import serializers
from .models import ProyectoTarea

class ProyectoTareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectoTarea
        fields = '__all__'