from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TipoInforme
from .serializers import TipoInformeSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def tipoInformeLC(request):
    if request.method == 'GET':
        tipoInforme = TipoInforme.objects.all()
        serializer = TipoInformeSerializer(tipoInforme, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TipoInformeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def tipoInformeUD(request, pk):
    tipoInforme = get_object_or_404(TipoInforme, pk=pk)
    if request.method == 'GET':
        serializer = TipoInformeSerializer(tipoInforme)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = TipoInformeSerializer(tipoInforme, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        tipoInforme.delete()
        return Response(status=204)