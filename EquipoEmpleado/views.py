from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EquipoEmpleado
from .serializers import EquipoEmpleadoSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def equipoEmpleadoLC(request):
    if request.method == 'GET':
        equipoEmpleado = EquipoEmpleado.objects.all()
        serializer = EquipoEmpleadoSerializer(equipoEmpleado, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EquipoEmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def equipoEmpleadoUD(request, pk):
    equipoEmpleado = get_object_or_404(EquipoEmpleado, pk=pk)
    if request.method == 'GET':
        serializer = EquipoEmpleadoSerializer(equipoEmpleado)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = EquipoEmpleadoSerializer(equipoEmpleado, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        equipoEmpleado.delete()
        return Response(status=204)