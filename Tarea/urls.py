from django.urls import path
import Tarea.views as view

urlpatterns = [
    path('',view.tareaLC,name='list_create'),
    path('<int:pk>/',view.tareaUD,name='update_delete')
]
