from django.urls import path, include

urlpatterns = [
    path('catalogs/', include('mvcat.models.Catalogs.urls')),

]