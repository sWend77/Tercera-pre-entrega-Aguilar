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
    
    
    
class Instrumento(models.Model):
    
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    number_series = models.IntegerField()
    
    def __str__(self):
    
        return f"{self.name}"
    
class Genero (models.Model):   

    name = models.CharField(max_length=30)
    
    def __str__(self):
    
        return f"{self.name}"

class Producto (models.Model):
    
    name = models.CharField(max_length=20)
    brand = models.CharField (max_length=20)
    price = models.IntegerField ()
    
class Avatar (models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True , null=True)
    
   























