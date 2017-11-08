#!/usr/bin/env python
from sys import argv

def read_from_file(file_name):
    f = open(file_name,"r")
    token=f.read().rstrip()
    f.close()
    return token

#Used to test
#print read_from_file(argv[1])
