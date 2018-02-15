#! /usr/bin/python

from sys import stdin, stdout, stderr, path, exit, argv, platform
import sys
import csv
from getopt import getopt

from parse import parse
from parseargs import parseargs
from process import process
from output import output

def main(argv):

    if platform == "win32":
        stdout = open(sys.__stdout__.fileno(), 
            mode=sys.__stdout__.mode, 
            buffering=1, 
            encoding=sys.__stdout__.encoding, 
            errors=sys.__stdout__.errors, 
            newline='\n', 
            closefd=False)

    precision = parseargs(argv)

    reader = csv.reader(stdin)
    headings, names, points = parse(reader)

    points_out = process(points)


#    point = points_out[0]
#    po0 = point[0]
#    po1 = point[1]
#   po = point[2]
    writer = csv.writer(stdout)
    output(writer, headings, names[1:], points_out, precision)

    exit(0)

# Application entry point!
if __name__ == "__main__":
    main(argv[1:])
