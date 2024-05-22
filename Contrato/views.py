from django.shortcuts import render
from .models import Contrato
from .serializers import ContratoSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def contratoLC(request):
    if request.method == 'GET':
        contrato = Contrato.objects.all()
        serializer = ContratoSerializer(contrato, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContratoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def contratoUD(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    if request.method == 'GET':
        serializer = ContratoSerializer(contrato)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = ContratoSerializer(contrato, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        contrato.delete()
        return Response(status=204)