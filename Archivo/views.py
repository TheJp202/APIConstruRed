from django.shortcuts import render
from .models import Archivo
from .serializers import ArchivoSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
from rest_framework.parsers import MultiPartParser, FormParser


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def archivoLC(request):
    if request.method == 'GET':
        archivo = Archivo.objects.all()
        serializer = ArchivoSerializer(archivo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArchivoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@parser_classes([MultiPartParser, FormParser])
def archivoUD(request, pk):
    archivo = get_object_or_404(Archivo, pk=pk)
    if request.method == 'GET':
        serializer = ArchivoSerializer(archivo)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = ArchivoSerializer(archivo, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        archivo.delete()
        return Response(status=204)