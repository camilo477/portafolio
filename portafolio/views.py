from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def inicio(request):
    return render(request,"pages/inicio.html",{})

@login_required
def resumen(request):
    return render(request,"pages/resumen.html",{})

def login(request):
    return render(request,"registration/login.html", {})