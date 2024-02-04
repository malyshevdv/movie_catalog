from django.db import models
from django.core.exceptions import ValidationError

from ..models.Countries import Country


def validate_name(name:str):
    print(name)
    if name.find('Santa') >= 0:
        print('ERROR')
        raise ValidationError("ERROR", params={'value' : name})
    else:
        print(name.find('Santa'))


class Actor(models.Model):
    name = models.CharField(max_length=150, validators=[validate_name])
    birthday = models.DateField(null=True, blank=True)
    age = models.CharField(max_length=150, default=0)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name