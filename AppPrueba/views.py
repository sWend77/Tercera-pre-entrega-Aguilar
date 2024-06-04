from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse

# Create your views here.

def usuarios(req, user, password):
    users = Usuario( user = user, password = password)
    users.save()
    return HttpResponse(f"Usuario: {user} agregado exitosamente!")

    



























