from django.urls import path
import ProyectoTarea.views as view

urlpatterns = [
    path('',view.proyectoTareaLC,name='list_create'),
    path('<int:pk>/',view.proyectoTareaUD,name='update_delete')
]
