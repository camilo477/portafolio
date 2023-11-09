from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import inicio, resumen, login  # Cambia 'login_view' a 'login'

from django.urls import re_path
from django.views.static import serve

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio, name="inicio"),
    path("inicio/", inicio, name="inicio"),
    path("resumen/", resumen, name="resumen"),
    path('login/', login, name='login'),
    path("", include('Aplicaciones.proyectos.urls')), 
    path("", include('Aplicaciones.contacto.urls')),  
    path("", include('Aplicaciones.api.urls')),
    path("", include('Aplicaciones.recetas.urls')),
    path("", include('Aplicaciones.usuarios.urls')),    
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
