#The program will prompt for a URL, read the XML data from that URL using urllib
# and then parse and extract the comment counts from the XML data, 
#compute the sum of the numbers in the file

import urllib
import xml.etree.ElementTree as ET


url = raw_input('Enter location: ')
if len(url) < 1 : print 'Invalid location'

    #url = urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
print tree
tempcount =0
sum = 0
counts = tree.findall('.//count')
for count in counts: 
	tempcount += 1
	sum += int(count.text)

print 'count:',tempcount
print 'Sum:',sum
