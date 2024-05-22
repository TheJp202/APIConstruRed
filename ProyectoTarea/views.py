from django.shortcuts import render
from .models import ProyectoTarea
from .serializers import ProyectoTareaSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def proyectoTareaLC(request):
    if request.method == 'GET':
        proyectoTarea = ProyectoTarea.objects.all()
        serializer = ProyectoTareaSerializer(proyectoTarea, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProyectoTareaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def proyectoTareaUD(request, pk):
    proyectoTarea = get_object_or_404(ProyectoTarea, pk=pk)
    if request.method == 'GET':
        serializer = ProyectoTareaSerializer(proyectoTarea)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = ProyectoTareaSerializer(proyectoTarea, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        proyectoTarea.delete()
        return Response(status=204)