from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rol
from .serializers import RolSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def rolLC(request):
    if request.method == 'GET':
        rol = Rol.objects.all()
        serializer = RolSerializer(rol, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def rolUD(request, pk):
    rol = get_object_or_404(Rol, pk=pk)
    if request.method == 'GET':
        serializer = RolSerializer(rol)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = RolSerializer(rol, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        rol.delete()
        return Response(status=204)