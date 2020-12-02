import requests
import urllib 
import urllib.request
from bs4 import BeautifulSoup
import os


def image_scraper(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage, 'html.parser')
	
	folder_name = url.split('/')[-1]  # splitting the URL link to use as folder name
	try:
		os.mkdir(os.path.join(os.getcwd(), folder_name)) # creating new directory (os.mkdir) by joining(os.path.join) current directory path(os.getcwd()) with new folder name
	except:
		pass
	os.chdir(os.path.join(os.getcwd(), folder_name))
	for images in soupdata.find_all('img'): # filter the html code for img files
		links = images['src'] # picking all the images with 'src'
		if links == 'assets/images/logo.png': # skipping this string in loop
			continue
		elif links == 'assets/images/logo-small.png': # skipping this string in looop
			continue 
		name_only = links.split('/')[-1] # splitting the link text to use as file name
		with open(name_only + '.jpg', 'wb') as f: # open the file in wirte mode 'w', # 'wb' is the 'write binary' mode
			im = requests.get(links) # sending individual requests to the links, to get the informatio from them
			f.write(im.content) # write and save content (information) that the link contains  to file