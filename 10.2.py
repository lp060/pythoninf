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
		time = words[5].split(':')
		counts[time[0]] = counts.get(time[0],0) + 1
tup = counts.items()

for k,v in sorted(tup):
	print k,v
