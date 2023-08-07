from django.contrib import admin

# Register your models here.
from gestionTienda.models import Tienda, Producto

admin.site.register(Tienda)
admin.site.register(Producto)
