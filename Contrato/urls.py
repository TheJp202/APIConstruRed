from django.urls import path
import Contrato.views as view

urlpatterns = [
    path('',view.contratoLC,name='list_create'),
    path('<int:pk>/',view.contratoUD,name='update_delete')
]
