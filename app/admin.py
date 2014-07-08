from django.contrib import admin
from models import *
# Register your models here.

class clienteAdmin(admin.ModelAdmin):
	list_display = ('nit', 'nombre', 'direccion', 'telefono', 'email')
	list_filter = ('nit', 'direccion')
	search_fields = ('nombre__direccion',)

class sucursalAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'direccion', 'telefono', 'email')

class ProductoInline(admin.StackedInline):
    model = producto
    extra = 3

class productoAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'nombre', 'descripcion', 'cantidad', 'precio_c', 'precio_v', 'sucursal')
	#inlines = [ProductoInline]

class proveedorAdmin(admin.ModelAdmin):
	list_display = ('nit', 'nombre', 'direccion', 'telefono', 'email',)

class empleadoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'direccion', 'dpi', 'telefono','email', 'salario', 'sucursal')

class facturaAdmin(admin.ModelAdmin):
	list_display = ('factura', 'fecha', 'cliente',)

admin.site.register(cliente, clienteAdmin)
admin.site.register(sucursal, sucursalAdmin)
admin.site.register(producto, productoAdmin)
admin.site.register(proveedor, proveedorAdmin)
admin.site.register(empleado, empleadoAdmin)
admin.site.register(rol)
admin.site.register(factura, facturaAdmin)
admin.site.register(detalle_factura)

