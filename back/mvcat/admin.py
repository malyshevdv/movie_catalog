from django.contrib import admin
from .models import Actor, Movie

# Register your models here.

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

