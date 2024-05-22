from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TipoMensaje
from .serializers import TipoMensajeSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def tipoMensajeLC(request):
    if request.method == 'GET':
        tipoMensaje = TipoMensaje.objects.all()
        serializer = TipoMensajeSerializer(tipoMensaje, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TipoMensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def tipoMensajeUD(request, pk):
    tipoMensaje = get_object_or_404(TipoMensaje, pk=pk)
    if request.method == 'GET':
        serializer = TipoMensajeSerializer(tipoMensaje)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = TipoMensajeSerializer(tipoMensaje, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        tipoMensaje.delete()
        return Response(status=204)