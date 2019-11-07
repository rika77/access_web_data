# Retrieving Web Pages
## Using urllib in Python

import urllib.request, urllib.parse, urllib.error

# file handle
# treat URL like a file 
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
	print(line.decode().strip())

counts = dict()


# How is First web crawler like ?