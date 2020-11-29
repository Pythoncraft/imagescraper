import requests 
from bs4 import BeautifulSoup

#headers = {'User-Agent':'Chrome/75.0.3770.80'}
#URL = 'https://www.narbutas.com/news/new-product-catalogue-2020/'

#get the data
data = requests.get("https://www.narbutas.com/news/new-product-catalogue-2020/")

#loading data in to beautiful Soup. storing in a variable 'soupdata'
soupdata = BeautifulSoup(data.text, 'html.parser')

links = []

image_links = soupdata.select('img[src^="https://www.narbutas.com/wp-content/"')

for images in image_links:
	links.append(images)

for l in links:
	print(l)
#get data by looking through the structure. in this case: all 'div' heads

#for div in soupdata.find_all('div'):
	#for src in div.find_all('src'):
		#print(src)