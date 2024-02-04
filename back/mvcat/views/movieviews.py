from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import OuterRef, Subquery, Count
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from ..models import Movie, MovieType, Actor, MovieCountries, MovieCast, MovieDirectors
from ..dataprocessor import getSelectedActors, getSelectedActorsId, DeleteSelectedActor
from ..forms import SearchMovieForm, DeleteSelectedActorForm
from ..tasks import firsttask


# Create your views here.
class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 20

    #print('FIRST TASK')
    #firsttask(1,3)
    #sampletask()


    def get_queryset(self):

        search_title = self.request.GET.get('search_title', '')
        search_year = self.request.GET.get('search_year', '')
        search_country = self.request.GET.get('search_country', '')
        search_description = self.request.GET.get('search_description', '')

        search_actor = self.request.GET.get('search_actor', '')
        search_actor_list = self.request.GET.get('search_actor_list', '')
        search_actor_colaboration = self.request.GET.get('search_actor_colaboration', '')
        search_have_poster = self.request.GET.get('search_have_poster', '')

        print(f'POSTER={search_have_poster}')

        myDataset = Movie.objects.all()

        if search_title:
            myDataset = myDataset.filter(title__icontains=search_title)

        if search_year:
            myDataset = myDataset.filter(year = int('0' + search_year))

        if search_description:
            myDataset = myDataset.filter(description__icontains=search_description)

        if search_country:
            MoviesFromCountry = MovieCountries.objects.filter(country__name__icontains= search_country)
            myDataset = myDataset.filter(id__in = Subquery(MoviesFromCountry.values('movie_id')))

        if search_actor:
            MoviesCust = MovieCast.objects.filter(actor__name__icontains=search_actor)
            myDataset = myDataset.filter(id__in=Subquery(MoviesCust.values('movie_id')))


        if search_actor_list:
            SelectedActorsId = getSelectedActorsId(self.request)
            MoviesCust = MovieCast.objects.filter(actor__id__in=SelectedActorsId)
            myDataset = myDataset.filter(id__in=Subquery(MoviesCust.values('movie_id')))

        if search_actor_list and search_actor_colaboration:
            SelectedActorsId = getSelectedActorsId(self.request)
            MoviesCust = MovieCast.objects.filter(actor__id__in=SelectedActorsId)
            MoviesCust2 = MoviesCust.values('movie_id').annotate(countactors = Count('actor_id')).filter(countactors=len(SelectedActorsId))
            myDataset = myDataset.filter(id__in=Subquery(MoviesCust2.values('movie_id')))

        if search_have_poster:
            myDataset = myDataset.filter(poster__icontains='http')

        return myDataset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        FormName = self.request.GET.get('FormName', '')
        if FormName == 'DeleteSelectedActorForm':
            DeleteSelectedActor(self.request.GET.get('ItemId', ''), self.request)

        initsearchset = {
        'search_title' : self.request.GET.get('search_title', ''),
        'search_year' : self.request.GET.get('search_year', ''),
        'search_country' : self.request.GET.get('search_country', ''),
        'search_description': self.request.GET.get('search_description', ''),
        'search_actor': self.request.GET.get('search_actor', ''),
        'search_actor_list': self.request.GET.get('search_actor_list', ''),
        'search_actor_colaboration': self.request.GET.get('search_actor_colaboration', ''),
        'search_have_poster': self.request.GET.get('search_have_poster', ''),
        }

        context['SearchExist'] = True
        context['SearchModel'] = 'Movie'
        context['SearchForm'] = SearchMovieForm(initial=initsearchset)

        context['SelectedActors'] = getSelectedActors(self.request)
        context['DeleteSelectedActorForm'] = DeleteSelectedActorForm(initial={'FormName' : 'DeleteSelectedActorForm'})
        return context

class MovieByActorListView(generic.ListView):
    #template_name =
    model = Movie

    def get_queryset(self):
        self.actor = get_object_or_404(Actor, name = self.kwargs['actor_id'] )
        #return Movie.objects.filter()


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        print('Key list MovieByActorListView:')
        for key in kwargs:
            print(key)

        return context

class MovieByTypeListView(generic.ListView):
    template_name = 'movies/moviesbytype.html'
    paginate_by = 20


    def get_queryset(self):
       self.type2 = get_object_or_404(MovieType, id = self.kwargs['type'])
       return Movie.objects.filter(type = self.type2)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movietype'] = self.type2
        #context['SelectedActors'] = getSelectedActors(self.request)
        #context['DeleteSelectedActorForm'] = DeleteSelectedActorForm(initial={'FormName': 'DeleteSelectedActorForm'})

        return context








