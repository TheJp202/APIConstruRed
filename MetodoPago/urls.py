from django.urls import path
import MetodoPago.views as view

urlpatterns = [
    path('',view.metodoPagoLC,name='list_create'),
    path('<int:pk>/',view.metodoPagoUD,name='update_delete')
]
