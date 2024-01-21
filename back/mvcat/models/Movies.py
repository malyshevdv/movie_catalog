from django.db import models
from Actors import Actor
from MovieType import MovieType

# Create your models here.






class Movie(models.Model):
    url = models.CharField(max_length=250, null=True)
    type = models.ForeignKey(MovieType, null=True, blank=True, on_delete=models.SET_NULL)

    title = models.CharField(max_length=150, null=True, blank=True)
    titleRu = models.CharField(max_length=150, null=True, blank=True)
    agelimitation = models.CharField(max_length=50, null=True, blank=True)

    year = models.DecimalField(max_digits=4, decimal_places=0, default=0, blank=True)
    date_added = models.DateField(null=True, blank=True)
    quality = models.CharField(max_length=50, null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    descriptionHTML = models.TextField(null=True, blank=True)

    imdb = models.CharField(max_length=15, null=True, blank=True)
    poster = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.title}  => {self.url}'




class MovieCast(models.Model):
    movie = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL)
    actor = models.ForeignKey(Actor, null=True, on_delete=models.SET_NULL)
    rollname = models.CharField(max_length=50, null=True, blank=True)
    salary = models.DecimalField(max_digits=15, decimal_places=0, null=True)


class MovieDirectors(models.Model):
    movie = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL)
    director = models.ForeignKey(Actor, null=True, on_delete=models.SET_NULL)


class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class MovieCountries(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

