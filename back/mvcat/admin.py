from django.contrib import admin
from .models import Actor, Movie, MovieCast

# Register your models here.

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


class movieCastInlineTab(admin.TabularInline):
    model = MovieCast


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [movieCastInlineTab]

