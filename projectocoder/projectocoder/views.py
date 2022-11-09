import imp
from datetime import datetime
from pydoc import doc
from django.http import HttpResponse
from django.template import Template, Context, loader



def vista_saludo(request):
    return HttpResponse("""
    <h1>Hola coders! :) </h1>
    <p style='color:red' >Esto es una prueba</p>
    """
)


def iniciar_sesion(request):
    return HttpResponse("pasame tu wp")


def dia_hoy(request, nombre):
    hoy = datetime.now()

    respuesta = f"Hoy es {hoy} - Bienvenid@ {nombre}"
    return HttpResponse(respuesta)

 
def calcular_año(request, edad):
    edad=int(edad)


    fecha_nacimiento= datetime.now().year - edad
    return HttpResponse(fecha_nacimiento)   


def vista_plantilla(request):
    archivo = open(r"D:\coder\17_django\projectocoder\projectocoder\templates\plantilla_bonita.html")

    plantilla = Template(archivo.read())

    archivo.close()

    datos = {"nombre":"santiago", "fecha": datetime.now(),"apellido": "ortiz", "edad": 20}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)



def vista_listado_alumnos(request):
    
    archivo = open(r"D:\coder\17_django\projectocoder\projectocoder\templates\listado_alumnos.html")

    plantilla = Template(archivo.read())

    archivo.close()

    listado_alumnos = ["Leonel Gareis", "Santiago ortiz", "Agustin Garcia", "Cristian Franco", "Barbara pelaez"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}
    
    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def vista_listado_alumnos2(request):
    listado_alumnos = ["Leonel Gareis", "Santiago ortiz", "Agustin Garcia", "Cristian Franco", "Barbara pelaez"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}

    plantilla = loader.get_template("listado_alumnos.html")

    documento= plantilla.render(datos)
    
    return HttpResponse(documento)


def vista_plantilla2(request):

    datos = {"nombre":"santiago", "fecha": datetime.now(),"apellido": "ortiz", "edad": 20}

    plantilla = loader.get_template("plantilla_bonita.html")
    documento = plantilla.render(datos)

    return HttpResponse(documento)