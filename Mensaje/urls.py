from django.urls import path
import Mensaje.views as view

urlpatterns = [
    path('',view.mensajeLC,name='list_create'),
    path('<int:pk>/',view.mensajeUD,name='update_delete')
]
