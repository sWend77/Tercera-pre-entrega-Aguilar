from django.urls import path 
from AppPrueba.views import inicio,registro,musica,login,artistas,instrumentos


urlpatterns = [
    path("", inicio, name = "Inicio"),
    path("registro/", registro, name ="Registro"),
    path("musica/", musica, name = "Musica"),
    path("login/", login, name = "Iniciar sesion"),
    path("artistas/", artistas, name = "Artistas"),
    path("instrumentos/", instrumentos, name = "Instrumentos")    
]
