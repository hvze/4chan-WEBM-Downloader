from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import wget


site = input("Type 4chan board URL: ")

hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site, headers=hdr)
page = urlopen(req)

soup = BeautifulSoup(page, 'html.parser')
s = set()

for link in soup.findAll('a'):
	_link = str(link.get('href'))
	if _link.endswith('webm'):
		s.add(_link)

for i in list(s):
	url = 'https:' + str(i)
	filename = wget.download(url)
	
input("\n\nDownload Complete.\n\nPress Enter To Exit\n")
