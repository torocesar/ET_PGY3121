from django.shortcuts import redirect, render
from .models import Proveedor
from .forms import ProveedorForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'core\index.html')
def contacto(request):
    return render(request,'core\contacto.html')    

def proveedores(request):
    
    proveedor = Proveedor.objects.all()

    datos ={

        'proveedor' : proveedor
    }

    return render(request,'core\proveedores.html', datos)

def form_proveedores(request):

    datos ={

        'forms' : ProveedorForm()
    }

    if request.method == 'POST':

        formulario=ProveedorForm(request.POST)

        if formulario.is_valid():

            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="proveedores")

            #datos ['mensaje'] = "Guardado Correctamente"
            
    return render(request, 'core/form_proveedores.html', datos)


def form_proveedores_mod(request, id):

    proveedor = Proveedor.objects.get(rut=id)

    datos ={
        'forms' : ProveedorForm(instance=proveedor)
    }

    if request.method == 'POST':

        formulario = ProveedorForm(data=request.POST, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="proveedores")

        #datos['mensaje'] = "Registro Modificado Correctamente"

    return render(request, 'core/form_proveedores_mod.html', datos)


def form_proveedores_del(request, id):

    proveedor = Proveedor.objects.get(rut =id)

    proveedor.delete()

    return redirect(to="proveedores")
        

