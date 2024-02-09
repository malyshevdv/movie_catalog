import tempfile

from ..forms import LoadMoviesFromFile, ActionForm

from django.shortcuts import render
from django.http import HttpResponseRedirect

from ..dataprocessor import loadOneMovieUrl, HandleActionForm

def loadFile(f, movietype):
    res = ''

    mylist = []
    mylist.append(f'HI!!!')
    mylist.append(f'Content-type: {f.content_type}')
    mylist.append(f'size: {f.size}')
    mylist.append(f'name: {f.name}')
    mylist.append(f'content_type_extra: {f.content_type_extra}')
    #mylist.append(f'temporary_file_path: {f.temporary_file_path()}')

    mylines = []
    with tempfile.NamedTemporaryFile(mode='wb+', delete=False) as file:
        for chunk in f.chunks():
            file.write(chunk)
        file.close()

        with open(file.name, mode='r') as file2:
            mylines = file2.readlines()

    res_founded = 0
    res_unfounded = 0

    #AllMovies = Movie.objects.all()

    for item in mylines:
        mystr = item
        if mystr[-1] == '\n':
            mystr = mystr[:-1]

        loadOneMovieUrl(mystr, movietype)



    mylist.append(f'count: {len(mylines)}')
    mylist.append(f'Founded: {res_founded}')
    mylist.append(f'UnFounded: {res_unfounded}')


    res = '; '.join(mylist)
    return res

def reverseInt(myInt):
    newInt = 0
    ost = 0
    devider = 10
    prevdivider = 0

    while myInt < (devider*10):
        ost = myInt % devider

        newInt = newInt * devider + ost

        prevdivider = devider
        devider =  devider * 10


    return newInt






def LoadFromFileView(request):

    print(str(request.method))
    if request.method == 'POST':

        form = LoadMoviesFromFile(request.POST, request.FILES)
        if form.is_valid():
            res = 'dddd'
            print(str(request.FILES))
            res  = loadFile(request.FILES['myFile'], form.cleaned_data['movietype'])

            context = {
                    'res' : res
            }
        else:
            context = {
                'res': 'ERROR: ' + str(form.errors)
            }
        print(context['res'])
        return HttpResponseRedirect('/success/loadfile', context)
        #return HttpResponseRedirect('/success/loadfile', content=context)

    else:
        HandleActionForm(request)

        context = {
            'form' : LoadMoviesFromFile,
            'ActionForm' : ActionForm(),
            #'MovieTypes' : MovieType.objects.all()
        }
        return render(request, 'loadfile.html', context)


def LoadFromFileSuccessView(request):
    context = {}
    return render(request, 'success/fileloaded.html', context=context)
