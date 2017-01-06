#!/usr/bin/python2
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	line.rstrip()
	words = line.split()
	if len(lst) == 0 : lst.append(words[0])
	for word in words:
		if word in lst: continue
		lst.append(word)

lst.sort()
print lst
