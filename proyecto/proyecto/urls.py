from django.urls import path
from proyecto.proyecto.views import inicio

urlpatterns = [
    path('', inicio),
]
