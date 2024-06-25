from django.urls import path 
from AppPrueba.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio, name = "Inicio"),
    path("registro/", registro, name ="Registro"),
    path("musica/", musica, name = "Musica"),
    path("login_view/", login_view, name = "IniciarSesion"),
    path("artistas/", artistas, name = "Artistas"),
    path("lista-categorias/", ListaCategoria.as_view(), name = "Categorias"),
    path("busqueda_username/", busqueda_usuarios, name="Busqueda"),    
    path("buscar/", buscar, name = "BuscarUsuario"),
    path("lista-generos/", ListaGenero.as_view(), name = "ListaGeneros"),
    path("detail-genero/<pk>", DetailGenero.as_view(), name = "DetalleGeneros"),
    path("create-genero/", CreateGenero.as_view(), name = "CrearGenero"),
    path("delete-genero/<pk>", DeleteGenero.as_view(), name = "EliminarGenero"),
    path("edit-genero/<pk>", UpdateGenero.as_view(), name = "EditarGenero"),
    path("logout/", LogoutView.as_view(template_name = "logout.html"), name = "LogoutUser"),
    path("edit-perfil/", editar_perfil, name = "EditarPerfil"),
    path("agregar-avatar/", agregar_avatar, name = "AgregarAvatar"),
    path("about/", about, name = "AboutMe"),
    path("detail-categoria/<pk>", DetailCategoria.as_view(), name = "DetalleCategoria"),
    path("publicaciones/", ListaPublicaciones.as_view(), name = "ListaPublicaiones"),
    path("resultado-busqueda-instrumentos/", buscar_instrumentos, name = "ResultadoInstrumentos"),
    path("datos-compras/<int:pk>", comprar, name = "DatosCompras"),
    path("carrito/<int:pk>" , agregar_carrito, name = "MiCarrito"),
    path("realiza-pago/" , seleccionar_cantidad, name = "SeleccionarCantidad"),
]
