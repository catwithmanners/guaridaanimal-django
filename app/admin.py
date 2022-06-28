from django.contrib import admin

from app.views import carrito
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','descripcion','precio','stock','tipo', 'imagen']
    search_fields = ['codigo', 'nombre']
    list_per_page = 3

class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ['id_tipo','tipo']
    search_fields = ['id_tipo', 'tipo']
    list_per_page = 3

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['run','dv','nombre','apellido','edad','comuna','region','direccion','correo','telefono','contrasena', 'imagen']
    search_fields =['run']
    list_per_page  = 3

class ItemsCarroAdmin(admin.ModelAdmin):
    list_display = ['id','nombreProducto','precioProducto','imagen']
    search_fields = ['id', 'nombreProducto']
    list_per_page = 3

class HistorialAdmin(admin.ModelAdmin):
    list_display = ['orden','usuario','total','codigo_seg']
    search_fields = ['orden', 'usuario']
    list_per_page = 3

class SeguimientoAdmin(admin.ModelAdmin):
    list_display = ['codigo_seg','estado_seg']
    search_fields = ['codigo_seg', 'estado_seg']
    list_per_page = 3

admin.site.register(TipoProducto,TipoProductoAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(ItemsCarro,ItemsCarroAdmin)
admin.site.register(Historial,HistorialAdmin)
admin.site.register(Seguimiento, SeguimientoAdmin)