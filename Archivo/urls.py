from django.urls import path
import Archivo.views as view

urlpatterns = [
    path('',view.archivoLC,name='list_create'),
    path('<int:pk>/',view.archivoUD,name='update_delete')
]
