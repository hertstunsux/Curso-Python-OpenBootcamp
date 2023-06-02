from django.shortcuts import render

# Create your views here.

from .models import Director,Pelicula

def index(request):
    num_directores = Director.objects.all().count()
    num_peliculas = Pelicula.objects.all().count()
    return render (
        request, 
        'index.html', 
        context={
            'num_directores':num_directores,
            'num_peliculas':num_peliculas
            }
            )
def directores(request):
    directores = Director.objects.all()
    return render (
        request, 
        'directores.html', 
        context={
            'directores':directores
            }
            )
def peliculas(request):
    peliculas = Pelicula.objects.all()
    return render (
        request, 
        'peliculas.html', 
        context={
            'peliculas': peliculas
            }
            )