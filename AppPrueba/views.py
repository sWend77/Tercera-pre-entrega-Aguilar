from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def inicio (req):
    
    return render(req, "index.html",{})

def registro (req): 
    
    print("method:",req.method)
    print("method:",req.POST)
    
    if req.method == "POST":
        nuevo_usuario = Usuario(user = req.POST ["username"] , email = req.POST ["email"] , password = req.POST ["password"])
        nuevo_usuario.save()
        return render(req, "index.html", {})
    
    else:
        return render(req, "registrarse.html",{})

def musica(req):
    
    if req.method == "POST":
        nueva_cancion = Musica(name_song = req.POST ["name_song"] , artist = req.POST["artist"] , gender = req.POST ["gender"] , release_year = req.POST ["release_year"])
        nueva_cancion.save()
        return render(req, "musica.html",{})
    
    else:
        return render(req, "musica.html",{})

def artistas(req):
    
    if req.method == "POST":
        nuevo_artista = Artista(name = req.POST ["name"], country = req.POST ["country"], birthdate = req.POST ["birthdate"], important_albums = req.POST ["important_albums"])
        nuevo_artista.save()
        return render(req, "artistas.html",{})
        
    else:
        return render(req, "artistas.html",{})

def instrumentos(req):
    
    if req.method == "POST":
        agregar_instrumento = Instrumento(name = req.POST ["name"], brand = req.POST ["brand"] , model = req.POST ["model"], number_series = req.POST ["number_series"])
        agregar_instrumento.save()
        return render(req, "instrumentos.html" , {})
    
    else:
        return render(req, "instrumentos.html",{})

def login(req):
    
    return render(req, "iniciar_sesion.html",{})


    


    



























