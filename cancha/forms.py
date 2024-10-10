from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Reserva, Bebida, Stock, Usuario

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'telefono', 'password1', 'password2']

class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ['nombre', 'precio', 'stock']
        
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'cancha', 'fecha_reserva', 'hora_inicio', 'hora_fin']