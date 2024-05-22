from django.urls import path
import Agenda.views as view

urlpatterns = [
    path('',view.agendaLC,name='list_create'),
    path('<int:pk>/',view.agendaUD,name='update_delete')
]
