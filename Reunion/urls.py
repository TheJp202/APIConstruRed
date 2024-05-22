from django.urls import path
import Reunion.views as view

urlpatterns = [
    path('',view.reunionLC,name='list_create'),
    path('<int:pk>/',view.reunionUD,name='update_delete')
]
