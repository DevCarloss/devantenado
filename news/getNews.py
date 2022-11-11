import requests
from bs4 import BeautifulSoup

def requestNews(url):
    requestSite = requests.get(url)
    requestContent = BeautifulSoup(requestSite.text,'html.parser')
    return requestContent
