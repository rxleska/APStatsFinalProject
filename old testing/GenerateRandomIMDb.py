import random

from sqlalchemy import null
import collect


def getRandomMovie():
    isMovie = False
    movieSoup = None
    while(isMovie == False):
        num = random.randint(999999, 99999999)
        movieSoup = collect.getRequest(num.__str__())
        isMovie = collect.isMovie(movieSoup)
    return movieSoup


def generateEntry():
    ex = getRandomMovie()
    dictElement = {"title": collect.getTitle(ex), "rating": collect.getRating(
        ex), "runtime": collect.getRunTime(ex)}
    return dictElement


print(generateEntry().__str__())
