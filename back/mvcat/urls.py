from django.urls import path, include
from .views import Index, MovieTypeView, ActorsListView, ActorDetailView, SerchView,\
    MovieListView, MovieByTypeListView, \
    MovieByActorListView, MovieDetailView, \
    LoadFromFileView, LoadFromFileSuccessView, MovieListFilteredView

from .models.Catalogs.Country.views import REST_CountryList


urlpatterns = [
    path('', Index, name ='home'),
   # path('cat2/', Cat2, name ='cat2'),
   # path('cat3/', Cat3, name ='cat3'),

    path('movietype/', MovieTypeView.as_view()),

    path('movies/', MovieListView.as_view()),
    path('moviesfiltered/', MovieListFilteredView),

    path('movies/type/<int:type>', MovieByTypeListView.as_view()),
    path('movies/actor/<actor_id>', MovieByActorListView.as_view()),

    path('movie/<int:id>', MovieDetailView.as_view(), name= 'item' ),

    path('actors/', ActorsListView.as_view()),
    path('actor/<int:id>', ActorDetailView.as_view()),

    path('load/', LoadFromFileView, name='load-file'),

    path('success/loadfile/', LoadFromFileSuccessView),

    path('search/', SerchView ),

    #API

    path('count/', REST_CountryList),
    path('api/catalogs/', include('mvcat.models.urls_API')),

]
