from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(aticleUrl):
    try:
        html = urlopen("http://en.wikipedia.org/wiki/" + aticleUrl)
    except HTTPError as e:
        print(e)
        return None
    if html is None:
        print("Url not found")
        return None
    bsObj = BeautifulSoup(html, "lxml")
    try:
        links = bsObj.find("div", {"id": "bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))
    except AttributeError as e:
        print("tag not found")
        return None
    return links
links = getLinks("Kevin_Bacon")
if links is not None:
    for link in links:
        print(link)

# while len(links) > 0:
#     newArticl = links[random.randint(0, len(links)-1)].attrs["href"]
#     print(newArticl)
#     links = getLinks(newArticl)
