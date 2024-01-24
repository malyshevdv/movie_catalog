from django.views import generic
from ..models import Actor, Movie, MovieCast

class ActorsListView(generic.ListView):
    model = Actor

    def get_queryset(self):
        return  Actor.objects.all()

class ActorDetailView(generic.DetailView):
    model = Actor
    template_name = 'mvcat/actor/ActorDetail.html'
    def get_object(self, queryset=None):
        return Actor.objects.get(id = self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)

        context['movies'] = MovieCast.objects.filter(actor = self.kwargs['id'])

        return context