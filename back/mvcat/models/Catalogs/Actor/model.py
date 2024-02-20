from django.db import models
from django.core.exceptions import ValidationError
from  ..Country.model import Country


class Actor(models.Model):
    name = models.CharField(max_length=150)
    birthday = models.DateField(null=True, blank=True)
    age = models.CharField(max_length=150, default=0)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name



