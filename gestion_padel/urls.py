from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cancha/', include('cancha.urls')),  # Incluye las URLs de la app "cancha"
    path('', RedirectView.as_view(url='/cancha/', permanent=False)),  # Redirige la raíz a /cancha/
]
