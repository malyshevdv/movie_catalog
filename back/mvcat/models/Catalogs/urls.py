from django.urls import path, include
from .Country.views import REST_CountryList, REST_CountryDetail
from .Actor.views import actor_detail_API, actor_list_API, ActorsListViewAPI

urlpatterns = [
    path('country/<int:id>', REST_CountryDetail),
    path('country/', REST_CountryList),

   # path('actors/', ActorsListViewAPI.as_view),
    path('actors/<int:id>', actor_detail_API),

]
