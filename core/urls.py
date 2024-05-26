
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/',include('Cliente.urls')),
    path('metodoPago/',include('MetodoPago.urls')),
    path('reunion/',include('Reunion.urls')),
    path('rol/',include('Rol.urls')),
    path('tarea/',include('Tarea.urls')),
    path('tipoInforme/',include('TipoInforme.urls')),
    path('tipoMensaje/',include('TipoMensaje.urls')),
    path('empleado/',include('Empleado.urls')),
    path('cita/',include('Cita.urls')),
    path('mensaje/',include('Mensaje.urls')),
    path('agenda/',include('Agenda.urls')),
    path('proyecto/',include('Proyecto.urls')),
    path('agendaTarea/',include('AgendaTarea.urls')),
    path('proyectoTarea/',include('ProyectoTarea.urls')),
    path('contrato/',include('Contrato.urls')),
    path('archivo/',include('Archivo.urls')),
    path('informeAutomatico/',include('InformeAutomatico.urls')),
    path('factura/',include('Factura.urls')),
    path('equipo/',include('Equipo.urls')),
    path('equipoEmpleado/',include('EquipoEmpleado.urls')),
    path('equipoProyecto/',include('EquipoProyecto.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
