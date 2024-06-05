from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def inicio (req):
    
    return render(req, "index.html",{})

def registro (req): 
    
    return render(req, "registrarse.html",{})

def musica(req):
    
    return render(req, "musica.html",{})

def login(req):
    
    return render(req, "iniciar_sesion.html",{})

def artistas(req):
    
    return render(req, "artistas.html",{})

def instrumentos(req):
    
    return render(req, "instrumentos.html",{})




    


    



























