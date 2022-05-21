import math
import tmdbsimple as tmdb
import config
import random
import time
from multiprocessing import Pool
api_key = config.API_KEY

tmdb.API_KEY = api_key


def getData(id):
    """
    Gets the Title Rating and Runtime of a movie from its id on the movie database\n
    parameter : id : TMDb id
    """
    movie = tmdb.Movies(id)
    response = movie.info()
    if response['vote_average'] == 0.0 or response['runtime'] < 30 or response['vote_count'] < 100:
        return None
    return movie.title.replace("~", "") + "~" + response['vote_average'].__str__().replace("~", "") + "~" + response['runtime'].__str__().replace("~", "")


def getRandomMovie():
    """
    Attempts random movie id calls until one doesn't return 404
    """
    while True:
        try:
            x = getData(random.randint(1, 700000))
            if x == None:
                continue
            else:
                return x
            break
        except:
            continue


def addAMovie():
    """
    Adds a single movie's data to output.txt
    """
    with open('output.txt', "a", encoding="utf-8") as file:
        file.write(getRandomMovie().__str__() + "\n")
        file.close()


def addNMovies(n):
    """
    Collects data on a number of movies then adds data to output.txt\n
    parameter : n : number of movies to add data from
    """
    data = ""
    for i in range(0, n):
        data = data + "\n" + getRandomMovie()
    with open('output.txt', "a", encoding="utf-8") as file:
        file.write(data)
        file.close()


def add10Movies(n):
    """
    Adds 50 movies to output.txt\n
    parameter : n : current process number
    """
    print(f"start process:{n}")
    addNMovies(10)
    print(f"end process:{n}")


def add50Movies(n):
    """
    Adds 50 movies to output.txt\n
    parameter : n : current process number
    """
    print(f"start process:{n}")
    addNMovies(50)
    print(f"end process:{n}")

#############################################################################
############# Change the value below then run to get your data ##############
#############################################################################


# Change This to the number of movies to collect data on
numberOfMoviesToCollectDataOn = 50


processes = math.ceil((numberOfMoviesToCollectDataOn*1.0)/50.0)


if __name__ == '__main__':
    starttime = time.time()
    pool = Pool()
    pool.map(add50Movies, range(processes))
    pool.close()
    endtime = time.time()
    print(f"Time taken {endtime-starttime} seconds")
