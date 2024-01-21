from django.shortcuts import render
from .models import Movie, MovieType, Actor
from django.views import generic
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Index(request):

    movieCount = Movie.objects.all().count()



    myList = ['1','2','3','4','5']

    intercount = request.session.get('intercount', 0)
    request.session['intercount'] = intercount + 1

    props = {
        'movieCount' : movieCount,
        'movieType' : list(MovieType.objects.all()),
        'myName' : "Denis Malyshev",
        'movieType2': myList,
        'intercount' : request.session.get('intercount', 0)
    }



    return render(request, 'cat.html', context = props)


class MovieTypeView(generic.ListView):
    model = MovieType
    #context_object_name = 'movietype_list'
    #queryset = MovieType.abjects.all()

class ActorsView(generic.ListView):
    model = Actor

    def get_queryset(self):
        return  Actor.objects.all()


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
        context['actors'] = Actor.objects.all()
        return context

class MovieDetailView(generic.DetailView):
    model = Movie
    #context_object_name = 'item2'
    template_name = 'mvcat/movies/moviecard.html'
    queryset = Movie.objects.all()



    def get_object(self):
        return Movie.objects.get(id = self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = Movie.objects.get(id = self.kwargs['id'])

        #context['ppp'] = self.kwargs['ppp']

        #we need to describe all items of context


        return context





def Cat2(request):
    props = {}
    return render(request, 'cat2.html', context=props)

def Cat3(request):
    props = {}
    return render(request, 'cat3.html', props)

