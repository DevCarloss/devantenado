from news.getNews import requestNews
# Script Noticias Tecnologia adrenaline.com

# Adrenaline Requests
URL = 'https://adrenaline.com.br/noticias'
adrenalineBs4 = requestNews('https://adrenaline.com.br/noticias')

# Adrenaline News 

newsDiv = adrenalineBs4.find('div',attrs={'class': "col-lg-4 post-h__image"})
newsLink = newsDiv.find('a')['href']
newsTitle = newsDiv.find('img')['title']
newsImage = newsDiv.find('img')['data-original']
newsDescription = adrenalineBs4.find('p',attrs={'class': "post-h__content-sub"}).getText()
