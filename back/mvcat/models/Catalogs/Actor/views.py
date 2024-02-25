from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet
from rest_framework import pagination
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import generics

from .model import Actor
from .serializer import ActorSerializer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'

class ActorListAPI3(generics.ListAPIView):
    serializer_class = ActorSerializer
    pagination_class = CustomPagination
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        search_name = self.request.query_params.get('name')
        print(search_name)
        res = Actor.objects.all()
        if search_name != None:
           res = res.filter(name__icontains=search_name)
           print('My filter')
        return res


class ActorsListViewAPI(ModelViewSet):
    serializer_class = ActorSerializer
    pagination_class = CustomPagination

    #search_name = ModelViewSet.request.query_params.get("name")
    res = Actor.objects.all()
    #if search_name != None:
    #    res.filter(name__icontains=search_name)
    queryset = res

    #queryset = Actor.objects.all()

    #filter_backends = (filters.DjangoFilterBackend,)
    #filter_fields = ('name')
    #lookup_field =

    def get_object(self):
        return get_object_or_404(Actor, id=self.request.query_params.get("id"))

    def get_queryset(self):
        search_name = self.request.query_params.get("name")
        print(search_name)
        res = Actor.objects.all()
        if search_name != None:
            res.filter(name__icontains=search_name)
        self.queryset = res
        return res

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


#@csrf_exempt
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

#@csrf_exempt
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


