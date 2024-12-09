from django.urls import path

from app_tienda.views import *

 
urlpatterns = [
    path("", inicio, name="inicio"),
    path('cliente/', cliente, name="cliente"),
    path('categoria/', categoria, name="categoria"),
    path('producto/', producto ,name="prodcuto"),
   

    path('buscar-producto/', buscar_producto, name='buscar_producto'),
    path('buscar-categoria/', buscar_categoria, name='buscar_categoria'),
    path('registro/', registro_cliente, name='registro'),
    path('login/', login_cliente, name='login'),
    path('logout/', logout_cliente, name='logout'),
     
] 

