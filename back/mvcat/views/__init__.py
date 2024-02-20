from .movieviews import MovieByActorListView, MovieByTypeListView, MovieListView, MovieListFilteredView
from .MovieDetailView import MovieDetailView
from .indexviews import Index, SerchView
from .movietypeviews import MovieTypeView
from .actorviews import ActorsListView,ActorDetailView
from .loaddata import LoadMoviesFromFile, LoadFromFileView, LoadFromFileSuccessView
from ..models.Catalogs.Actor.views import actor_list_API, actor_detail_API