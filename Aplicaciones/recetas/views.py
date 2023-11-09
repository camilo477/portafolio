from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests

def nombre_view(request):
    current_nombre = 'pancakes'  # Nombre predeterminado
    
    if request.method == 'POST':
        new_nombre = request.POST.get('new_nombre')
        if new_nombre:
            current_nombre = new_nombre

            # Realizar solicitud a la API con el nuevo nombre
            api_url = f'http://kmiska.pythonanywhere.com/nombres?nombre={current_nombre}'
            response = requests.get(api_url)

            # Verificar que la solicitud fue exitosa (código de respuesta 200)
            if response.status_code == 200:
                api_data = response.json()
                recetas = api_data.get('recetas', [])
            else:
                recetas = []
    else:
        # Si no es una solicitud POST, obtener las recetas predeterminadas
        api_url = f'http://kmiska.pythonanywhere.com/nombres?nombre={current_nombre}'
        response = requests.get(api_url)

        if response.status_code == 200:
            api_data = response.json()
            recetas = api_data.get('recetas', [])
        else:
            recetas = []

    return render(request, 'recetas.html', {'current_nombre': current_nombre, 'recetas': recetas})
