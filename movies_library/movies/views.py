from django.shortcuts import render
from .models import Movie

# Create your views here.

#list all movies
def index(request):
    movies = Movie.objects.all()
    return render(request,'movies/index.html',{'movies': movies})

def add_movie(request):
    return render(request,'movies/adicionar.html')