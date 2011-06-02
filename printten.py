#!/usr/bin/env python

# Will print even numbers in range

r=range(10)

for i in r:
	#print "Hello, World %d!" %(i+1)
	if (i+1) % 2 == 0:
		print "Hello, World " + str(i+1) + "!"
