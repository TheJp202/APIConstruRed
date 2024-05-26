from django.urls import path
import Cliente.views as view

urlpatterns = [
    path('',view.clienteL,name='list'),
    path('<int:pk>/',view.clienteUD,name='update_delete'),
    path('register/',view.register_view,name='register_cliente'),
    path('login/',view.login_view,name='login_cliente'),
    path('logout/',view.logout_view,name='logout_cliente'),
    path('auto_login/',view.user_data_cookie_view,name='auto_login_cliente')
]
