from django.shortcuts import render
from .models import Proyecto
from .serializers import ProyectoSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
from rest_framework.parsers import MultiPartParser, FormParser



@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def proyectoLC(request):
    if request.method == 'GET':
        proyecto = Proyecto.objects.all()
        serializer = ProyectoSerializer(proyecto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProyectoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@parser_classes([MultiPartParser, FormParser])
def proyectoUD(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'GET':
        serializer = ProyectoSerializer(proyecto)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = ProyectoSerializer(proyecto, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        proyecto.delete()
        return Response(status=204)