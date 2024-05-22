from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EquipoProyecto
from .serializers import EquipoProyectoSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def equipoProyectoLC(request):
    if request.method == 'GET':
        equipoProyecto = EquipoProyecto.objects.all()
        serializer = EquipoProyectoSerializer(equipoProyecto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EquipoProyectoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def equipoProyectoUD(request, pk):
    equipoProyecto = get_object_or_404(EquipoProyecto, pk=pk)
    if request.method == 'GET':
        serializer = EquipoProyectoSerializer(equipoProyecto)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = EquipoProyectoSerializer(equipoProyecto, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        equipoProyecto.delete()
        return Response(status=204)