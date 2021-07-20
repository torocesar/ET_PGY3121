from django.urls import path
from rest_proveedores.views import proveedores_lista, proveedores_detalle

urlpatterns =[

    path('proveedores_lista', proveedores_lista, name="proveedores_lista"),
    path('proveedores_detalle/<id>', proveedores_detalle, name="proveedores_detalle"),

]