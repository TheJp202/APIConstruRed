from django.urls import path
import Empleado.views as view

urlpatterns = [
    path('',view.empleadoL,name='list'),
    path('<int:pk>/',view.empleadoUD,name='update_delete'),
    path('register/',view.register_view,name='register_empleado'),
    path('login/',view.login_view,name='login_empleado'),
    path('logout/',view.logout_view,name='logout_empleado'),
    path('auto_login/',view.user_data_cookie_view,name='auto_login_empleado'),
]
