from django.urls import path
import TipoInforme.views as view

urlpatterns = [
    path('',view.tipoInformeLC,name='list_create'),
    path('<int:pk>/',view.tipoInformeUD,name='update_delete')
]
