from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import loader
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def inicio (req):
    
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "index.html", {"url" : avatar.imagen.url})
    except:
        return render(req, "index.html", {})
    
    
    
    return render(req, "index.html", {"url" : avatar.imagen.url})

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

@login_required()
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


# Seccion login----------------------------------------------------------------------------------------------------------------

def login_view (req):
    
    if req.method == "POST":
        
        mi_formulario = AuthenticationForm(req, data=req.POST)
        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            
            usuario = data["username"]
            pw = data["password"]
            
            user = authenticate(username = usuario, password = pw)
            
            if user:
                login(req, user)
                return render(req, "index.html" , {"message": f"Bienvenido {usuario}!"})       
            else: return render(req, "index.html" , {"message":"Datos erroneos"} )
        else: return render (req, "index.html" , {"message":"Datos invalidos"})
    else:
        mi_formulario = AuthenticationForm()
        return render (req, "login.html",{"mi_formulario": mi_formulario})
    
def registro (req):
    
    if req.method == "POST":
        
        mi_formulario = UserCreationForm(req.POST)
        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            
            usuario = data["username"]
            
            user = authenticate(username = usuario)
            
            mi_formulario.save()
            
            return render(req, "index.html" , {"message": f"Bienvenido {usuario}, ya eres miembro de MusecK!"})       
            
        else: return render (req, "index.html" , {"message":"Datos invalidos"})
    else:
        mi_formulario = UserCreationForm()
        return render (req, "registrarse.html",{"mi_formulario": mi_formulario})    

@login_required    
def editar_perfil (req):
    
    if req.method == "POST":
        
        usuario = req.user
        
        mi_formulario = UsereEditForm(req.POST, instance = req.user)
        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password2"])
            
            usuario.save()
            
            return render(req, "index.html" , {"message": "Datos Actualizados con exito!"})       
            
        else: return render (req, "editar-perfil.html",{"mi_formulario": mi_formulario}) 
    else:
        mi_formulario = UsereEditForm(instance = req.user)
        return render (req, "editar-perfil.html",{"mi_formulario": mi_formulario})
    
@login_required
def agregar_avatar (req):
    
    if req.method == "POST":
        
        mi_formulario = FormularioAvatar(req.POST , req.FILES)
        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            
            avatar = Avatar(user=req.user,imagen=data['imagen'])
            
            avatar.save()
            
            return render(req, "index.html" , {"message": "Avatar cargado con exito"})       
            
        else: return render (req, "index.html" , {"message":"Ocurrio un error al cargar el avatar"})
    else:
        
        mi_formulario = FormularioAvatar()
        
        return render (req, "agregar_avatar.html",{ "mi_formulario": mi_formulario})    
    
    
    
    
    
    
    
    
    
        

#Seccion Musica--------------------------------------------------------------------------------------------------------------

class ListaGenero(ListView):
    
    model = Genero
    template_name = "list-genero.html"
    context_object_name = "generos"
    
class DetailGenero (DetailView):
    
    model = Genero
    template_name = "detail-genero.html"
    context_object_name = "detalle"

class CreateGenero (CreateView):
    
    model = Genero
    template_name = "create-genero.html"
    fields =  ["name"]
    success_url = "/app-include/lista-generos/"
    
class UpdateGenero (UpdateView):
    
    model = Genero 
    template_name = "update-genero.html"
    fields = ["name"]
    success_url = "/app-include/lista-generos/"
    context_object_name = "genero"
    
class DeleteGenero (DeleteView):
    
    model = Genero
    template_name = "delete-genero.html"
    success_url = "/app-include/lista-generos/"
    context_object_name = "genero"
    
#Seccion Instrument shop--------------------------------------------------------------------------------------------------------------

class ListaProducto(ListView):
    
    model = Producto
    template_name = "list-productos.html"
    context_object_name = "productos"
    
class DetailProducto (DetailView):
    
    model = Genero
    template_name = "detail-productos.html"
    context_object_name = "detalle-productos"

class CreateProducto (CreateView):
    
    model = Genero
    template_name = "create-producto.html"
    fields =  ["name","brand","price"]
    success_url = "/app-include/lista-productos/"
    
class UpdateProducto (UpdateView):
    
    model = Genero 
    template_name = "update-producto"
    fields = ["name"]
    success_url = "index.html"
    
class DeleteProducto (DeleteView):
    
    model = Genero
    template_name = "delete-producto.html"
    success_url = "index.html"
    


























