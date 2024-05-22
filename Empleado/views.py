from django.http import JsonResponse
from rest_framework.response import Response
from .models import Empleado
from .serializers import EmpleadoSerializer
from Rol.models import Rol
from rest_framework.decorators import api_view, parser_classes
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser

@api_view(['GET'])
def empleadoL(request):
    if request.method == 'GET':
        empleado = Empleado.objects.all()
        serializer = EmpleadoSerializer(empleado, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@parser_classes([MultiPartParser, FormParser])
def empleadoUD(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'GET':
        serializer = EmpleadoSerializer(empleado)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = EmpleadoSerializer(empleado, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        empleado.delete()
        return Response(status=204)


@api_view(['POST'])
def login_view(request):
    email = request.data.get('Correo') 
    raw_password = request.data.get('Contraseña')
    user_profile = Empleado.objects.filter(Correo=email).first()    
    if user_profile is None:
        return JsonResponse({"error": "Empleado no encontrado"}, status=404)

    if check_password(raw_password, user_profile.Contraseña):
        request.session['user_id'] = user_profile.id
        if user_profile.Foto:
            foto_url = user_profile.Foto.url
        else:
            foto_url = ""
        user_data = {
            "id": user_profile.id,
            "Foto": foto_url,
            "Nombres": user_profile.Nombres,
            "Apellidos": user_profile.Apellidos,
            "DNI":user_profile.DNI,
            "FechaContratacion":user_profile.FechaContratacion,
            "Telefono":user_profile.Telefono,
            "Correo": user_profile.Correo,
            "Rol": {
                "id": user_profile.Rol.id,
                "Nombre": user_profile.Rol.Nombre
            }
        }
        response_data = {"message": "Inicio de sesión exitoso", "user_profile": user_data}
        response = JsonResponse(response_data)
        response.set_cookie(key='sessionid', value=request.session.session_key, samesite='None')
        return response
    else:
        return JsonResponse({"error": "Credenciales inválidas"}, status=400)
    
    
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def register_view(request):
    nombres = request.data.get('Nombres')
    apellidos = request.data.get('Apellidos')
    dni = request.data.get('DNI')
    fecha_contratacion = request.data.get('FechaContratacion')
    telefono = request.data.get('Telefono')
    email = request.data.get('Correo')
    rol = request.data.get('Rol')
    foto = request.data.get('Foto')
    raw_password = request.data.get('Contraseña')
    hashed_password = make_password(raw_password)
    rol_instance = get_object_or_404(Rol, id=rol)
    if not all([nombres, apellidos, dni, fecha_contratacion, telefono, email, rol,hashed_password]):
        return JsonResponse({'error': 'Se requieren todos los campos'}, status=400)
    if Empleado.objects.filter(Correo=email).exists():
        return JsonResponse({'error': 'El email ya está en uso'}, status=400)
    user = Empleado.objects.create(
        Foto=foto,
        Nombres=nombres,
        Apellidos=apellidos,
        DNI = dni,
        FechaContratacion = fecha_contratacion,
        Telefono = telefono,
        Correo=email,
        Contraseña=hashed_password,
        Rol=rol_instance)
    
    if user:
        return JsonResponse({'message':'Empleado registrado exitosamente'}, status=201)
    else:
        return JsonResponse({'error': 'Error al crear el usuario'}, status=500)

@api_view(['POST'])
def logout_view(request):
    request.session.flush()
    response = Response({'message': 'Cierre de sesión exitoso'})
    response.delete_cookie('sessionid')
    return response


@api_view(['POST'])
def user_data_cookie_view(request):
    sessionid = request.COOKIES.get('sessionid')
    if sessionid:
        try:
            session = Session.objects.get(session_key=sessionid)
            user_id = session.get_decoded().get('user_id')
            user_profile = Empleado.objects.get(id=user_id)
            user_data = {
                "id": user_profile.id,
                "Nombres": user_profile.Nombres,
                "Apellidos": user_profile.Apellidos,
                "DNI":user_profile.DNI,
                "FechaContratacion":user_profile.FechaContratacion,
                "Telefono":user_profile.Telefono,
                "Correo": user_profile.Correo,
                "Rol": {
                    "id": user_profile.Rol.id,
                    "Nombre": user_profile.Rol.Nombre
                }
            }
            return JsonResponse({'user_profile': user_data})
        except Session.DoesNotExist:
            return JsonResponse({'error': 'Sesión no encontrada'}, status=404)
        except Empleado.DoesNotExist:
            return JsonResponse({'error': 'Empleado no encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Cookie de sesión no proporcionada'}, status=400)
    
