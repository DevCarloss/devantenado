import requests
from bs4 import BeautifulSoup

# Script Noticias Tecnologia adrenaline.com

# Adrenaline Requests

adrenalineUrl = 'https://adrenaline.com.br/noticias'

adrenalineReq = requests.get(adrenalineUrl)

adrenalinebs4 = BeautifulSoup(adrenalineReq.text,'html.parser')

# Adrenaline News 

adrenalinenewsName = adrenalinebs4.find('div',attrs={'class': "col-lg-4 post-h__image"}).find('img')['title']

adrenalinenewsImg = adrenalinebs4.find('div',attrs={'class': "col-lg-4 post-h__image"}).find('img')['data-original']

adrenalinenewsExcerpt = adrenalinebs4.find('p',attrs={'class': "post-h__content-sub"}).getText()
