from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks2(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "lxml")
    for link in bsObj.findAll("a",href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #new url
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks2(newPage)
getLinks2("")
