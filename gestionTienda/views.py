from django.shortcuts import render
from gestionTienda.models import Producto , Tienda
#datetime import datetime

# Create your views here.}

def gestionTienda_view(request):
    return render(request, 'index.html')

def productos_view(request):
    # Aquí puedes obtener la lista de productos desde la base de datos
    # y pasarla al template para mostrarla
    productos = Producto.objects.all()
    tiendas = Tienda.objects.all()
    #producto.html esta en la carpeta templates
    return render(request, 'productos.html', {'productos': productos, 'tiendas': tiendas})

def producto_save(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        codigo = request.POST.get('codigo')
        precioVenta = request.POST.get('precioVenta')
        cantidad = request.POST.get('cantidad')
        tienda = request.POST.get('tienda')
        producto = Producto(descripcion=descripcion, codigo=codigo, precioVenta=precioVenta, cantidad=cantidad, tienda_id=tienda)
        producto.save()
        return productos_view(request)
    else:
        return productos_view(request)

def producto_edit(request, producto_id):
    if  request.method == 'POST':
        producto = Producto.objects.get(id=producto_id)
        producto.descripcion = request.POST.get('descripcion_edit')
        producto.codigo = request.POST.get('codigo_edit')
        producto.precioVenta = request.POST.get('precioVenta_edit')
        producto.cantidad = request.POST.get('cantidad_edit')
        producto.tienda_id = request.POST.get('tienda_edit')
        producto.save()
        return productos_view(request) 

def producto_delete(request, producto_id):
    if request.method == 'DELETE':
        producto = Producto.objects.get(id=producto_id)
        producto.delete()
        return productos_view(request)
    
def tiendas_view(request):
    # Aquí puedes obtener la lista de tiendas desde la base de datos
    # y pasarla al template para mostrarla
    tiendas = Tienda.objects.all()
    return render(request, 'tiendas.html', {'tiendas': tiendas})

def tienda_save(request):
    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        provincia = request.POST.get('provincia')
        region = request.POST.get('region')
        telefono = request.POST.get('telefono')
        tienda = Tienda(direccion=direccion, provincia=provincia, region=region,  telefono=telefono)
        tienda.save()
        tiendas = Tienda.objects.all()
        return render(request, 'tiendas.html', {'tiendas': tiendas})
    else:
        return render(request, 'tiendas.html', {'tiendas': tiendas})

def tienda_edit(request, tienda_id):
    if  request.method == 'POST':
        tienda = Tienda.objects.get(id=tienda_id)
        tienda.direccion = request.POST.get('direccion_edit')
        tienda.provincia = request.POST.get('provincia_edit')
        tienda.region = request.POST.get('region_edit')
        tienda.telefono = request.POST.get('telefono_edit')
        tienda.save()
        return tiendas_view(request)
    
def tienda_delete(request, tienda_id):
    if request.method == 'DELETE':
        tienda = Tienda.objects.get(id=tienda_id)
        tienda.delete()
        return tiendas_view(request)

def tienda_detalle_view(request, tienda_id):
    tienda = Tienda.objects.get(id=tienda_id)
    productos = Producto.objects.filter(tienda_id=tienda_id)
    return render(request, 'tiendaDetalles.html', {'tienda': tienda, 'productos': productos})