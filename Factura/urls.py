from django.urls import path
import Factura.views as view

urlpatterns = [
    path('',view.facturaLC,name='list_create'),
    path('<int:pk>/',view.facturaUD,name='update_delete')
]
