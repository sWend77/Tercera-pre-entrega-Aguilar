from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect

def inicio (req):
    
    try:
        avatar = Avatar.objects.POST(user=req.user.id)
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

@login_required()
def instrumentos(req):
    
    if req.method == "POST":
        agregar_instrumento = Instrumento(name = req.POST ["name"], brand = req.POST ["brand"] , model = req.POST ["model"], number_series = req.POST ["number_series"])
        agregar_instrumento.save()
        return render(req, "index.html" , {})
    
    else:
        
        mi_formulario = Formulario_instrumento()
        
        return render(req, "instrumentos.html",{"mi_formulario":mi_formulario})

# Seccion login y registro----------------------------------------------------------------------------------------------------------------

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
    
def registro(req):
    if req.method == "POST":
        mi_formulario = CustomUserCreationForm(req.POST)
        
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            usuario = data["username"]
            mi_formulario.save()
            
            return render(req, "index.html", {"message": f"Bienvenido {usuario}, ya eres miembro de MusecK!"})       
            
        else:
            return render(req, "index.html", {"message":"Datos invalidos"})
    else:
        mi_formulario = CustomUserCreationForm()
        return render(req, "registrarse.html", {"mi_formulario": mi_formulario}) 

@login_required
def editar_perfil(req):
    usuario = req.user

    if req.method == "POST":
        mi_formulario = UsereEditForm(req.POST, req.FILES, instance=usuario)

        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]

            password2 = data.get("password2")
            if password2:
                usuario.set_password(password2)

            usuario.save()

            user_profile, created = UserProfile.objects.get_or_create(user=usuario)
            user_profile.direccion = data['direccion']
            user_profile.piso = data['piso']
            user_profile.save()

            avatar, created = Avatar.objects.get_or_create(user=usuario)
            if data['imagen']:
                avatar.imagen = data['imagen']
                avatar.save()

            return render(req, "index.html", {"message": "Datos actualizados con éxito"})
        else:
            return render(req, "editar-perfil.html", {"mi_formulario": mi_formulario})
    else:
        user_profile, created = UserProfile.objects.get_or_create(user=usuario)
        avatar, created = Avatar.objects.get_or_create(user=usuario)
        initial_data = {
            'direccion': user_profile.direccion,
            'piso': user_profile.piso,
            'imagen': avatar.imagen,
        }
        mi_formulario = UsereEditForm(instance=usuario, initial=initial_data)
        return render(req, "editar-perfil.html", {"mi_formulario": mi_formulario})
    

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
    
def about (req):
    
    return render (req, 'about.html', {})
    
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
    
#Seccion Artistas-----------------------------------------------------------------------------------------------------------------------------

def artistas(req):
    if req.method == "POST":
        form = FormularioArtista(req.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre_de_artista')
            pais = form.cleaned_data.get('pais')
            
            
            artistas = Artista.objects.all()
            
            
            if nombre:
                artistas = artistas.filter(name__icontains=nombre)
            
            if pais:
                artistas = artistas.filter(country__icontains=pais)
            
            contexto = {
                'form': form,
                'artistas': artistas,
            }
            return render(req, 'resultado-busqueda-artista.html', contexto)
    else:
        form = FormularioArtista()

    return render(req, 'artistas.html', {'form': form})




#Seccion Market instrumentos--------------------------------------------------------------------------------------------------------------

class ListaPublicaciones(ListView):
    
    model = Instrumento
    template_name = "list-instrumentos.html"
    context_object_name = "instrumentos"
    
class DetailPublicaciones (DetailView):
    
    model = Instrumento
    template_name = "detail-instrumentos.html"
    context_object_name = "detalle-instrumentos"

class CreatePublicaciones (CreateView):
    
    model = Instrumento
    template_name = "crear-publicacion.html"
    fields =  ['imagen','tipo','marca','modelo','precio','cantidad_disponible']
    success_url = "/app-include/"
    context_object_name = 'form'
    
class UpdatePublicaciones (UpdateView):
    
    model = Instrumento
    template_name = "update-instrumento"
    fields = ["name"]
    success_url = "index.html"
    
class DeletePublicaciones (DeleteView):
    
    model = Instrumento
    template_name = "delete-instrumento.html"
    success_url = "index.html"
    

# -------------------------------------------------------------------------------------------------------------------------------------------------------
    
class CrearCategoriaInstrumentos(CreateView):
    
    model= CategoriaInstrumentos
    template_name = "crear-categoria.html"
    fields = ["nombre"]
    success_url = "/app-include/agregar-categoria/"

class ListaCategoria(LoginRequiredMixin, ListView):
    
    model = CategoriaInstrumentos
    template_name = "lista-categorias.html"
    context_object_name = "categorias"

class DetailCategoria(DetailView):
    
    model = CategoriaInstrumentos
    template_name = "detail-categoria.html"
    context_object_name = "categoria"
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['form'] = BusquedaForm()
        return contexto
    
def buscar_instrumentos(req):
    if req.method == "POST":
        form = BusquedaForm(req.POST)
        
        if form.is_valid():
            busqueda = form.cleaned_data["buscar"]
            
            tipo = ""
            marca = ""
            modelo = ""
            
            if ' ' in busqueda:
                tipo, marca, modelo = busqueda.split(' ', 1)
            else:
                
                tipo = busqueda
                marca = busqueda
                modelo =busqueda

            
            resultados =Instrumento.objects.filter(tipo__icontains=tipo, marca__icontains=marca) | \
                        Instrumento.objects.filter(tipo__icontains=tipo) | \
                        Instrumento.objects.filter(marca__icontains=marca) | \
                        Instrumento.objects.filter(tipo__icontains=tipo, marca__icontains=marca, modelo__icontains=modelo) | \
                        Instrumento.objects.filter(modelo__icontains=modelo) | \
                        Instrumento.objects.filter(marca__icontains=marca, modelo__icontains=modelo)    
            
            return render(req, "resultado_busqueda_instrumentos.html", {"resultados": resultados})
        else:
            return render(req, "index.html", {"message": "Datos incorrectos"})
    
    else:
        form = BusquedaForm()
        return render(req, "detail-categoria.html", {"form": form})

def comprar(req, pk):
    
    instrumento = get_object_or_404(Instrumento, pk=pk)
    
    return render(req, "datos-compra.html", {"instrumento": instrumento})

def agregar_carrito(req, pk):
    
    instrumento = get_object_or_404(Instrumento, pk=pk)
    
    return render(req, "datos-carrito.html", {"instrumento": instrumento})

  
def seleccionar_cantidad(req):
    
    if req.method == "POST":
        
        instrumento_id = req.POST.get('instrumento_id')
        
        cantidad = int(req.POST.get('cantidad', 0))
        
        if instrumento_id:
            
            instrumento = get_object_or_404(Instrumento, id=instrumento_id)
            
            if cantidad > 0 and cantidad <= instrumento.cantidad_disponible:
                
                resultados = Instrumento.objects.filter(id=instrumento_id)
                
                return render(req, "resultado_busqueda_instrumentos.html", {"resultados": resultados})
            
            else:
                
                mensaje = f'La cantidad seleccionada ({cantidad}) es inválida o excede la cantidad disponible ({instrumento.cantidad_disponible}).'
                
                return render(req, "index.html", {"message": mensaje})
        
        else:
            
            return HttpResponseBadRequest("No se ha proporcionado un ID de instrumento válido.")        
    
    else:
        instrumento_id = req.GET.get('instrumento_id') 
        
        if instrumento_id:
            
            instrumento = get_object_or_404(Instrumento, id=instrumento_id)
            
            return render(req, "detail-categoria.html", {"instrumento": instrumento})
        
        else:
            
            return HttpResponseBadRequest("No se ha proporcionado un ID de instrumento válido.")

def elegir_pago (req):
    
    return render (req, "forma-pago.html", {})

@login_required
def agregar_al_carrito(req, pk):
    
    producto = get_object_or_404(Instrumento, pk=pk)
    carrito, creado = Carrito.objects.get_or_create(usuario=req.user)
    
    item_carrito, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    
    if not creado:
        item_carrito.save()
    
    return redirect('MiCarrito')

@login_required
def ver_carrito(req):
    carrito, creado = Carrito.objects.get_or_create(usuario=req.user)
    items_carrito = ItemCarrito.objects.filter(carrito=carrito)
    
    if req.method == "POST":
        for item in items_carrito:
            cantidad = int(req.POST.get(f'cantidad_{item.id}', 1))
            item.cantidad = cantidad
            item.save()
        
    precio_total = sum(item.producto.precio * item.cantidad for item in items_carrito)
    
    return render(req, 'carrito.html', {'carrito': carrito, 'items_carrito': items_carrito, 'precio_total': precio_total})

    
class DeleteItem (DeleteView):
    
    model = ItemCarrito
    template_name = "delete-item.html"
    success_url = "/app-include/carrito/"
    context_object_name = "delete"
    

def tu_vista_principal(req):
    
    carrito = Carrito.objects.get(usuario=req.user)
    
    return render(req, 'navbar.html', {'carrito': carrito})

def confirmar_pago_tarjeta(req):
    
    return render(req , 'pago-tarjeta.html', {})

def suma_precios(req):
    items_carrito = Carrito.objects.filter(usuario=req.user)  
    precio_total = sum(item.producto.precio for item in items_carrito)

    return render(req, 'carrito.html', {
        'items_carrito': items_carrito,
        'precio_total': precio_total,
    })






























