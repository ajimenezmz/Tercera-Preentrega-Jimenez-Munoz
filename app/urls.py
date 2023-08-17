from django.urls import path, include
from .views import *                #Para importar todo de views en la misma carpeta

urlpatterns = [
    path('',home, name="home"),
    path('tienda/',tienda, name="tienda"),
    path('clientes/',clientes, name="clientes"),
    path('sobre_nosotros/',nosotros, name="nosotros"),
    path('ordenes/',ordenes, name="ordenes"),
    path('prenda_form/',prendaForm, name="prendaForm"),
    path('orden_form/',ordenForm, name="ordenForm"),
    path('user_form/',clienteForm, name="clienteForm"),
    path('buscar/', buscar, name="buscar" ),
]