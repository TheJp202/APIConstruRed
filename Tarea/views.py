from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tarea
from .serializers import TareaSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def tareaLC(request):
    if request.method == 'GET':
        tarea = Tarea.objects.all()
        serializer = TareaSerializer(tarea, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TareaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def tareaUD(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'GET':
        serializer = TareaSerializer(tarea)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = TareaSerializer(tarea, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        tarea.delete()
        return Response(status=204)