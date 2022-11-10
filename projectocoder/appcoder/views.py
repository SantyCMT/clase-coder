from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def inicio(request):
    return render(request, "appcoder/index.html")


def Estudiantes(request):
    return render(request, "appcoder/estudiantes.html")
    
def Profesor(request):
    return render(request, "appcoder/profesores.html")

def Curso(request):
    return render(request, "appcoder/cursos.html")

def Catedra(request):
    return render(request, "appcoder/catedra.html")

def Entrega(request):
    return render(request, "appcoder/entregables.html")