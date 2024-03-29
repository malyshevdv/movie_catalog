from django.contrib import admin
from .models import Actor, Movie, MovieCast, MovieCountries, MovieDirectors, MovieType, Janres, MovieJanres
from .models.Catalogs.Country.model import Country
from .loader import loadFilmInfo

# Register your models here.

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(MovieType)
class MovieTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Janres)
class MovieTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']

class movieCastInlineTab(admin.TabularInline):
    model = MovieCast
    autocomplete_fields = ['actor']
    search_fields = ['name']

class movieDirectorsInlineTab(admin.TabularInline):
    model = MovieDirectors
    autocomplete_fields = ['director']
    search_fields = ['name']

class movieCountryInlineTab(admin.TabularInline):
    model = MovieCountries
    autocomplete_fields = ['country']
    search_fields = ['name']

class movieJanresInlineTab(admin.TabularInline):
    model = MovieJanres
    autocomplete_fields = ['janre']
    search_fields = ['name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display =('title', 'titleRu', 'year', 'is_published', 'url')
    list_filter = ['type', 'title']
    inlines = [movieCastInlineTab, movieDirectorsInlineTab, movieCountryInlineTab, movieJanresInlineTab]
    search_fields = ['title', 'titleRu', 'url']

    actions = ['UpdateInfo']
    @admin.action(description='Update info from site')
    def UpdateInfo(modeladmin, request, queryset):
        for item in queryset:
            dd = loadFilmInfo(item.url)

            print(item)
            print(dd)
