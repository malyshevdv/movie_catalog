from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=150)
    birthday = models.DateField(null=True, default='01/01/1970')
    age = models.CharField(max_length=150, default=0)

    def __str__(self):
        return self.name