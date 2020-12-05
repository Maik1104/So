from django.shortcuts import render
from subprocess import *


def inicio(request):

    ubicacion=getoutput("pwd")
    carpetas=getoutput("find . -maxdepth 1 -type f ")
    return render(request, "index.html", {"ubicacion":ubicacion, "carpetas":carpetas})
