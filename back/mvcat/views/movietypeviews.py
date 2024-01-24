from ..models import MovieType
from django.views import generic
class MovieTypeView(generic.ListView):
    model = MovieType
    #context_object_name = 'movietype_list'
    #queryset = MovieType.abjects.all()
