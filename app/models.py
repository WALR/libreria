from django.db import models

# Create your models here.
class cliente(models.Model):
	nit = models.CharField("Nit",max_length = 20, primary_key = True)
	nombre = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 70)
	telefono = models.CharField(max_length = 10)
	email = models.EmailField()
	def __unicode__(self):
		return "%s - %s - %s - %s - %s" % (self.nit, self.nombre, self.direccion, self.telefono, self.email) 

class sucursal(models.Model):
	nombre = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 70)
	telefono = models.CharField(max_length = 10)
	email = models.EmailField()
	def __unicode__(self):
		return "%s - %s - %s - %s" % (self.nombre, self.direccion, self.telefono, self.email)

class producto(models.Model):
	codigo = models.CharField("Codigo",max_length = 20, primary_key = True)
	nombre = models.CharField(max_length = 50)
	descripcion = models.CharField(max_length = 80)
	cantidad = models.PositiveIntegerField()
	precio_c = models.FloatField()
	precio_v = models.FloatField()
	sucursal = models.ForeignKey(sucursal)
	def __unicode__(self):
		return "%s - %s - %s - %s - %s - %s - %s" % (self.codigo, self.nombre, self.descripcion, self.cantidad, self.precio_c, self.precio_v, self.sucursal) 

class proveedor(models.Model):
	nit = models.CharField("Nit",max_length = 20, primary_key = True)
	nombre = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 70)
	telefono = models.CharField(max_length = 10)
	email = models.EmailField()
	def __unicode__(self):
		return "%s - %s - %s - %s - %s" % (self.nit, self.nombre, self.direccion, self.telefono, self.email)

class empleado(models.Model):
	nombre = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 70)
	dpi = models.BigIntegerField()
	telefono = models.CharField(max_length = 10)
	email = models.EmailField()
	salario = models.FloatField()
	sucursal = models.ForeignKey(sucursal)
	def __unicode__(self):
		return "%s - %s - %s - %s - %s - %s - %s" % (self.nombre, self.direccion, self.dpi, self.telefono, self.email, self.salario, self.sucursal)

class venta(models.Model):
	fecha = models.DateField()
	descripcion = models.CharField(max_length = 100)
	def __unicode__(self):
		return "%s - %s" % (self.fecha, self.descripcion)