import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# API is not needed.
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')


print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

print(data.decode())
tree = ET.fromstring(data)
results = tree.findall('.//count')

sum = 0
for result in results:
	sum += int(result.text)

print("Count: ", len(results)) 
print("Sum: ", sum)