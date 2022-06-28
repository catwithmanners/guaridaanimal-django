from django.urls import path
from unicodedata import name
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('IndexLogin/', indexLogin, name='indexLogin'),
    path('Login/', login, name='login'),
    path('CategoriaPerro/', catPerro, name='perrito'),
    path('CategoriaPerroLogeado/', catPerroLogin, name='perritoLog'),
    path('CategoriaGato/', catGato, name='gatito'),
    path('CategoriaGatoLogeado/', catGatoLogin, name='gatitoLog'),
    path('CategoriaAccesorio/', catAcc, name='accesorio'),
    path('CategoriaAccesorioLogeado/', catAccLogin, name='accesorioLog'),
    path('Perfil/', perfil, name='perfil'),
    path('PerfilEdit/', perfilEdit, name='perfilEdit'),
    path('PerfilHisto/', perfilHistorial, name='perfilHistorial'),
    path('PerfilSegui/<orden>', perfilSegui, name='perfilSegui'),
    path('ListadoProductos/', listarProducto, name='listarProd'),
    path('ModificarProductos/<codigo>', modificarProducto, name='modProd'),
    path('EliminarProductos/<codigo>', eliminarProducto, name='eliminarProd'),
    path('AgregarProductos/', agregarProducto, name='agregarProd'),
    path('Registrar/', registro_usuario, name='registro'),
    path('ListaUsuarios/', listarUsuarios, name='listarUsuario'),
    path('EliminarUsuario/<run>', eliminarUsuario, name='eliminarUsuario'),
    path('ModificarUsuario/<run>', modUsuarios, name='modificarUsuario'),
    path('Pagar/', pagar, name='pagar'),
    path('PagoExitoso/', pago, name='pago'),
    path('Carrito/', carrito, name='carrito'),
    path('QuitarCarrito/<id>', quitar, name='quitarCarrito'),
    path('registro_usuario/', registro_usuario, name='registro_usuario'),
    path('prueba/', prueba, name='prueba'),
    path('ProductosApi/', productosApi, name='productosApi'),
    path('UniversoApi/', universoApi, name='universoApi'),
    path('Suscripcion/', suscripcion, name='suscripcion'),

]