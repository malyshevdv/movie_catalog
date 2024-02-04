from ..dataprocessor import getSelectedActors, DeleteSelectedActor
from ..forms import DeleteSelectedActorForm
from ..models import MovieType
from django.views import generic
class MovieTypeView(generic.ListView):
    model = MovieType
    #context_object_name = 'movietype_list'
    #queryset = MovieType.abjects.all()
    def get_context_data(self, **kwargs):

        FormName = self.request.GET.get('FormName', '')

        if FormName == 'DeleteSelectedActorForm':
            DeleteSelectedActor(self.request.GET.get('ItemId', ''), self.request)

        context = super().get_context_data(**kwargs)
        context['SelectedActors'] = getSelectedActors(self.request)
        context['DeleteSelectedActorForm'] = DeleteSelectedActorForm(initial={'FormName': 'DeleteSelectedActorForm'})

        return context
