from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reunion
from .serializers import ReunionSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def reunionLC(request):
    if request.method == 'GET':
        reunion = Reunion.objects.all()
        serializer = ReunionSerializer(reunion, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReunionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def reunionUD(request, pk):
    reunion = get_object_or_404(Reunion, pk=pk)
    if request.method == 'GET':
        serializer = ReunionSerializer(reunion)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = ReunionSerializer(reunion, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        reunion.delete()
        return Response(status=204)