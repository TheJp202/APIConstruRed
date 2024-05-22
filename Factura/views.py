from django.shortcuts import render
from .models import Factura
from .serializers import FacturaSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def facturaLC(request):
    if request.method == 'GET':
        factura = Factura.objects.all()
        serializer = FacturaSerializer(factura, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FacturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def facturaUD(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    if request.method == 'GET':
        serializer = FacturaSerializer(factura)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = FacturaSerializer(factura, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        factura.delete()
        return Response(status=204)