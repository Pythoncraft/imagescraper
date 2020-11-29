import requests
import urllib 
import urllib.request
from bs4 import BeautifulSoup
import os

def make_soup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage, 'html.parser')
	return soupdata

image_links = []
soup = make_soup('https://officeandhome.eu/catalog/office-chairs') # calling the function
#os.mkdir(os.path.join(get))
for images in soup.find_all('img'): # filter the html code for img files
	links = images['src'] # picking all the images with 'src'
	if links == 'assets/images/logo.png': # skipping this string in loop
		continue
	elif links == 'assets/images/logo-small.png': # skipping this string in looop
		continue 
	name_only = links.split('/')[-1] # splitting the link text to use as file name
	with open(name_only + '.jpg', 'wb') as f: # open the file in wirte mode 'w', # 'wb' is the 'write binary' mode
		im = requests.get(links) # sending individual requests to the links, to get the informatio from them
		f.write(im.content) # write and save content (information) that the link contains  to file
	