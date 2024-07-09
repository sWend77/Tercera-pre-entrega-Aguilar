from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Usuario(models.Model):

    user = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=20)
    
    def __str__ (self):
    
        return f"{self.user}"
    
class Musica(models.Model):
    
    name_song = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    release_year = models.IntegerField()

    def __str__(self):
        
        return f"{self.name_song}"
    
class Artista(models.Model):
    
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    birthdate = models.DateField(max_length=30)
    important_albums = models.CharField(max_length=40)
    biografia = models.CharField(max_length= 130423952, default=False)
    imagen = models.ImageField(upload_to='avatares', blank=True , null=True)
        
    def __str__(self):
    
        return f"{self.name}"
    
class Genero (models.Model):   

    name = models.CharField(max_length=30)
    
    def __str__(self):
    
        return f"{self.name}"

class Avatar (models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True , null=True)
    
    def __str__(self):
        return f'Avatar #{self.id}'
    
class Instrumento(models.Model):
    
    TIPO_CHOICES = [
        ('guitarra', 'Guitarra'),
        ('bajo', 'Bajo'),
        ('baterias', 'Baterias'),
        ('violines', 'Violines'),
        ('ukeleles', 'Ukeleles'),
        ('saxofones', 'Saxofones'),
        ('pianos', 'Pianos'),
        ('acordeones' , 'Acordeones'),
        ('flautas' , 'Flautas'),
    ]
    
    marca = models.CharField(max_length=50, default='')
    modelo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='instrumentos/', null=True, blank=True)
    tipo = models.CharField(max_length=50, default="", choices=TIPO_CHOICES)
    
    def __str__(self):
        return (self.tipo + " " + self.marca)

class CategoriaInstrumentos (models.Model):
    
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255, blank=True)
    piso = models.IntegerField(blank=True, null=True)
    imagen = models.ImageField(upload_to='avatares', blank=True , null=True)
    
    def __str__(self):
        return self.user.username

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Instrumento, through='ItemCarrito')
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Carrito de {self.usuario.username}'
    
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre} en {self.carrito}'   










