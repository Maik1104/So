from django.shortcuts import render
from subprocess import *


def inicio(request):

    ubicacion=getoutput("pwd")
    carpetas=getoutput("find . -maxdepth 1 -type d")
    carpetas = carpetas.split(" ")
    for i in range(len(carpetas)):
        carpetas[i] = carpetas[i][2:]
    return render(request, "index.html", {"ubicacion":ubicacion, "carpetas":carpetas})
