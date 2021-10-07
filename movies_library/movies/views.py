from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from .models import Movie,Category

# Create your views here.

#list all movies
def index(request):
    movies = Movie.objects.all()
    return render(request,'movies/index.html',{'movies': movies})

def add_movie(request):
    if request.method =='POST':
        m = Movie()
        c = Category.objects.get(id=request.POST['category'])

        m.movie_name = request.POST['movie_name']
        m.publish_date = request.POST['publish_date']
        m.category = c

        m.save()

        return HttpResponseRedirect(reverse('movies:index'))


    return render(request,'movies/adicionar.html')