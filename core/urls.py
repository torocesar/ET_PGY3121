from django.urls import path
from .views import index, contacto, proveedores, form_proveedores, form_proveedores_mod, form_proveedores_del

urlpatterns =[

    path('', index, name="index"),
    path('contacto',contacto,name='contacto'),
    path('proveedores',proveedores,name="proveedores"),
    path('form-proveedores',form_proveedores,name="form_proveedores"),
    path('form-proveedores-mod/<id>',form_proveedores_mod,name="form_proveedores_mod"),
    path('form-proveedores-del/<id>',form_proveedores_del,name='form_proveedores_del'),
]