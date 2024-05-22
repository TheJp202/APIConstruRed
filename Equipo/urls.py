from django.urls import path
import Equipo.views as view

urlpatterns = [
    path('',view.equipoLC,name='list_create'),
    path('<int:pk>/',view.equipoUD,name='update_delete')
]
