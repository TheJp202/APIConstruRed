from rest_framework import serializers
from .models import TipoInforme

class TipoInformeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInforme
        fields = '__all__'