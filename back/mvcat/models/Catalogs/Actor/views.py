from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .model import Actor
from .serializer import ActorSerializer


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