from urllib import response
import requests

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'app/home.html')

def registro_usuario(request):
    datos = {
        'form' : RegistroUsuarioForm()
    }
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            #login(request,user)
            suscripcion = Suscripcion()
            suscripcion.username_sus = request.POST.get('username')
            suscripcion.estado_sus = "No suscrito"
            messages.success(request,'¡Usuario registrado correctamente!')
        datos["form"] = formulario
    return render(request, 'registration/registro.html',datos)

def suscripcion(request):
    suscripcion = Suscripcion.objects.all()
    datos = {
        'suscripcion' : suscripcion
    }

    if request.method =='POST':
        nuevo = Suscripcion()
        nuevo.nombre = request.POST.get('username')
        nuevo.estado = request.POST.get('boolean')
        nuevo.save()
    return render(request, 'app/suscripcion.html', datos)

@login_required
def indexLogin(request):
    return render(request, 'app/homeLogin.html')

def login(request):
    return render(request, 'app/login.html')

def categorias(request):
    return render(request, 'app/baseCategorias.html')

@login_required
def perfil(request):
    usuario = Usuario.objects.all()
    datos = {
        'usuario' : usuario
    }

    return render(request, 'app/perfilUsuario.html', datos)

@login_required
def perfilEdit(request):
    return render(request, 'app/perfilUsuarioEditar.html')

@login_required
def perfilHistorial(request):
    historial = Historial.objects.all()
    seguimiento = Seguimiento.objects.all()
    usuario = Usuario.objects.all()
    datos = {
        'historial' : historial,
        'seguimiento' : seguimiento,
        'usuario' : usuario
    }

    return render(request, 'app/historialCompra.html', datos)

@login_required
def perfilSegui(request, orden):
    historial = Historial.objects.get(orden=orden)
    seguimiento = Seguimiento.objects.all()

    datos = {
        'historial' : historial,
        'seguimiento' : seguimiento
    }

    return render(request, 'app/seguimiento.html', datos)

def catPerro(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    return render(request, 'app/catPerro.html', datos)

@login_required
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

@login_required
def productosApi(request):
    response = requests.get('http://127.0.0.1:8000/api/producto/').json()
    datos = {
        'listaApi' : response
    }

    if request.method == 'POST':
        carrito = ItemsCarro()
        carrito.codigoProducto = request.POST.get('codigo')
        carrito.nombreProducto = request.POST.get('nombre')
        carrito.precioProducto = request.POST.get('precio')
        carrito.imagen = request.POST.get('imagen')
        carrito.save()

    return render(request, 'app/productosApi.html', datos)

@login_required
def universoApi(request):
    response = requests.get('https://ghibliapi.herokuapp.com/films/').json()
    datos = {
        'listaUniApi' : response
    }

    if request.method == 'POST':
        carrito = ItemsCarro()
        carrito.codigoProducto = request.POST.get('codigo')
        carrito.nombreProducto = request.POST.get('nombre')
        carrito.precioProducto = request.POST.get('precio')
        carrito.imagen = request.POST.get('imagen')
        carrito.save()

    return render(request, 'app/universoApi.html', datos)

def catGato(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    return render(request, 'app/catGato.html', datos)

@login_required
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

@login_required
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
@permission_required('app.add_producto')
def agregarProducto(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')

    return render(request, 'app/productos/agregar_producto.html', datos)

#SECCION LISTAR
@permission_required('app.view_producto')
def listarProducto(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    return render(request, 'app/productos/listar_producto.html', datos)

#SECCION MODIFICAR
@permission_required('app.change_producto')
def modificarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')
            datos['form'] = formulario

    return render(request, 'app/productos/modificar_producto.html', datos)

#SECCION ELIMINAR
@permission_required('app.delete_producto')
def eliminarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listarProd")

#SECCION USUARIOS
@permission_required('app.add_producto')
def agregarUsuario(request):
    usuarios = {

        'form' : UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            usuarios['mensaje'] = "Usuario registrado correctamente!"

    return render (request,'app/user.html', usuarios)

def suscripcion(request):
    usuario = Suscripcion.objects.all()
    datos = {
        'usuario' : usuario
    }
    if request.method == 'POST':
        usuarios = Suscripcion()
        usuarios.nombre = request.POST.get('username')
        usuarios.estado = request.POST.get('boolean')
        usuarios.save()
    return render (request, '', datos)

@permission_required('app.view_producto')
def listarUsuarios(request):
    usuariosAll = Usuario.objects.all()
    datos = {
        'listaUsuarios' : usuariosAll
    }
    return render (request, 'app/listarUsuarios.html', datos)

@permission_required('app.change_producto')
def modUsuarios(request, run):
    usuariosAll = Usuario.objects.get(run=run)
    datos = {
        'form' : UsuarioForm(instance=usuariosAll)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES, instance=usuariosAll)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = '¡Usuario modificado correctamente!'
            datos['form'] = formulario
    return render(request, 'app/modificarUser.html', datos)

@permission_required('app.delete_producto')
def eliminarUsuario(request, run):
    usuario = Usuario.objects.get(run=run)
    usuario.delete()

    return redirect(to="listarUsuario")
#CARRITO
def carrito(request):
    carrito = ItemsCarro.objects.all()
    total = 0 
    totalDesc= 0
    desc=0

    for aux in carrito:
        total += aux.precioProducto 
        totalDesc += round(aux.precioProducto * 0.95)
        desc += aux.precioProducto-round(aux.precioProducto*0.95)

    datos = { 'listaCarrito' : carrito,
                'total' : total,
                'totalDesc' : totalDesc,
                'desc' : desc
    }

    if request.method == 'POST':
        carrito = ItemsCarro()
        carrito.id = request.POST.get('id')
        carrito.delete()

    return render (request, 'app/carrito.html', datos)

def pago(request):
    carrito = ItemsCarro.objects.all()
    historial2 = Historial.objects.all()
    seguimiento = Seguimiento.objects.all()
    total = 0 
    totalDesc= 0
    desc = 0
    norden = 1

    for aux in carrito:
        total += aux.precioProducto 
        totalDesc += round(aux.precioProducto * 0.95)
        desc += aux.precioProducto-round(aux.precioProducto*0.95)

    datos = {
        carrito : 'carrito',
        historial2 : 'historial',
        seguimiento : 'seguimiento'
    }
    for aux2 in historial2:
        norden += 1

    if totalDesc > 0:
        historial = Historial()
        historial.orden = norden
        historial.usuario = request.user.get_username()
        historial.total = totalDesc
        historial.codigo_seg = seguimiento.get(Q(codigo_seg=1))
        historial.save() 
        carrito.delete()
        return render (request, 'app/pagado.html', datos)
    
    return redirect(to="carrito")

def quitar(request, id):
    carrito = ItemsCarro.objects.get(id=id)
    carrito.delete()

    return redirect(to="carrito")

@login_required
def pagar(request):
    return render(request, 'app/pagar.html')

def total(request):
    carrito = ItemsCarro.objects.all()
    datos = { 'listaCarrito' : carrito}

@login_required
def prueba(request):
    return render(request, 'app/prueba.html')
    