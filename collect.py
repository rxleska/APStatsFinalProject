# Libraries used in the web scraping
from distutils.log import error
import requests
from bs4 import BeautifulSoup
import json
from io import BytesIO
import re

from sqlalchemy import false

# generally followed by a 7-8 digits number
BASE_SEARCH_URL = "https://www.imdb.com/title/tt"

TAGS_CLASSNAME = "sc-94726ce4-3 eSKKHi"
RATING_CLASSNAME = "sc-7ab21ed2-1 jGRxWM"
RUNTIME_CLASSNAME = "ipc-metadata-list-item__content-container"
TITLE_CLASSNAME_Ma = "sc-b73cd867-0 eKrKux"
TITLE_CLASSNAME_Mi = "sc-b73cd867-0 eKrKux"
EFOF_CLASSNAME = "sc-5a0cf61d-5 epMgJy"


def getRequest(IMDbID):
    searchUrl = BASE_SEARCH_URL + "" + IMDbID
    htmlResponse = requests.get(searchUrl).text
    theSOUP = BeautifulSoup(htmlResponse, 'html.parser')
    return theSOUP


def isMovie(soup):
    fofE = soup.findAll(attrs={"class": EFOF_CLASSNAME})
    if(len(fofE) > 0):
        return False

    eps = soup.findAll(attrs={"class": "sc-2a366625-3 eqCBtv"})
    if(len(eps) > 0):
        return False

    divs = soup.findAll(attrs={"class": TAGS_CLASSNAME})
    if(len(divs) < 1):
        return False
    div = divs[0]
    listItems = div.findAll('li')
    firstListItem = listItems[0]
    firstListItemText = firstListItem.text
    return firstListItemText.isnumeric()


def getRating(soup):
    try:
        span = soup.find(attrs={"class": RATING_CLASSNAME})
        rating = span.text
        return rating
    except:
        return "none"


def getRunTime(soup):
    divs = soup.findAll(attrs={"class": RUNTIME_CLASSNAME})
    for div in divs:
        if "minute" in div.text or "hour" in div.text:
            return timeText2Minutes(div.text)
    return "unknown"


def timeText2Minutes(text):
    text = text.replace("s", "")
    time = 0
    if "hour" in text:
        hm = text.split("hour")
        time += 60 * int(hm[0].strip())
        if "minute" in text:
            m = hm[1].split("minute")
            time += int(m[0].strip())
    elif "minute" in text:
        m = text.split("minutes")
        time += int(m[0].strip())
    return time


def getTitle(soup):
    divs = soup.findAll(attrs={"class": TITLE_CLASSNAME_Ma})
    for div in divs:
        d = div.findAll(attrs={"class": TITLE_CLASSNAME_Mi})
        for a in d:
            return d.text
    return "unknown"

    # av = getRequest("2622826")  # Avalance sharks tv movie 2.3 - 1 hour 22 minutes
    # print(isMovie(av))
    # print(getRating(av))
    # print(getRunTime(av))

    # # doctor strange in the multiverse MOVIE 7.4 - 2 hours 6 minutes
    # ds = getRequest("9419884")
    # print(isMovie(ds))
    # print(getRating(ds))
    # print(getRunTime(ds))

    # p = getRequest("10203880")  # TV mini series 6.1 - 2 hours 40 minutes
    # print(isMovie(p))
    # print(getRating(p))
    # print(getRunTime(p))

    # ws = getRequest("0090305")  # Movie 6.6 - 1 hour 34 minutes
    # print(isMovie(ws))
    # print(getRating(ws))
    # print(getRunTime(ws))
