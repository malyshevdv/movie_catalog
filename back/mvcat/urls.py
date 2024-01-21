from django.contrib import admin
from django.urls import path, include
from .views import Index, Cat2, Cat3, MovieTypeView, ActorsView, MovieListView, MovieByTypeListView, MovieByActorListView, MovieDetailView


urlpatterns = [
    path('', Index, name ='home'),
    path('cat2/', Cat2, name ='cat2'),
    path('cat3/', Cat3, name ='cat3'),

    path('movietype/', MovieTypeView.as_view()),
    path('actors/', ActorsView.as_view()),
    path('movies/', MovieListView.as_view()),

    path('movies/type/<int:type>', MovieByTypeListView.as_view()),
    path('movies/actor/<actor>', MovieByActorListView.as_view()),

    path('movie/<int:id>', MovieDetailView.as_view(), name= 'item' ),

]
