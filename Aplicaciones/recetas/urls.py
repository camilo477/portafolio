from django.urls import path
from .views import nombre_view

urlpatterns = [
    path('recetas/', nombre_view, name='recetas_view'),
    # Otras URL de tu aplicación
]
