from django import forms

class PrendaForm(forms.Form):
    numSerie = forms.CharField(max_length=5, required=True)
    tipoPrenda = forms.CharField(max_length=15, required=True)
    tela = forms.CharField(max_length=15, required=True)
    color = forms.CharField(max_length=10, required=True)
    talla = forms.CharField(max_length=2, required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    stock = forms.IntegerField(required=True)

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    direccion = forms.CharField(max_length=100, required=True)
    correoElectronico = forms.EmailField(max_length=30, required=True)
    numeroTelefono = forms.IntegerField(required=True)

class OrdenForm(forms.Form):
    nombreCliente = forms.CharField(max_length=100, required=True)
    numSerieProd = forms.CharField(max_length=5, required=True)
    direccion = forms.CharField(max_length=100, required=True)
    cantidad = forms.IntegerField(required=True)