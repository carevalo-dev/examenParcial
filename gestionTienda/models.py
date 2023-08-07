from django.db import models
# Create your models here.

class Tienda(models.Model):
    direccion = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    fechaCreacion = models.DateField( auto_now=True)
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.direccion} - {self.provincia} - {self.region} - {self.fechaCreacion} - {self.telefono}"
    

class Producto(models.Model):
    descripcion = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    precioVenta = models.FloatField()
    cantidad = models.IntegerField()
    tienda = models.ForeignKey(Tienda, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.descripcion} - {self.codigo} - {self.precioVenta} - {self.cantidad} - {self.tienda}"