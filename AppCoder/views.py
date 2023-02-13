from django.shortcuts import render
from django.http import HttpResponse
#from AppCoder.models import *

# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/inicio.html')
    #return HttpResponse('vista inicio')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')
    #return HttpResponse('vista cursos')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')
    #return HttpResponse('vista profesores')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')
    #return HttpResponse('vista estudiantes')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')
    #return HttpResponse('vista entregables')
""""
def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada=19881)
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)
"""
def cursoFormulario(request):
    return render(request="AppCoder/cursoFormulario.html")