import requests
from bs4 import BeautifulSoup

# Script Noticias veja.com.br/ultimas

# Veja News Requests

vejaUrl = "https://veja.abril.com.br/ultimas-noticias/"

vejaReq = requests.get(vejaUrl)

vejabs4 = BeautifulSoup(vejaReq.text,'html.parser')

# Veja News 

vejanewsName = vejabs4.find('h2',attrs={'class': 'title'}).getText()

vejanewsImg = vejabs4.find('figure',attrs={'class':'media'}).find('img')['src']
