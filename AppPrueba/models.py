from django.db import models

# Create your models here.

class Usuario(models.Model):

    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
class Musica(models.Model):
    
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    release_year = models.IntegerField()
    
class Artista():
    
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    birthdate = models.CharField(max_length=30)
    important_albums = models.CharField(max_length=40)
    
class Instrumento():
    
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    number_series = models.IntegerField()
    
    




























