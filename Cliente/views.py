from django.http import JsonResponse
from rest_framework.response import Response
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def clienteL(request):
    if request.method == 'GET':
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def clienteUD(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = ClienteSerializer(cliente, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status=204)


@api_view(['POST'])
def login_view(request):
    email = request.data.get('Correo') 
    raw_password = request.data.get('Contraseña')
    user_profile = Cliente.objects.filter(Correo=email).first()    
    if user_profile is None:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)

    if check_password(raw_password, user_profile.Contraseña):
        request.session['user_id'] = user_profile.id
        user_data = {
            "id": user_profile.id,
            "Nombres": user_profile.Nombres,
            "Apellidos": user_profile.Apellidos,
            "DNI":user_profile.DNI,
            "Telefono":user_profile.Telefono,
            "Correo": user_profile.Correo
        }
        response_data = {"message": "Inicio de sesión exitoso", "user_profile": user_data}
        response = JsonResponse(response_data)
        response.set_cookie(key='sessionid', value=request.session.session_key, samesite='None')
        return response
    else:
        return JsonResponse({"error": "Credenciales inválidas"}, status=400)
    
    
@api_view(['POST'])
def register_view(request):
    nombres = request.data.get('Nombres')
    apellidos = request.data.get('Apellidos')
    dni = request.data.get('DNI')
    telefono = request.data.get('Telefono')
    email = request.data.get('Correo')
    raw_password = request.data.get('Contraseña')
    hashed_password = make_password(raw_password)
    
    if not all([nombres,apellidos,dni,telefono, email, hashed_password]):
        return JsonResponse({'error': 'Se requieren todos los campos'}, status=400)
    if Cliente.objects.filter(Correo=email).exists():
        return JsonResponse({'error': 'El email ya está en uso'}, status=400)
    user = Cliente.objects.create(
    Nombres=nombres,
    Apellidos=apellidos,
    DNI = dni,
    Telefono = telefono,
    Correo=email,
    Contraseña=hashed_password)
    
    if user:
        return JsonResponse({'message':'Usuario registrado exitosamente'}, status=201)
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
            user_profile = Cliente.objects.get(id=user_id)
            user_data = {
                "id": user_profile.id,
                "Nombres": user_profile.Nombres,
                "Apellidos": user_profile.Apellidos,
                "DNI":user_profile.DNI,
                "Telefono":user_profile.Telefono,
                "Correo": user_profile.Correo
            }
            return JsonResponse({'user_profile': user_data})
        except Session.DoesNotExist:
            return JsonResponse({'error': 'Sesión no encontrada'}, status=404)
        except Cliente.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Cookie de sesión no proporcionada'}, status=400)
    
