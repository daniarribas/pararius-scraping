from bs4 import BeautifulSoup
import requests
from csv import writer
pag =1
pages = 66 #number ofpages teh website has
with open('pararius.csv', 'w', encoding='utf8', newline='') as f:
  thewriter = writer(f)
  header = ['Title','Location','Price','Area']
  thewriter.writerow(header)
  while pag<=pages : #this loop manages each page URL
    url = "https://www.pararius.com/apartments/nederland/page-" + str(pag)
    page = requests.get(url)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    lists =  soup.find_all('section',class_="listing-search-item")
    for list in lists:
     title = list.find('a', class_="listing-search-item__link--title").text.replace('\n','')
     location = list.find('div', class_="listing-search-item__sub-title").text.replace('\n','')
     price = list.find('div', class_="listing-search-item__price").text.replace('\n','')
     area = list.find('li', class_="illustrated-features__item--surface-area").text.replace('\n','')
     info = [title, location, price, area]
     thewriter = writer(f)
     thewriter.writerow(info)
      
    pag += 1
print("finished") # this message means CSV is ready to use