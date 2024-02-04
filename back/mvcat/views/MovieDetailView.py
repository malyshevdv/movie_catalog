from django.views import generic
from ..models import Movie, MovieType, Actor, MovieCountries, MovieCast, MovieDirectors, MovieJanres
from django.http import HttpResponseRedirect
from ..forms import ActionForm
from ..dataprocessor import HandleActionForm

class MovieDetailView(generic.DetailView):
    model = Movie
    #context_object_name = 'item2'
    template_name = 'mvcat/movies/moviecard.html'
    queryset = Movie.objects.all()



    def get_object(self):
        return Movie.objects.get(id = self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print(self.request)


        if self.request.method == "POST":
            pass
            #return HttpResponseRedirect(reverse('all-borrowed'))
        elif self.request.method == "GET":

            HandleActionForm(self.request)

            myId = self.kwargs['id']
            context['item'] = Movie.objects.get(id = myId)

            context['countries'] = MovieCountries.objects.filter(movie = myId)
            context['actors'] = MovieCast.objects.filter(movie=myId)
            context['directors'] = MovieDirectors.objects.filter(movie=myId)

            context['directors'] = MovieDirectors.objects.filter(movie=myId)
            context['janres'] = MovieJanres.objects.filter(movie=myId)

            context['UpdateMoviedataForm'] = MovieDirectors.objects.filter(movie=myId)

            context['ActionForm'] = ActionForm()

        return context