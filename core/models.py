from django.db import models

# Create your models here.

#Modelo para el Pais

class Pais(models.Model):
    idPais= models.IntegerField(primary_key=True, verbose_name='Id Pais')
    nombrePais =models.CharField(max_length=50, verbose_name='Pais')

    def __str__(self):
        return self.nombrePais

#Modelo para la Moneda        

class Moneda(models.Model):
    idMoneda= models.IntegerField(primary_key=True, verbose_name='Id Moneda')
    nombreMoneda =models.CharField(max_length=50, verbose_name='Moneda')

    def __str__(self):
        return self.nombreMoneda

#Modelo para el Proveedor

class Proveedor(models.Model):
    rut     	= models.CharField(max_length=10, primary_key=True, verbose_name='Numero identificacion')
    logo        = models.ImageField(upload_to="proveedores",null=True)
    nombre      = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre Completo')
    telefono    = models.CharField(max_length=50, null=False, blank=False, verbose_name='Telefono')
    direccion   = models.CharField(max_length=250,null=False, blank=False, verbose_name='Direccion')
    email       = models.EmailField(max_length=50,null=False, blank=False, verbose_name='Email')
    pais   	    = models.ForeignKey(Pais, on_delete=models.CASCADE)
    password    = models.CharField(max_length=50,null=False, blank=True, verbose_name='Password')
    moneda   	= models.ForeignKey(Moneda,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.rut