from django.urls import path
import TipoMensaje.views as view

urlpatterns = [
    path('',view.tipoMensajeLC,name='list_create'),
    path('<int:pk>/',view.tipoMensajeUD,name='update_delete')
]
