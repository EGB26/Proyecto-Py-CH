from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def curso(self):
    Curso = curso(nombre="Desarrollo Web", camada=19881)
    Curso.save()
    documentoDeTexto = f"--->Curso: {Curso.nombre} Camada: {Curso.camada}"
    return HttpResponse(documentoDeTexto)
