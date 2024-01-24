from django.shortcuts import render
from ..models import Movie, MovieType
from ..forms import MyForm, ActorForm

def Index(request):

    movieCount = Movie.objects.all().count()



    myList = ['1','2','3','4','5']

    intercount = request.session.get('intercount', 0)
    request.session['intercount'] = intercount + 1

    props = {
        'movieCount' : movieCount,
        'movieType' : list(MovieType.objects.all()),
        'myName' : "Denis Malyshev",
        'movieType2': myList,
        'intercount' : request.session.get('intercount', 0),
        'form' : MyForm,
        'actorform': ActorForm,


    }



    return render(request, 'cat.html', context = props)
