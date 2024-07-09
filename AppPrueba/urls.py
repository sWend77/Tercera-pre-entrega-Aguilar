from django.urls import path 
from AppPrueba.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", inicio, name = "Inicio"),
    path("registro/", registro, name ="Registro"),
    path("musica/", musica, name = "Musica"),
    path("login_view/", login_view, name = "IniciarSesion"),
    path("artistas/", artistas, name = "Artistas"),
    path("lista-categorias/", ListaCategoria.as_view(), name = "Categorias"),
    path("lista-generos/", ListaGenero.as_view(), name = "ListaGeneros"),
    path("detail-genero/<pk>", DetailGenero.as_view(), name = "DetalleGeneros"),
    path("create-genero/", CreateGenero.as_view(), name = "CrearGenero"),
    path("delete-item/<int:pk>", DeleteItem.as_view(), name = "EliminarItem"),
    path("edit-genero/<pk>", UpdateGenero.as_view(), name = "EditarGenero"),
    path("logout/", LogoutView.as_view(template_name = "logout.html"), name = "LogoutUser"),
    path("edit-perfil/", editar_perfil, name = "EditarPerfil"),
    path("agregar-avatar/", agregar_avatar, name = "AgregarAvatar"),
    path("about/", about, name = "AboutMe"),
    path("detail-categoria/<int:pk>", DetailCategoria.as_view(), name = "DetalleCategoria"),
    path("publicaciones/", ListaPublicaciones.as_view(), name = "ListaPublicaiones"),
    path("resultado-busqueda-instrumentos/", buscar_instrumentos, name = "ResultadoInstrumentos"),
    path("datos-compras/<pk>", comprar, name = "DatosCompras"),
    path('carrito/', ver_carrito, name='MiCarrito'),
    path("seleccionar-cantidad/" , seleccionar_cantidad, name = "SeleccionarCantidad"),
    path("forma-pago/" , elegir_pago, name = "FormaPago"),
    path("resultados-artistas/" , artistas, name = "ResultadosArtistas"),
    path("datos-carrito/<int:pk>" , agregar_carrito, name = "DatosCarrito"),
    path("agregar-producto/<int:pk>" , agregar_al_carrito, name = "AgregarProducto"),
    path("confirmar-pago/" , confirmar_pago_tarjeta, name = "ConfirmarPago"),
    path("crear-publicaciones/" , CreatePublicaciones.as_view(), name = "CrearPublicaciones"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)