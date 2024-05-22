from django.shortcuts import render
from .models import Cita
from .serializers import CitaSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def citaLC(request):
    if request.method == 'GET':
        cita = Cita.objects.all()
        serializer = CitaSerializer(cita, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CitaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def citaUD(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'GET':
        serializer = CitaSerializer(cita)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = CitaSerializer(cita, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        cita.delete()
        return Response(status=204)