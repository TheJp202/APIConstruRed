from django.urls import path
import AgendaTarea.views as view

urlpatterns = [
    path('',view.agendaTareaLC,name='list_create'),
    path('<int:pk>/',view.agendaTareaUD,name='update_delete')
]
