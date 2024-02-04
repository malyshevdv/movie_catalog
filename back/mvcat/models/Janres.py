from django.db import models

class Janres(models.Model):
    name = models.CharField(max_length=50, null=True, default="")
    nameRu = models.CharField(max_length=50, null=True, default="")
    picturePath = models.CharField(max_length=150, null=True, default="")
    def __str__(self):
        return self.name