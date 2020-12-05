from django.shortcuts import render
from subprocess import *


def inicio(request):

    ubicacion = getoutput("pwd")
    carpetas = getoutput("find . -maxdepth 1 -type d")
    carpetas = carpetas.split("\n")
    carpetas2 = []
    for i in range(1, len(carpetas)):
        carpetas2.append(carpetas[i][2:])
    return render(request, "index.html", {"ubicacion":ubicacion, "carpetas":carpetas})
