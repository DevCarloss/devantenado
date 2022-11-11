
from news.getNews import requestNews

# Script Requests olhardigital.com.br

URL = "https://olhardigital.com.br/editorias/noticias/amp/"

olharDigitalBs4 = requestNews(URL)
# Olhar Digital News
linkPost = olharDigitalBs4.find('a',attrs={'class': "od-post"})

newsLink = linkPost['href']
newsTitle = linkPost['title']
newsImage= olharDigitalBs4.find('div',attrs={'class': "od-post-img"}).find('amp-img')['src']
newsDescription = olharDigitalBs4.find('div',attrs={'class': "od-post-excerpt"}).getText()
