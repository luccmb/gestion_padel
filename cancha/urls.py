from django.urls import path
from . import views
from .views import gestionar_reservas

app_name = 'cancha'

urlpatterns = [
    path('', views.gestionar_reservas, name='gestionar_reservas'),  # URL por defecto
    path('gestionar_usuarios/', views.gestionar_usuarios, name='gestionar_usuarios'),
    path('gestionar_bebidas/', views.gestionar_bebidas, name='gestionar_bebidas'),
    path('ver_stock/', views.ver_stock, name='ver_stock'),
    path('caja_diaria/', views.caja_diaria, name='caja_diaria'),
    path('reporte_mensual/', views.reporte_mensual, name='reporte_mensual'),
    path('gestionar-reservas/', gestionar_reservas, name='gestionar_reservas'),
    path('crear/', views.crear_reserva, name='crear_reserva'),
]
