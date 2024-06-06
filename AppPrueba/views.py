from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import loader
from .forms import *

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
        
        mi_formulario = Formulario_registro()
        
        return render(req, "registrarse.html",{"mi_formulario": mi_formulario})

def musica(req):
    
    if req.method == "POST":
        nueva_cancion = Musica(name_song = req.POST ["name_song"] , artist = req.POST["artist"] , gender = req.POST ["gender"] , release_year = req.POST ["release_year"])
        nueva_cancion.save()
        return render(req, "index.html",{})
    
    else:
        
        mi_formulario = Formulario_musica()
        
        return render(req, "musica.html",{"mi_formulario":mi_formulario})

def artistas(req):
    
    if req.method == "POST":
        nuevo_artista = Artista(name = req.POST ["name"], country = req.POST ["country"], birthdate = req.POST ["birthdate"], important_albums = req.POST ["important_albums"])
        nuevo_artista.save()
        return render(req, "index.html",{})
        
    else:
        
        mi_formulario = Formulario_artista()
        
        return render(req, "artistas.html",{"mi_formulario":mi_formulario})

def instrumentos(req):
    
    if req.method == "POST":
        agregar_instrumento = Instrumento(name = req.POST ["name"], brand = req.POST ["brand"] , model = req.POST ["model"], number_series = req.POST ["number_series"])
        agregar_instrumento.save()
        return render(req, "index.html" , {})
    
    else:
        
        mi_formulario = Formulario_instrumento()
        
        return render(req, "instrumentos.html",{"mi_formulario":mi_formulario})

def busqueda_usuarios(req):
    
    return render(req, "busqueda_usuarios.html",{}) 

def buscar(req):
    
    if req.GET["user"]:
        
        user = req.GET["user"]
        
        usuario = Usuario.objects.get( user = user)
        
        return render(req, "resultado_busqueda.html",{"usuario":usuario , "user": user})
        
    else:
        return render(req, "index.html", {"message" : "No enviaste el dato de usuario"})    

def login (req):
    
    return render(req, "iniciar_sesion.html",{})


    


    



























