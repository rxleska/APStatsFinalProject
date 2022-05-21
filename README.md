# AP Statistics Final Project

### The Goal of this project is to test the indepence of Movie Runtimes and Movie Ratings. Using a Chi<sup>2</sup> Test of Independence

### [**tmdbTest.py**](tmdbTest.py)

A program that creates a list of movie data in the format of TITLE\~Rating\~Runtime

Using the, **_the movie database_ API** 

#### [TMDB API]([https://www.themoviedb.org/](https://developers.themoviedb.org/3/getting-started/introduction)) 
[![TMDB](https://www.themoviedb.org/assets/2/v4/logos/v2/blue_short-8e7b30f73a4020692ccca9c88bafe5dcb6f8a62a4c6bc55cd9ba82bb2cd95f6c.svg)](https://www.themoviedb.org/) 

See [**Example Config**](example_config.py) for how to set up the program
**_Note:_** duplicates can exist in this data so keep that in mind in any usage


This data was then imported into google sheets, after duplicate values were removed, We were left with >10000 entries


### [**googleSheetsFunctions.js**](googleSheetsFunctions.js)

Contains the function GetNumInRange() that is used to create a matrix of the observed num of movies with in ranges based on runtime and rating.


### The Test Results

Using _10055_ datapoints, A Chi<sup>2</sup> Test of independence was ran on the data in intervals of 15 minutes of runtime and 0.5 rating points. (2-9.5) (30-175 ( last range was [175,600) ))

**H<sub>0</sub>** = Movie Rating and Runtime are independent

**H<sub>a</sub>** = Movie Rating and Runtime are dependent

The Chi<sup>2</sup> value was found to be _1877.509_, with _126_ degrees of freedom the test shows a _p value <0.00001_.
The data suggests that movie runtime and movie rating are not indepent of each other.

We then restricted the data to a smaller range with larger intervals, 30 minutes and 1 point, (4,9) (60,180) (98% of the data, 9848 data points)
H0 = the 2 parameters are independent, Ha = the 2 parameters are dependent

The Chi<sup>2</sup> value was found to be _786.469_, with _12_ degrees of freedom the test shows a _p value <0.0001_.
The data again suggests that movie runtime and movie rating are not indepent of each other.
