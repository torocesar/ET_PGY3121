from django.forms import ModelForm
from .models import Proveedor

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['rut','nombre','telefono','direccion','email','pais','password','moneda']