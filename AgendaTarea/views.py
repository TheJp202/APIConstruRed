from django.shortcuts import render
from .models import AgendaTarea
from .serializers import AgendaTareaSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def agendaTareaLC(request):
    if request.method == 'GET':
        agendaTarea = AgendaTarea.objects.all()
        serializer = AgendaTareaSerializer(agendaTarea, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AgendaTareaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def agendaTareaUD(request, pk):
    agendaTarea = get_object_or_404(AgendaTarea, pk=pk)
    if request.method == 'GET':
        serializer = AgendaTareaSerializer(agendaTarea)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = AgendaTareaSerializer(agendaTarea, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        agendaTarea.delete()
        return Response(status=204)