from django.contrib import admin
from django.urls import path, include
from .views import Index, Cat2, Cat3, MovieTypeView


urlpatterns = [
    path('', Index, name ='home'),
    path('cat2/', Cat2, name ='cat2'),
    path('cat3/', Cat3, name ='cat3'),

    path('movietype/', MovieTypeView.as_view()),

]
