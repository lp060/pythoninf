#The program will prompt for a URL, read the JSON data from that URL using 
#urllib and then parse and extract the comment counts from the JSON data, 
#compute the sum of the numbers in the file.

import urllib
import json


url = raw_input('Enter location: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
js = json.loads(data)
#print json.dumps(js,indent=4)

count = 0
sum =0
for comment in js['comments']:
	count+=1
	sum+=comment['count']
print 'Count:',count
print 'Sum:',sum
	
