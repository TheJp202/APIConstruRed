from rest_framework import serializers
from .models import AgendaTarea

class AgendaTareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaTarea
        fields = '__all__'