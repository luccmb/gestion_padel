from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db.models import Sum
from datetime import date, timedelta
from .models import Reserva, Bebida, Stock
from .forms import RegistroUsuarioForm, ReservaForm, BebidaForm, Stock
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'cancha/dashboard.html')

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('dashboard')  # Redirige al dashboard después de registrarse
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'cancha/registro.html', {'form': form})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirigir al dashboard después de crear la reserva
    else:
        form = ReservaForm()

    return render(request, 'cancha/crear_reserva.html', {'form': form})


def gestionar_bebidas(request):
    if request.method == 'POST':
        form = BebidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirige al dashboard después de crear o editar la bebida
    else:
        form = BebidaForm()

    return render(request, 'cancha/gestionar_bebidas.html', {'form': form})

def gestionar_stock(request):
    # Aquí puedes implementar la lógica para gestionar el stock de bebidas
    # Puedes listar las bebidas y mostrar un formulario para actualizar su stock o cantidad vendida
    bebidas = Bebida.objects.all()
    return render(request, 'cancha/gestionar_stock.html', {'bebidas': bebidas})

def caja_diaria(request):
    hoy = date.today()
    ventas_hoy = Stock.objects.filter(fecha=hoy).aggregate(total=Sum('cantidad_vendida'))
    return render(request, 'cancha/caja_diaria.html', {'ventas_hoy': ventas_hoy})

def reporte_mensual(request):
    inicio_mes = date.today().replace(day=1)
    fin_mes = inicio_mes + timedelta(days=31)  # Aproximación para obtener el último día del mes
    ventas_mes = Stock.objects.filter(fecha__range=[inicio_mes, fin_mes]).aggregate(total=Sum('cantidad_vendida'))
    return render(request, 'cancha/reporte_mensual.html', {'ventas_mes': ventas_mes})

def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'cancha/listar_usuarios.html', {'usuarios': usuarios})

def gestionar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'gestionar_usuarios.html', {'usuarios': usuarios})

def gestionar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'gestionar_reservas.html', {'reservas': reservas})

def gestionar_bebidas(request):
    bebidas = Bebida.objects.all()
    return render(request, 'gestionar_bebidas.html', {'bebidas': bebidas})

def ver_stock(request):
    stock = Stock.objects.all()
    return render(request, 'ver_stock.html', {'stock': stock})

def caja_diaria(request):
    # Aquí puedes implementar la lógica para ver la caja diaria
    return render(request, 'caja_diaria.html')

def reporte_mensual(request):
    # Aquí puedes implementar la lógica para generar un reporte mensual
    return render(request, 'reporte_mensual.html')
