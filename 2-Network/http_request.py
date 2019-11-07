# Hypertext Transfer Protocol
# HTTP to retrieve HTML

# https://www.coursera.org/hoge.htm
# https:// -- protocol
# www.coursera.org -- host
# /hoge.htm -- document

# When you click URL on blowser, web-server/
# Webserver responds back HTML
# Browser reads HTML and parse it.

# telnet HOST PORT
# it's a way to connect to any server, any...

# GET http://data.pr4e.org/page1.htm HTTP/1.0
# METADATA (Headers)
# CONTENT (Body)

# Hacker Movies
- Matrix Reloaded
- Bourne Ultimatum
- Die Hard 4

# Actual Security Hacking Software
- https://nmap.org/movies/ 

# An HTTP Request in Python

import socket
# Connect socket
mysock = sock.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4g.org', 80))
# Socket connected to server exists.
# Make a request
# \r\n\r\n = enter enter
cmd = 'GET http://data.pr4g.prg/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
	data = mysock.recv(512)
	if (len(data) < 1):
		# End of  File/ End of transmission
		break
	pront(data.decode())
mysock.close

# There are 3 ways to get Headers & Body.
# 1. Open developer mode
# 2. Write python code
# 3. Use telnet
