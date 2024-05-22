from django.urls import path
import Proyecto.views as view

urlpatterns = [
    path('',view.proyectoLC,name='list_create'),
    path('<int:pk>/',view.proyectoUD,name='update_delete')
]
