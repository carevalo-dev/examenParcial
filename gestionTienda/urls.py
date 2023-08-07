from django.urls import path
from gestionTienda.views import (
    gestionTienda_view,
    productos_view,
    tiendas_view,
    tienda_detalle_view,
    producto_save,
    producto_delete,
    producto_edit,
    tienda_save,
    tienda_edit,
    tienda_delete,
)

urlpatterns = [
    path('', gestionTienda_view, name='index'),
    path('productos', productos_view, name='productos'),
    path('tiendas', tiendas_view, name='tiendas'),
    path('productos/save', producto_save, name='producto_save'),
    path('productos/delete/<int:producto_id>/', producto_delete, name='producto_delete'),
    path('productos/<int:producto_id>/', producto_edit, name='producto_edit'),
    path('tiendas/save', tienda_save, name='tienda_save'),
    path('tiendas/edit/<int:tienda_id>/', tienda_edit, name='tienda_edit'),
    path('tiendas/delete/<int:tienda_id>/', tienda_delete, name='tienda_delete'),
    path('tiendas/<int:tienda_id>/', tienda_detalle_view, name='tienda_detalle'),

]
    