#!/usr/bin/env python
import sys

#print(sys.argv[2])

#name=input("")

f = open(sys.argv[1])

file_contents = f.read()

print (file_contents)

f.c