from django.shortcuts import render
from ..models import Movie, MovieType, Actor, MovieCountries, MovieCast, MovieDirectors
from django.views import generic
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

# Create your views here.
class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 20

class MovieByActorListView(generic.ListView):
    #template_name =
    model = Movie

    def get_queryset(self):
        self.actor = get_object_or_404(Actor, name = self.kwargs['actor'] )
        #return Movie.objects.filter()

class MovieByTypeListView(generic.ListView):
    template_name = 'movies/moviesbytype.html'
    paginate_by = 20


    def get_queryset(self):
       self.type2 = get_object_or_404(MovieType, id = self.kwargs['type'])
       return Movie.objects.filter(type = self.type2)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movietype'] = self.type2
        return context

class MovieDetailView(generic.DetailView):
    model = Movie
    #context_object_name = 'item2'
    template_name = 'mvcat/movies/moviecard.html'
    queryset = Movie.objects.all()



    def get_object(self):
        return Movie.objects.get(id = self.kwargs['id'])

    def get_context_data(self, **kwargs):
        myId = self.kwargs['id']
        context = super().get_context_data(**kwargs)
        context['item'] = Movie.objects.get(id = myId)

        context['countries'] = MovieCountries.objects.filter(movie = myId)
        context['actors'] = MovieCast.objects.filter(movie=myId)
        context['directors'] = MovieDirectors.objects.filter(movie=myId)

        #context['ppp'] = self.kwargs['ppp']

        #we need to describe all items of context


        return context






