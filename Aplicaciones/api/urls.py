from django.urls import path
from . import views

urlpatterns = [ 
    path("mapa/", views.sitios_interes, name="Mapa"),
]
