from django.http import HttpResponse
import random
from django.template import Template, Context
from datetime import datetime
"""
OJO: importar de django el modulo

2 objetos necesarios para realizar una petición a una URL y devolver una respuestaa traves de una vista.    
    
    # Request: para realizar peticiones al servidor.
    
    # httpResponsive: Para enviar la respuesta usando el protocolo HTTP.
    
    
    jango utiliza objetos request y response para pasar estado a través del sistema.

Cuando se solicita una página, Django crea un objeto HttpRequest que contiene metadatos sobre la solicitud. 
Entonces Django carga la vista apropiada, pasando el objeto HttpRequest como primer argumento a la función 
de la funcion vista. Cada vista es responsable de devolver un objeto HttpResponse.
    
"""


# Esto es una vista
def bienvenida(request): #>> aqui pasamos un objeto de tipo request como argumento.
    return HttpResponse ("bienvenido a este curso de Django !!! ")

def estilo_rojo(request):
    return HttpResponse("<h1 style= color:red> Este es otro estilo de prueba       </h1>")

def categoria_edad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera edad"
        else:
            categoria = "adultez"    
    else:
            if edad < 10: categoria = "infancia" 
            else: categoria = "adolescencia"
    resultado = " <h1> Categoria de la edad: %s</h1>" %categoria         
    return HttpResponse(resultado)
    
def random_number(request):
    numero = random.randint(1,10)
    mostrar = '<h1>Tu numero al azar es: </h1>%s' %numero
    return HttpResponse(mostrar)        

def conthtml(request, nombre, edad):
    contenido = """
    
    <!DOCTYPE html>
<html lang="en">

  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML Prueba</title>
    
  </head>
  
  <body>
	<h1> Tu nombre es: </h1> <p>%s </p>
    <p> </p>
    <h1> Tu edad es: </h1> <p>%s </p>
  </body>
</html>
    
    """%(nombre, edad)
    return HttpResponse(contenido) 

def contplant(request):
    
    #Asi se abre una plantilla llamada index alojada en la carpeta templates.
    plantillaindex = open("C:/Users/desarrollo.1/OneDrive - DICOP CONSULTING S.L/Documentos/django1/proyecto1/templates/index.html")
    # Cargar el documento en una variable de tipo plantilla.
    temp = Template(plantillaindex.read())
    # Es una buena practica cerrar el documento externo que alberga la plantilla. Asi se hace:
    plantillaindex.close()
    # Aqui creamos un contexto 
    contexto = Context()
    #Renderizar el documento:
    documento= temp.render(contexto)
    #final de todo con return y HttpResponse
    return HttpResponse(documento)
    
def plantParam(request):
    
    nombre = "Daniel"
    fecha_actual= datetime.now
       
    plantillaindex = open("C:/Users/desarrollo.1/OneDrive - DICOP CONSULTING S.L/Documentos/django1/proyecto1/templates/plantillaParametros.html")

    temp = Template(plantillaindex.read())

    plantillaindex.close()

    contexto = Context({"nombre_autor":nombre, "fecha_actual":fecha_actual})

    documento= temp.render(contexto)

    return HttpResponse(documento)
    
    
def plant_listas(request):
    
    nombre = "Daniel"
    fecha_actual= datetime.now
    lenguaje_programacion = ["Python", "Java", "Javascript","C#"]
    
       
    plantillaindex = open("C:/Users/desarrollo.1/OneDrive - DICOP CONSULTING S.L/Documentos/django1/proyecto1/templates/plantListas.html")

    temp = Template(plantillaindex.read())

    plantillaindex.close()

    contexto = Context({"nombre_autor":nombre, "fecha_actual":fecha_actual, "lenguajes":lenguaje_programacion})

    documento= temp.render(contexto)

    return HttpResponse(documento)  