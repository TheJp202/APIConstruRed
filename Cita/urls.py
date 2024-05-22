from django.urls import path
import Cita.views as view

urlpatterns = [
    path('',view.citaLC,name='list_create'),
    path('<int:pk>/',view.citaUD,name='update_delete')
]
