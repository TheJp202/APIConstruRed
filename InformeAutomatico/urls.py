from django.urls import path
import InformeAutomatico.views as view

urlpatterns = [
    path('',view.informeAutomaticoLC,name='list_create'),
    path('<int:pk>/',view.informeAutomaticoUD,name='update_delete')
]
