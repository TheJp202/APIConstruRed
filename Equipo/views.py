from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Equipo
from .serializers import EquipoSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def equipoLC(request):
    if request.method == 'GET':
        equipo = Equipo.objects.all()
        serializer = EquipoSerializer(equipo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EquipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def equipoUD(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == 'GET':
        serializer = EquipoSerializer(equipo)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = EquipoSerializer(equipo, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        equipo.delete()
        return Response(status=204)