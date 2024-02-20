FROM python:latest

LABEL authors="denis"
LABEL description="movie catalog backend"

ENV DATABASE="MOVIE"

WORKDIR /usr/src/app
COPY . .

RUN ["python","-m","pip", "install", "-r","requarements.txt"]

EXPOSE 8000

#ENTRYPOINT ["top", "-b"]


ENTRYPOINT ["python", "manage.py", "runserver"]
