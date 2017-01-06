#!/usr/bin/python2
# Use the file name mbox-short.txt as the file name

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
	line.rstrip()
	if line == ' ': continue
	words = line.split()
	if words[0] == "From:" or words[0] != "From " : continue
	print words[1]
    	count = count + 1

print "There were", count, "lines in the file with From as the first word"

