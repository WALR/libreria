from django.db import models

# Create your models here.
class cliente(models.Model):
	nit = models.ForeingKey(nit)
	nombre = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 70)
	telefono = models.CharField(max_length = 10)
	email = models.EmailField()


class producto(models.Model):
	codigo = models.ForeingKey(codigo)
	nombre = models.CharField(max_length = 50)
	descripcion = models.CharField(max_length = 80)
	cantidad = models.PositiveIntegerField()
	precio_c = models.FloatField(max_digits=20,decimal_places=2)
	precio_v = models.FloatField(max_digits=20,decimal_places=2)

class proveedor(models.Model):
	nit = models.ForeingKey(nit)
	nombre = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 70)
	telefono = models.CharField(max_length = 10)
	email = models.EmailField()

class sucursal(models.Model):
	nombre = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 70)
	telefono = models.CharField(max_length = 10)
	email = models.EmailField()

class empleado(models.Model):
	nombre = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 70)
	dpi = models.IntegerField()
	telefono = models.CharField(max_length = 10)
	email = models.EmailField()
	salario = models.FloatField(max_digits=20,decimal_places=2)

class venta(models.Model):
	fecha = models.DateField()
	descripcion = models.CharField(max_length = 100)




	titulo = models.CharField(max_length = 100)