from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Proveedor, Pais
from .serializers import ProveedorSerializer
from django.contrib import messages


# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])

def proveedores_lista(request):
    """
    Lista Todos los Proveedores
    """
    if request.method=='GET':

        proveedor = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedor, many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':

        data =JSONParser().parse(request)
        serializer = ProveedorSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def proveedores_detalle(request, id):
    
    try:
        proveedor = Proveedor.objects.get(rut = id)
    except Proveedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer = ProveedorSerializer(proveedor)
        return Response(serializer.data)
    
    if request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = ProveedorSerializer(proveedor, data=data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Modificado Correctamente")
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        











