from django.shortcuts import render
from .models import InformeAutomatico
from .serializers import InformeAutomaticoSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def informeAutomaticoLC(request):
    if request.method == 'GET':
        informeAutomatico = InformeAutomatico.objects.all()
        serializer = InformeAutomaticoSerializer(informeAutomatico, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = InformeAutomaticoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def informeAutomaticoUD(request, pk):
    informeAutomatico = get_object_or_404(InformeAutomatico, pk=pk)
    if request.method == 'GET':
        serializer = InformeAutomaticoSerializer(informeAutomatico)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = InformeAutomaticoSerializer(informeAutomatico, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        informeAutomatico.delete()
        return Response(status=204)