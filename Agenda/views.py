from django.shortcuts import render
from .models import Agenda
from .serializers import AgendaSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def agendaLC(request):
    if request.method == 'GET':
        agenda = Agenda.objects.all()
        serializer = AgendaSerializer(agenda, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AgendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def agendaUD(request, pk):
    agenda = get_object_or_404(Agenda, pk=pk)
    if request.method == 'GET':
        serializer = AgendaSerializer(agenda)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = AgendaSerializer(agenda, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        agenda.delete()
        return Response(status=204)