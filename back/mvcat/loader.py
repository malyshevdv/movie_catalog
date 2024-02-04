import requests
from requests_html import HTMLSession
#from requests import Session as HTMLSession
#from site-packages import

import lxml
from lxml import etree
from html.parser import HTMLParser
#from .models import *

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#dd = Movie.ob

statTypes = ('')


adress_domen = 'https://191223.lordfilm4.black/'





class MovieType:
    def __init__(self, adress_films : str, filename : str = ''):
        self.adress_films = adress_films
        if filename == '':
            self.filename = adress_films + '.txt'
        else:
            self.filename = filename + '.txt'
        self.name = filename

    def __str__(self):
        return self.name

class MovieTypes:
    def __init__(self):
        self.films = MovieType('films','films.txt')
        self.anime = MovieType('ultfilmy/anime-filmy', 'films.txt')
        self.serialy= MovieType('serialy','serialy.txt')
        self.multserialy= MovieType('serialy/multserialy','multserialy.txt')
        self.multfilmy= MovieType('multfilmy','multfilmy.txt')
        self.foreinmultfilmy= MovieType('multfilmy/zarubezhnye-multiki', 'foreinmultfilmy.txt')

adress_films = 'films/'
#adress_films = 'multfilmy/anime-filmy'
filename = 'amine'
adress_page = 'page/'

AllTypes =  MovieTypes();

#site0 = 'https://191223.lordfilm4.black/films/'
#site1 = 'https://191223.lordfilm4.black/films/page/2/'




def loadFilmsType(ob : MovieType):

    movielist = []

    session = HTMLSession()

    pageLink = f'{adress_domen}{ob.adress_films}/'
    res = session.get(pageLink)
    films = res.html.find('.th-item', first=False)


    for item in films:
        absolute_links = item.absolute_links.pop()
        movie_text  = item.text
        print(f'{movie_text}    {absolute_links} ')
        movielist.append(absolute_links)

    navigation_list = res.html.find('.navigation', first=False)
    maxPages = 0
    for i in navigation_list:
        if i.text.find('...')>=0:
            spl = i.text.split('...')
            maxPages = int(spl[1])
        else:
            spl = i.text.split(' ')
            maxPages = int(spl[-1])

    print(f'Max {maxPages} pages')

    for i in range(2, maxPages+1):
        print(f'Page {i}')
        pageLink = f'{adress_domen}{ob.adress_films}/{adress_page}{i}/'
        res = session.get(pageLink)
        films = res.html.find('.th-item', first=False)

        for item in films:
            absolute_links = item.absolute_links.pop()
            movie_text = item.text
            print(f'{movie_text}    {absolute_links} ')
            movielist.append(absolute_links)

    with open(f'{ob.filename}', mode='w') as file:
        file.writelines('\n'.join(movielist))

    print('The END')


class Movie3:
    def __init__(self):
        self.actors = []
        self.date_premier = ''
        self.janres = []
        self.agelimitation = ''
        self.title = ''
        self.titleRu = ''

        self.year = ''
        self.directors = []
        self.countries = []
        self.date_add = ''
        self.quality = ''

        self.description = ''
        self.descriptionHTML = ''
        self.url = ''
        self.imdb = ''
        self.poster = ''
    def __str__(self):

        res = 'OBJECT STRUCTURE\n'
        print(dir(self))
        for MyItem in dir(self):
            if MyItem[0:1] != '_':
                res += f'{MyItem} : {self.__getattribute__(MyItem)}\n'
        return res


def loadFilmInfo(sampleAddress = 'https://191223.lordfilm4.black/7302-serial-hanna-2019.html'):
    session = HTMLSession()
    res = session.get(sampleAddress)

    myMovie = Movie3()

    films = res.html.find('.fdesc', first=False)
    for item in films:
        myMovie.description = item.text
        myMovie.descriptionHTML = item.html

    films = res.html.find('.speedbar', first=True)
    films2 = films.find('span')
    if len(films2)>=1:
        tt = str(films2[0].text).split('»')
        myMovie.titleRu = tt[-1]
    myMovie.url = films2[0].url

    #poster
    films = res.html.find('.fposter.img-wide', first=True)
    films2 = films.find('img')
    if len(films2) >= 1:
       myMovie.poster = films2[0].attrs['data-src']


    #players
    films = res.html.find('video', first=False)
    for item in films:
        dd = 0

    #open('', mode='', )


    films = res.html.find('.flist', first=False)
    for item in films:
        dd = item.full_text.split('\n')
        for item in dd :
            res = str(item).split(':')
            if len(res)>1:
                if res[0] == 'Актеры':
                    myMovie.actors = res[1].split(',')
                elif res[0] == 'Жанр':
                    myMovie.janres = res[1].split(',')
                elif res[0] == 'Премьера':
                    myMovie.date_premier = res[1]
                elif res[0] == 'Возрастное ограничение':
                    myMovie.agelimitation = res[1]

                elif res[0] == 'Оригинальное название':
                    myMovie.title = res[1]
                elif res[0] == 'Год выхода':
                    myMovie.year = res[1]
                elif res[0] == 'Режиссер':
                    myMovie.directors = res[1].split(',')
                elif res[0] == 'Страна':
                    myMovie.countries = res[1].split(',')

                elif res[0] == 'Добавлено (обновлено)':
                    myMovie.date_add = res[1]
                elif res[0] == 'Качество':
                    myMovie.quality = res[1]
                    myMovie.imdb = dd[4]

        print(dd)

 #   films = res.html.find('.fdesc', first=False)


    print('dd')
    return myMovie;


def loadInfo(address='https://191223.lordfilm4.black/7302-serial-hanna-2019.html'):
    res = loadFilmInfo(address)

    if res.title != '':
        print(res.title)

    return res
def fileLoader(fileName):
    res = []
    with open(fileName, mode='r') as file:
        return file.readlines()


