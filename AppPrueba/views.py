from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def inicio (req):
    
    plantilla = loader.get_template("index.html")
    
    doc = plantilla.render()
    
    return HttpResponse (doc) 

def registrarse (req, user, password): 
    
    users = Usuario(user = user, password = password)
    users.save()
    return HttpResponse(f"Usuario: {user} agregado exitosamente!")

def iniciar_sesion(req, user, password):
    
    users = Usuario (user = user , password = password)
    users.save()
    return HttpResponse("Iniciando sesion...")


    


    



























