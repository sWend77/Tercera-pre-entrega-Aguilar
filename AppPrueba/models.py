from django.db import models
from django.contrib.auth.models import User


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
    
    def __str__(self):
    
        return f"{self.name}"
    
class Genero (models.Model):   

    name = models.CharField(max_length=30)
    
    def __str__(self):
    
        return f"{self.name}"

class Avatar (models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True , null=True)
    

class Producto(models.Model):
    
    name = models.CharField (max_length=50)
        
class Instrumento(models.Model):
    marca = models.CharField(max_length=50, default='Sin marca')
    modelo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='instrumentos/', null=True, blank=True)
    
    def __str__(self):
        return self.marca

class CategoriaInstrumentos (models.Model):
    
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    















