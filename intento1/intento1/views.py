from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):

    return render(request, "index.html")

def buscar(request):

    mensaje = "Ingreso "+ request.GET["aBuscar"]

    return HttpResponse(mensaje)