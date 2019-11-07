from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
cnt = int(input('Enter count: '))
pos = int(input('Enter position: '))

for i in range(cnt):
	print('Retrieving: ', url)
	# Read a whole page in html
	html = urlopen(url, context=ctx).read()
	# Make tree
	soup = BeautifulSoup(html, "html.parser")

	# Retrive all of the anchor tags, which means <a /a>
	tags = soup('a')
	url = tags[pos-1].get('href', None)
	
print('Retrieving: ', url)
print('Last name: ', tags[pos-1].get_text())

