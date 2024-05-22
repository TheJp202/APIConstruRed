from django.urls import path
import EquipoEmpleado.views as view

urlpatterns = [
    path('',view.equipoEmpleadoLC,name='list_create'),
    path('<int:pk>/',view.equipoEmpleadoUD,name='update_delete')
]
