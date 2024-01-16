from django.shortcuts import render, HttpResponse
from .models import Movie, MovieType
from django.views import generic

# Create your views here.

def Index(request):

    movieCount = Movie.objects.all().count()

    myList = ['1','2','3','4','5']

    props = {
        'movieCount' : movieCount,
        'movieType' : list(MovieType.objects.all()),
        'myName' : "Denis Malyshev",
        'movieType2': myList
    }

    return render(request, 'cat.html', context = props)


def Cat2(request):
    props = {}
    return render(request, 'cat2.html', context=props)

def Cat3(request):
    props = {}
    return render(request, 'cat3.html', props)


class MovieTypeView(generic.ListView):
    model = MovieType
    #context_object_name = 'movietype_list'
    #queryset = MovieType.abjects.all()





