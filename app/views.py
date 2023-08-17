from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "app/home.html")

def tienda(request):
    contexto = {'productos': Prenda.objects.all() }
    return render(request, "app/tienda.html", contexto)

def clientes(request):
    contexto = {'clientes': Cliente.objects.all() }
    return render(request, "app/clientes.html", contexto)

def nosotros(request):
    return render(request, "app/nosotros.html")

def ordenes(request):
    contexto = {'ordenes': Orden.objects.all() }
    return render(request, "app/ordenes.html", contexto)

def prendaForm(request):
    if request.method == "POST":
        formulario = PrendaForm(request.POST)
        if formulario.is_valid():
            prendaNum = formulario.cleaned_data.get("numSerie")
            prendaTipo = formulario.cleaned_data.get("tipoPrenda")
            prendaTela = formulario.cleaned_data.get("tela")
            prendaColor = formulario.cleaned_data.get("color")
            prendaTalla = formulario.cleaned_data.get("talla")
            prendaPrecio = formulario.cleaned_data.get("precio")
            prendaStock = formulario.cleaned_data.get("stock")
            prenda = Prenda(numSerie=prendaNum,
                            tipoPrenda=prendaTipo,
                            tela=prendaTela,
                            color=prendaColor,
                            talla=prendaTalla,
                            precio=prendaPrecio,
                            stock=prendaStock
                            )
            prenda.save()
            return render(request, "app/home.html")
            
    else:
        formulario = PrendaForm()

    return render(request, "app/prendaForm.html", {"form":formulario})

def clienteForm(request):
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            clienteNombre = formulario.cleaned_data.get("nombre")
            clienteDireccion = formulario.cleaned_data.get("direccion")
            clienteCorreoElectronico = formulario.cleaned_data.get("correoElectronico")
            clienteNumeroTelefono = formulario.cleaned_data.get("numeroTelefono")
            cliente = Cliente(nombre=clienteNombre,
                              direccion=clienteDireccion,
                              correoElectronico=clienteCorreoElectronico,
                              numeroTelefono=clienteNumeroTelefono
                              )
            cliente.save()
            return render(request, "app/home.html")
            
    else:
        formulario = ClienteForm()

    return render(request, "app/clienteForm.html", {"form":formulario})

def ordenForm(request):
    if request.method == "POST":
        formulario = OrdenForm(request.POST)
        if formulario.is_valid():
            ordenNombreCliente = formulario.cleaned_data.get("nombreCliente")
            ordenNumSerieProd = formulario.cleaned_data.get("numSerieProd")
            ordenDireccion = formulario.cleaned_data.get("direccion")
            ordenCantidad = formulario.cleaned_data.get("cantidad")
            orden = Orden(nombreCliente=ordenNombreCliente,
                          numSerieProd=ordenNumSerieProd,
                          direccion=ordenDireccion,
                          cantidad=ordenCantidad
                          )
            orden.save()
            return render(request, "app/home.html")
            
    else:
        formulario = OrdenForm()

    return render(request, "app/ordenForm.html", {"form":formulario})


def buscar(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        tipoPrenda = Prenda.objects.filter(tipoPrenda__icontains=patron)
        contexto = {"productos": tipoPrenda}
        return render(request, "app/tienda.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")