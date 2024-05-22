from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MetodoPago
from .serializers import MetodoPagoSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def metodoPagoLC(request):
    if request.method == 'GET':
        metodoPago = MetodoPago.objects.all()
        serializer = MetodoPagoSerializer(metodoPago, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MetodoPagoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def metodoPagoUD(request, pk):
    metodoPago = get_object_or_404(MetodoPago, pk=pk)
    if request.method == 'GET':
        serializer = MetodoPagoSerializer(metodoPago)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = MetodoPagoSerializer(metodoPago, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        metodoPago.delete()
        return Response(status=204)