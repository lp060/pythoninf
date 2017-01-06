#!/usr/bin/python2

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
	line.rstrip()
	if line == " " or line == "":continue
	words = line.split()
	if len(words) == 0: continue
	if words[0] == "From":
		counts[words[1]] = counts.get(words[1],0) + 1
print counts
