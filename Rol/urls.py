from django.urls import path
import Rol.views as view

urlpatterns = [
    path('',view.rolLC,name='list_create'),
    path('<int:pk>/',view.rolUD,name='update_delete')
]
