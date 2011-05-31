#!/usr/bin/python

# ./helloworld.py 10
# Will print Hello World 10 times

import re, string, sys

counter = int(sys.argv[1])

# Option 2 (much simpler)
for i in xrange(1,counter+1):
	print "Hello, World %d!" %(i,)
