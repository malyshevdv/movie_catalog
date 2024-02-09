from .models import Movie, MovieType, Actor, MovieCast, MovieCountries, MovieDirectors, Country, Janres, MovieJanres
from .loader import loadFilmInfo
from django.core import exceptions

def HandleActionForm(request):

    if request.method == 'GET':
        FormName = request.GET.get('FormName','')

        if FormName == 'ActionForm':
            Action = request.GET.get('Action', '')

            match Action:
                case 'UpdateMovieData':
                    MyId = request.GET.get('MyId',0)
                    print(f'Update movie {MyId}')
                    MyMovie = Movie.objects.get(id=MyId)

                    print(MyMovie.url)
                    if MyMovie.url != '':
                        UpdateOneMovie(MyMovie)



                case 'AddActorToList':
                    id = request.GET.get('MyId',0)
                    print(f'Add actor {id}')

                case 'RemoveActorFromList':
                    id = request.GET.get('MyId', 0)
                    print(f'Remove actor {id}')

                case 'UpdateAllLinks':
                    print('START LOADING...')
                    StartUpdateAll()
                    print('FINISHED.')

    elif request.method == 'POST':
        pass


def StartUpdateAll():
    myset = Movie.objects.all().filter(title__exact=None)
    totalLength = len(myset)

    for ind,MyMovie in enumerate(myset):
        try:
            UpdateOneMovie(MyMovie)
            print(f'<  {ind}   {MyMovie.title}> => {MyMovie}')
        except:
            print(MyMovie.url)
    print()





def UpdateOneMovie(MyMovie):

    MyMovieStructure = loadFilmInfo(MyMovie.url)
    print(MyMovieStructure)

    if MyMovie.title != MyMovieStructure.title:
        MyMovie.title = MyMovieStructure.title

    if MyMovie.titleRu != MyMovieStructure.titleRu:
        MyMovie.titleRu = MyMovieStructure.titleRu

    pref = 'https://'
    if MyMovieStructure.url[0:8] == pref:
        newPoster = ''.join([pref, MyMovieStructure.url[8:].split('/')[0], MyMovieStructure.poster])
        if MyMovie.poster != newPoster:
            MyMovie.poster = newPoster
            print(newPoster)

    if MyMovie.year != MyMovieStructure.year:
        MyMovie.year = MyMovieStructure.year

    if MyMovie.description != MyMovieStructure.description:
        MyMovie.description = MyMovieStructure.description

    if MyMovie.agelimitation != MyMovieStructure.agelimitation:
        MyMovie.agelimitation = MyMovieStructure.agelimitation

    #if MyMovie.date_added != MyMovieStructure.date_add:
    #    MyMovie.date_added = MyMovieStructure.date_add

    #if MyMovie.date_premier != MyMovieStructure.date_premier:
    #    MyMovie.date_premier = MyMovieStructure.date_premier

    if MyMovie.descriptionHTML != MyMovieStructure.descriptionHTML:
        MyMovie.descriptionHTML = MyMovieStructure.descriptionHTML

    if MyMovie.imdb != MyMovieStructure.imdb:
        MyMovie.imdb = MyMovieStructure.imdb

    if MyMovie.quality != MyMovieStructure.quality:
        MyMovie.quality = MyMovieStructure.quality

    #Actors
    for ind,item in enumerate(MyMovieStructure.actors):
        Actorname = item.strip()
        try:
            ActorItem = Actor.objects.get(name = Actorname)
            print(f'Find actror {Actorname} => <{ActorItem}>')
        except exceptions.ObjectDoesNotExist:
            print(f'Does not find {Actorname}>')
            ActorItem = Actor.objects.create(name = Actorname)
            ActorItem.save()
            print(f'  saved actror {Actorname} => <{ActorItem}>')

        try:
            MyCast = MovieCast.objects.get(movie = MyMovie, actor = ActorItem)
            print(f'Find cast {ActorItem}')
        except exceptions.ObjectDoesNotExist:
            print(f'Does not find cast {ActorItem}>')
            NewCast = MovieCast.objects.create(movie=MyMovie, actor=ActorItem, stringnimber=(ind+1))
            NewCast.save()

    #Directors
    for item in MyMovieStructure.directors:
        Actorname = item.strip()
        try:
            ActorItem = Actor.objects.get(name = Actorname)
            #print(f'Find actror {Actorname} => <{ActorItem}>')
        except exceptions.ObjectDoesNotExist:
            print(f'Does not find {Actorname}>')
            ActorItem = Actor.objects.create(name = Actorname)
            ActorItem.save()
            print(f'  saved actror {Actorname} => <{ActorItem}>')

        try:
            MyCast = MovieDirectors.objects.get(movie = MyMovie, director = ActorItem)
            #print(f'Find cast {ActorItem}')
        except exceptions.ObjectDoesNotExist:
            print(f'Does not find cast {ActorItem}>')
            NewCast = MovieDirectors.objects.create(movie=MyMovie, director=ActorItem)
            NewCast.save()

    #Country
    for item in MyMovieStructure.countries:
        Actorname = item.strip()
        try:
            ActorItem = Country.objects.get(name=Actorname)

        except exceptions.ObjectDoesNotExist:
            print(f'Does not find {Actorname}>')
            ActorItem = Country.objects.create(name=Actorname)
            ActorItem.save()
            print(f'  saved Country {Actorname} => <{ActorItem}>')

        try:
            MyCast = MovieCountries.objects.get(movie=MyMovie, country=ActorItem)
            # print(f'Find cast {ActorItem}')
        except exceptions.ObjectDoesNotExist:
            print(f'Does not find country {ActorItem}>')
            NewCast = MovieCountries.objects.create(movie=MyMovie, country=ActorItem)
            NewCast.save()

    #janres
    for item in MyMovieStructure.janres:
        Actorname = item.strip()
        try:
            ActorItem = Janres.objects.get(nameRu=Actorname)

        except exceptions.ObjectDoesNotExist:
            print(f'Does not find janre {Actorname}>')
            ActorItem = Janres.objects.create(name=Actorname, nameRu=Actorname)
            ActorItem.save()
            print(f'  saved jonre {Actorname} => <{ActorItem}>')

        try:
            MyCast = MovieJanres.objects.get(movie=MyMovie, janre=ActorItem)
            # print(f'Find cast {ActorItem}')
        except exceptions.ObjectDoesNotExist:
            print(f'Does not find country {ActorItem}>')
            NewCast = MovieJanres.objects.create(movie=MyMovie, janre=ActorItem)
            NewCast.save()






    MyMovie.save()






def HandleDate(request):
    pass





def loadInfo(address = 'https://191223.lordfilm4.black/7302-serial-hanna-2019.html'):
    pass


def DeleteSelectedActor(id, request):

    if id == '' or id ==None:
        return
    print(f'Try to delete {id}')
    SelectedActorsId = getSelectedActorsId(request)

    NewList = [item for item in SelectedActorsId if item != str(id)]
    request.session['SelectedActorsId'] = ','.join(NewList)
    print(f'Result list {NewList}')

def addSelectedActor(MtId, request):
    print(f'ins {MtId}')
    if MtId == '' or MtId ==None:
        return
    if isinstance(MtId, int):
        MtId = str()
    #myList = []
    SelectedActorsId = getSelectedActorsId(request)
    #SelectedActorsId = []
    if MtId not in SelectedActorsId:
        print(f'Try to add <{MtId}> to {SelectedActorsId}')
        #myList.append(MtId)
        SelectedActorsId.append(str(MtId))
        myStr = ','.join(SelectedActorsId)
        request.session['SelectedActorsId'] = myStr
        print(f'Added {MtId}')

def getSelectedActorsId(request):

    SelectedActorsId = request.session.get('SelectedActorsId', '').split(',')
    res = [item for item in SelectedActorsId if item !='']
    return  res


def getSelectedActors(request):

    SelectedActorsId = getSelectedActorsId(request)
    print(f'Our string = {SelectedActorsId}')
   #SelectedActorsId = [3,5,6]
    print(f'Our string = {SelectedActorsId}')

    SelectedActors = []
    for item in SelectedActorsId:
        print(f'--> {item}   {type(item)}')
        if item != '':
            SelectedActors.append(Actor.objects.get(id = item))
    return SelectedActors

def ClearUrls():
    for item in Movie.objects.all():
        mystr= item.url
        if mystr[-1] == '\n':
            item.url = mystr[0:-1]
            item.save()
            print('Corrected ' + item.url)




def loadOneMovieUrl(url, movietype):
    #ClearUrls()

    #print(movietype)
    try:
        exist = Movie.objects.get(url=url)
    except Movie.DoesNotExist:
        newMovie = Movie()
        newMovie.url = url
        newMovie.type = movietype
        newMovie.save()
        print(f'Loaded {newMovie.type} = {newMovie.url}')

def fileLoader(fileName, typestr, loadFile = False):
    res = None
    with open(fileName, mode='r') as file:
        res = file.readlines()


    myType = MovieType.objects.get(name = typestr)
    if myType != None and res != None:
        for myStr in res:
            if loadFile:

                try:
                    exist = Movie.objects.get(url=myStr)

                    if exist !=None:
                        newMovie = Movie()
                        newMovie.url = myStr
                        newMovie.type = myType
                        newMovie.save()
                        print(f'Loaded {newMovie.type} = {newMovie.url}')
                    else:
                        print(f'skiped {myType} = {myStr}')

                except:
                    print(f'ERROR {myStr}')


            else:
                print(myStr)
    else:
        print('Something wrong')





