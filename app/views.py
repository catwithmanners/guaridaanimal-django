from django.shortcuts import render, redirect

from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'app/home.html')

def indexLogin(request):
    return render(request, 'app/homeLogin.html')

def login(request):
    return render(request, 'app/login.html')

def categorias(request):
    return render(request, 'app/baseCategorias.html')

def perfil(request):
    return render(request, 'app/perfilUsuario.html')

def perfilEdit(request):
    return render(request, 'app/perfilUsuarioEditar.html')

def perfilHistorial(request):
    return render(request, 'app/historialCompra.html')

def perfilSegui(request):
    return render(request, 'app/seguimiento.html')

def catPerro(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    return render(request, 'app/catPerro.html', datos)

def catPerroLogin(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    if request.method == 'POST':

        carrito = ItemsCarro()
        carrito.codigoProducto = request.POST.get('codigo')
        carrito.nombreProducto = request.POST.get('nombre')
        carrito.precioProducto = request.POST.get('precio')
        carrito.imagen = request.POST.get('imagen')
        carrito.save()
        
    return render(request, 'app/catPerroLogin.html', datos)

def catGato(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    return render(request, 'app/catGato.html', datos)

def catGatoLogin(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    if request.method == 'POST':

        carrito = ItemsCarro()
        carrito.codigoProducto = request.POST.get('codigo')
        carrito.nombreProducto = request.POST.get('nombre')
        carrito.precioProducto = request.POST.get('precio')
        carrito.imagen = request.POST.get('imagen')
        carrito.save()
        
    return render(request, 'app/catGatoLogin.html', datos)

def catAcc(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    return render(request, 'app/catAccesorios.html', datos)

def catAccLogin(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    if request.method == 'POST':

        carrito = ItemsCarro()
        carrito.codigoProducto = request.POST.get('codigo')
        carrito.nombreProducto = request.POST.get('nombre')
        carrito.precioProducto = request.POST.get('precio')
        carrito.imagen = request.POST.get('imagen')
        carrito.save()
        
    return render(request, 'app/catAccesoriosLogin.html', datos)

#SECCION AGREGAR
def agregarProducto(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto guardado correctamente'

    return render(request, 'app/productos/agregar_producto.html', datos)

#SECCION LISTAR
def listarProducto(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    return render(request, 'app/productos/listar_producto.html', datos)

#SECCION MODIFICAR
def modificarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto modificado correctamente!'
            datos['form'] = formulario

    return render(request, 'app/productos/modificar_producto.html', datos)

#SECCION ELIMINAR
def eliminarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listarProd")
#SECCION USUARIOS
def agregarUsuario(request):
    usuarios = {

        'form' : UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuarios['mensaje'] = "Usuario registrado correctamente!"

    return render (request,'app/user.html', usuarios)

def listarUsuarios(request):
    usuariosAll = Usuario.objects.all()
    datos = {
        'listaUsuarios' : usuariosAll
    }
    return render (request, 'app/listarUsuarios.html', datos)

def modUsuarios(request, run):
    usuariosAll = Usuario.objects.get(run=run)
    datos = {
        'form' : UsuarioForm(instance=usuariosAll)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES, instance=usuariosAll)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Usuario modificado correctamente!'
            datos['form'] = formulario
    return render(request, 'app/', datos)

def eliminarUsuario(request, run):
    usuario = Usuario.objects.get(run=run)
    usuario.delete()

    return redirect(to="listarUsuario")
#CARRITO
def carrito(request):
    carrito = ItemsCarro.objects.all()
    datos = { 'listaCarrito' : carrito}

    if request.method == 'POST':
        carrito = ItemsCarro()
        carrito.id = request.POST.get('id')
        carrito.delete()

    return render (request, 'app/carrito.html', datos)

def pago(request):
    carrito = ItemsCarro.objects.all()
    carrito.delete()

    return render (request, 'app/pagado.html')

def quitar(request, id):
    carrito = ItemsCarro.objects.get(id=id)
    carrito.delete()

    return redirect(to="carrito")

def pagar(request):
    return render(request, 'app/pagar.html')

def total(request):
    carrito = ItemsCarro.objects.all()
    datos = { 'listaCarrito' : carrito}
    