from django.urls import path, include
from django.conf import urls

from .Catalogs.Actor.views import ActorsListViewAPI, ActorListAPI3
from .Catalogs.Country.views import REST_CountryList

from rest_framework import routers

#from ..models.Catalogs.Actor.serializer import

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'actor', ActorsListViewAPI)
router.register(r'actor/<>', ActorsListViewAPI)


urlpatterns = [
    path('country/', REST_CountryList),   #work
    path('', include(router.urls)),
    path('actor2/', ActorsListViewAPI.as_view(
        {
            'get': 'list',
        })
    ),  # work

    path('actor3/', ActorListAPI3.as_view()),

    #path('actor/', ActorsListViewAPI.as_view()),    #error
#path('actors/<int:id>', actor_detail_API),

]