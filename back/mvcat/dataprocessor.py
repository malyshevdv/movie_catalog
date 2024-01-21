from back.mvcat.models.Movies import *

def loadInfo(address = 'https://191223.lordfilm4.black/7302-serial-hanna-2019.html'):
    pass

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





