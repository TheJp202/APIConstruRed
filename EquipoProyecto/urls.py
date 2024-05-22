from django.urls import path
import EquipoProyecto.views as view

urlpatterns = [
    path('',view.equipoProyectoLC,name='list_create'),
    path('<int:pk>/',view.equipoProyectoUD,name='update_delete')
]
