from _ast import Add

from django.http import JsonResponse, HttpResponse
from django.views import generic
from rest_framework.parsers import JSONParser

from ..models import Actor, Movie, MovieCast, MovieDirectors, MovieCountries
from django.db.models import OuterRef, Subquery
from abc import ABC
from ..forms import SearchActorForm, DeleteSelectedActorForm
from ..dataprocessor import getSelectedActors, addSelectedActor, DeleteSelectedActor
from ..forms  import AddActorToCompareForm

from ..serializers import ActorSerializer
from django.views.decorators.csrf import csrf_exempt

class ActorsListView(generic.ListView):
    model = Actor
    paginate_by = 10


    def get_queryset(self):
        search_name = self.request.GET.get('search_name', '')
        print(f'for quryset => {search_name}')
        if search_name == '':
            return Actor.objects.all()
        else:
            return Actor.objects.filter(name__icontains=search_name)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['SearchExist'] = True
        search_name = self.request.GET.get('search_name','')
        context['SearchForm'] = SearchActorForm(initial={'search_name' : search_name})

        context['SelectedActors'] = getSelectedActors(self.request)
        context['DeleteSelectedActorForm'] = DeleteSelectedActorForm(initial={'FormName': 'DeleteSelectedActorForm'})

        print(f'for context => {search_name}')

        return context



class ActorDetailView(generic.DetailView):
    model = Actor
    template_name = 'mvcat/actor/ActorDetail.html'


    def get_object(self, queryset=None):
        ActorId = self.kwargs['id']
        return Actor.objects.get(id =ActorId )

    def get_context_data(self, **kwargs):
        ActorId = self.kwargs['id']
        print(ActorId)

        context = super().get_context_data(**kwargs)


        if self.request.method == 'POST':
            print("POST")

        else:
            AddId = self.request.GET.get('id')

            FormName = self.request.GET.get('FormName', '')

            if FormName == 'AddActorToCompareForm':
                addSelectedActor(AddId, self.request)
            elif FormName == 'DeleteSelectedActorForm':
                DeleteSelectedActor(self.request.GET.get('ItemId', ''), self.request)

        #context['movies'] = Movie.objects.filter(id in MovieCast.objects.filter(actor = ))
        castst = MovieCast.objects.filter(actor_id = ActorId)
        context['movies'] = Movie.objects.filter(id__in = Subquery(castst.values('movie_id'))).order_by('-year')
        context['actors'] = MovieCast.objects.filter(movie_id__in = Subquery(context['movies'].values('id'))).order_by('stringnimber')
        context['directors'] = MovieDirectors.objects.filter(movie_id__in = Subquery(context['movies'].values('id')))
        context['countries'] = MovieCountries.objects.filter(movie_id__in=Subquery(context['movies'].values('id')))

        context['SelectedActors'] = getSelectedActors(self.request)
        context['DeleteSelectedActorForm'] = DeleteSelectedActorForm(initial={'FormName': 'DeleteSelectedActorForm'})

        context['AddToCompareform'] = AddActorToCompareForm(initial={'id' : int(ActorId), 'FormName' : 'AddActorToCompareForm'})

        print(f"Actors - {len(context['actors'])} ")

        print('Key list ActorDetailView:')
        for key in kwargs:
            print(key)

        return context
@csrf_exempt
def actor_list_API(request):

    if request.method == "GET":
        serializer = ActorSerializer(Actor.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)
        #return {'ddd' : 1}

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ActorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def actor_detail_API(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        actor = Actor.objects.get(id=id)
    except Actor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ActorSerializer(actor)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ActorSerializer(actor, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        actor.delete()
        return HttpResponse(status=204)