from django.shortcuts import render
from subprocess import *


def inicio(request):

    ubicacion=getoutput("pwd")

    return render(request, "index.html", {"ubicacion":ubicacion})
