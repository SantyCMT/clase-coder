from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def inicio(request):
    return render(request, "appcoder/index.html")


def Estudiantes(request):
    return HttpResponse("estudiantes")
    
def Profesor(request):
    return HttpResponse("Profesor")

def Curso(request):
    return HttpResponse("Curso")

def Catedra(request):
    return HttpResponse("Catedra")

def Comicion(request):
    return HttpResponse("Comicion")