from rest_framework import serializers
from .models import InformeAutomatico

class InformeAutomaticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformeAutomatico
        fields = '__all__'