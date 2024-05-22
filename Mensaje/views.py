from django.shortcuts import render
from .models import Mensaje
from .serializers import MensajeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def mensajeLC(request):
    if request.method == 'GET':
        mensaje = Mensaje.objects.all()
        serializer = MensajeSerializer(mensaje, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def mensajeUD(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    if request.method == 'GET':
        serializer = MensajeSerializer(mensaje)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = MensajeSerializer(mensaje, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        mensaje.delete()
        return Response(status=204)