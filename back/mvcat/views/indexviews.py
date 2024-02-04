from django.shortcuts import render, HttpResponseRedirect
from ..models import Movie, MovieType
from ..forms import MyForm, ActorForm, SearchForm, DeleteSelectedActorForm
from ..dataprocessor import getSelectedActors

def Index(request):

    movieCount = Movie.objects.all().count()



    myList = ['1','2','3','4','5']

    intercount = request.session.get('intercount', 0)
    request.session['intercount'] = intercount + 1

    context = {
        'movieCount' : movieCount,
        'movieType' : list(MovieType.objects.all()),
        'myName' : "Denis Malyshev",
        'movieType2': myList,
        'intercount' : request.session.get('intercount', 0),
        'form' : MyForm,
        'SearchExist': False,
        'SearchForm' : SearchForm,
        'actorform': ActorForm,
        'DeleteSelectedActorForm' : DeleteSelectedActorForm,

    }
    context['SelectedActors'] = getSelectedActors(request)

    return render(request, 'cat.html', context = context)





def SerchView(request, *args, **kwargs):


    if request.method == 'POST':
        print('POST arguments')
        for key in args:
            print(key)
        for key in kwargs:
            print(key)

        form = SearchForm(request.POST)
        for key in form:
            print(str(key))
        #print(form.cleaned_data['searchstring'])


        return HttpResponseRedirect('/')

    else:
        cont = {}

        return render(request, '', context=cont)




