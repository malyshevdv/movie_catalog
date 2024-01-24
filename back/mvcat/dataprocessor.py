from .models import Movie, MovieType

def loadInfo(address = 'https://191223.lordfilm4.black/7302-serial-hanna-2019.html'):
    pass


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





