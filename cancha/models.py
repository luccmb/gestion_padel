from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
import datetime

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True, null=True)
    es_administrador = models.BooleanField(default=False)

    # Añadimos related_name para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username
    
class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)  # Por ejemplo: césped, tierra, sintética

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    dia_semana = models.CharField(max_length=9)  # Lunes, Martes, etc.
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.dia_semana} de {self.hora_inicio} a {self.hora_fin}"


class Reserva(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, default=1)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f'Reserva de {self.usuario} en {self.cancha}'

class Bebida(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE, related_name='bebidas_stock', default=1)  # Define un valor predeterminado

    def __str__(self):
        return self.nombre

class Stock(models.Model):
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE, related_name='stock_items')
    cantidad = models.PositiveIntegerField(default=0)  # Definir un valor predeterminado
    cantidad_vendida = models.PositiveIntegerField(default=0)  # También puedes definir este campo si es necesario

    def __str__(self):
        return f"{self.bebida.nombre} - Vendido: {self.cantidad_vendida}"


class CajaDiaria(models.Model):
    fecha = models.DateField(auto_now_add=True)
    total_reservas = models.DecimalField(max_digits=7, decimal_places=2)
    total_bebidas = models.DecimalField(max_digits=7, decimal_places=2)
    total_dia = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"Total del día {self.fecha}: ${self.total_dia}"

class ReporteMensual(models.Model):
    mes = models.CharField(max_length=20)  # Enero, Febrero, etc.
    total_reservas = models.DecimalField(max_digits=10, decimal_places=2)
    total_bebidas = models.DecimalField(max_digits=10, decimal_places=2)
    total_mensual = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reporte de {self.mes}: ${self.total_mensual}"
    

