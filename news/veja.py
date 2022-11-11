from news.getNews import requestNews

# Script Noticias veja.com.br/ultimas

# Veja News Requests

URL = "https://veja.abril.com.br/ultimas-noticias/"


vejaBs4 = requestNews(URL)

# Veja News 
vejaTitleH2 = vejaBs4.find('h2',attrs={'class': 'title'})
newsDescription = vejaBs4.find('span', attrs={"class":"description"}).getText()
newsLink = vejaTitleH2.find_parent('a')['href']
newsTitle = vejaTitleH2.getText()
newsImage = vejaBs4.find('figure',attrs={'class':'media'}).find('img')['src']
