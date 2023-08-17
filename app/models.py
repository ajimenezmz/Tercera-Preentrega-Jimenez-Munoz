from django.db import models

# Create your models here.
class Prenda(models.Model):
    numSerie = models.CharField(max_length=5)
    tipoPrenda = models.CharField(max_length=15)
    tela = models.CharField(max_length=15)
    color = models.CharField(max_length=10)
    talla = models.CharField(max_length=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    correoElectronico = models.EmailField(max_length=30)
    numeroTelefono = models.IntegerField()
    
class Orden(models.Model):
    nombreCliente = models.CharField(max_length=100)
    numSerieProd = models.CharField(max_length=5)
    direccion = models.CharField(max_length=100)
    cantidad = models.IntegerField()