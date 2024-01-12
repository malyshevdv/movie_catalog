from django.db import models


# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=150)
    birthday = models.DateField(null=True, default='01/01/1970')
    age = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Movie(models.Model):
    url = models.CharField(max_length=150, null=True)

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
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    rollname = models.CharField(max_length=50, null=True, blank=True)
