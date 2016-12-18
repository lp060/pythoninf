#!/usr/bin/python2

import urllib
from BeautifulSoup import *

url = raw_input('Enter -')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
tags = soup('span')
count = 0
total=0
for tag in tags:
	count = count+1
	total = total+int(tag.contents[0])

print 'Count ',count
print 'Sum ',total
