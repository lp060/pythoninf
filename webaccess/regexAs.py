#!/usr/bin/python2
import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_42.txt"
handle = open(name)
#text = handle.read()
#numlist = re.findall('[0-9]+',text)
#print sum(int(x) for x in numlist)
print sum([int(x) for x in re.findall('[0-9]+', handle.read())])
