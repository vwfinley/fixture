#!/usr/bin/python

from sys import stdin, stdout, stderr, path, exit, argv
from getopt import getopt

default_precision = 4

def parseargs(argv):
    precision = default_precision

    opts, args = getopt(argv, "p:", "[]")
    for opt, arg in opts:
        if opt == '-p':
            precision = arg
    return precision
