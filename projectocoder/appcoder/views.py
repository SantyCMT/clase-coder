from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

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