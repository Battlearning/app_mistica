from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout
from .models import Producto


def inicio(request):
      return render(request, "app_tienda/index.html")



def cliente (request):
    query = request.GET.get('q')
    if query:
        cliente = Cliente.objects.filter(nombre__icontains=query)
    else:
        cliente= Cliente.objects.all()
    return render(request, "app_mistica/cliente.html", {"cliente": cliente, "query": query})



def categoria (request):
    query = request.GET.get('q')
    if query:
        categoria = Categoria.objects.filter(nombre__icontains=query)
    else:
        categoria= Categoria.objects.all()
    return render(request, "app_mistica/categoria.html", {"categoria": categoria, "query": query})




def producto (request):
    query = request.GET.get('q')
    if query:
        producto = Producto.objects.filter(nombre__icontains=query)
    else:
         producto = Producto.objects.all()
    return render(request, "app_mistica/producto.html", {"producto": producto, "query": query})



def registro_cliente(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Cliente.objects.create(user=user, telefono=request.POST.get('telefono'))
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})



def login_cliente(request):
    if request.method == 'POST':
        form = Inicio_Sesion_Form(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = Inicio_Sesion_Form()
    return render(request, 'login.html', {'form': form})



def logout_cliente(request):
    logout(request)
    return redirect('home')


def buscar_producto(request):
    form = Buscar_Producto_Form(request.GET)
    productos = None
    if form.is_valid():
        productos = Producto.objects.filter(nombre__icontains=form.cleaned_data['nombre'])
    return render(request, 'buscar_producto.html', {'form': form, 'productos': productos})

def buscar_categoria(request):
    form = Buscar_Categoria_Form(request.GET)
    categorias = None
    if form.is_valid():
        categorias = Categoria.objects.filter(nombre__icontains=form.cleaned_data['nombre'])
    return render(request, 'buscar_categoria.html', {'form': form, 'categorias': categorias})