from django.urls import path, include
from .Country.views import REST_CountryList, REST_CountryDetail

urlpatterns = [
    path('country/<int:id>', REST_CountryDetail),
    path('country/', REST_CountryList),
    ]
