from django.views import generic
from ..models import Actor, Movie, MovieCast, MovieDirectors, MovieCountries
from django.db.models import OuterRef, Subquery

class ActorsListView(generic.ListView):
    model = Actor
    paginate_by = 40

    def get_queryset(self):
        return  Actor.objects.all()

class ActorDetailView(generic.DetailView):
    model = Actor
    template_name = 'mvcat/actor/ActorDetail.html'
    def get_object(self, queryset=None):
        return Actor.objects.get(id = self.kwargs['id'])

    def get_context_data(self, **kwargs):
        ActorId = self.kwargs['id']
        print(ActorId)

        context = super().get_context_data(**kwargs)

        #context['movies'] = Movie.objects.filter(id in MovieCast.objects.filter(actor = ))
        castst = MovieCast.objects.filter(actor_id = ActorId)
        context['movies'] = Movie.objects.filter(id__in = Subquery(castst.values('movie_id'))).order_by('-year')
        context['actors'] = MovieCast.objects.filter(movie_id__in = Subquery(context['movies'].values('id'))).order_by('stringnimber')
        context['directors'] = MovieDirectors.objects.filter(movie_id__in = Subquery(context['movies'].values('id')))
        context['countries'] = MovieCountries.objects.filter(movie_id__in=Subquery(context['movies'].values('id')))

        print(f"Actors - {len(context['actors'])} ")
        return context