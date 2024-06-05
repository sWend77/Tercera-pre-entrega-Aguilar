from django.db import models

# Create your models here.

class Usuario(models.Model):

    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
class Guitarras(models.Model):
    
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    nro_de_serie = models.IntegerField()
    





























