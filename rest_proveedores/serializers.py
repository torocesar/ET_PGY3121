from core.models import Proveedor
from rest_framework import serializers

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields ='__all__'
    #    fields = ['rut','nombre','telefono','direccion','email','pais','password','moneda','logo']


