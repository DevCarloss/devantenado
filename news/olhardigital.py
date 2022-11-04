import requests
from bs4 import BeautifulSoup

# Script Requests olhardigital.com.br

olhardigitalUrl = "https://olhardigital.com.br/editorias/noticias/amp/"

olhardigitalReq = requests.get(olhardigitalUrl)

olhardigitalbs4 = BeautifulSoup(olhardigitalReq.text,'html.parser')

# Olhar Digital News

olhardigitalnewsName = olhardigitalbs4.find('a',attrs={'class': "od-post"})['title']

olhardigitalnewsImg = olhardigitalbs4.find('div',attrs={'class': "od-post-img"}).find('amp-img')['src']

olhardigitalnewsExcerpt = olhardigitalbs4.find('div',attrs={'class': "od-post-excerpt"}).getText()
