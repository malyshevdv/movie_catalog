from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from .Actors import Actor
from .MovieType import MovieType
from .Countries import Country
from .Janres import Janres

from datetime import date

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
    auther = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_premier = models.DateField(null=True, blank=True)

    #related fields
    janres = models.ManyToManyField(Janres, through='MovieJanres')


    @property
    def is_published(self):
        """Determines if the book is overdue based on due date and current date."""
        return bool(self.date_premier and date.today() > self.date_premier)

    def __str__(self):
        return f'{self.title}  => {self.url}'

    class Meta:
        # …
        permissions = (("can_mark_returned", "Set book as returned"),)


class MovieCast(models.Model):
    movie = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL)
    actor = models.ForeignKey(Actor, null=True, on_delete=models.SET_NULL)
    rollname = models.CharField(max_length=50, null=True, blank=True)
    salary = models.DecimalField(max_digits=15, decimal_places=0, null=True, default=0)
    stringnimber = models.DecimalField(decimal_places=0, max_digits=4, default=0, null=True)
    class Meta:
        pass


class MovieDirectors(models.Model):
    movie = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL)
    director = models.ForeignKey(Actor, null=True, on_delete=models.SET_NULL)


class MovieCountries(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class MovieJanres(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    janre = models.ForeignKey(Janres, on_delete=models.CASCADE)
