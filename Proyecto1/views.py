from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader

def saludo (req):
    return HttpResponse ("Hola! que tal! Como estas?")

def saludo_personalizado (req, nombre):
    
    datos = f"Hola, mi nombre es {nombre}. Como estas?"
    
    return HttpResponse (datos) 

def inicio (req):
    
    # mi_html = open("C:/Users/diego/Documents/Visual Studio Code/proyecto-python/Proyecto1/templates/index.html")
    
    # plantilla = Template(mi_html.read())
    
    # mi_html.close()
    
    # mi_contexto = Context()
    
    plantilla = loader.get_template("index.html")
    
    doc = plantilla.render()
    
    return HttpResponse (doc)
























