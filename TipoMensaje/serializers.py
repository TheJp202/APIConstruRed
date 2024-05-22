from rest_framework import serializers
from .models import TipoMensaje

class TipoMensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMensaje
        fields = '__all__'