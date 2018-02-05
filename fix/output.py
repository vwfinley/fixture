#!/usr/bin/python

from sys import stdin, stdout, stderr, path, exit
import csv


def output(writer, headings, names, points, precision):    
    formatstr = '{0:0.'+ str(precision) +'f}'
    writer.writerow(headings)

    for idx in range(len(points)):       
       #idx = points.index(point) 
#        writer.writerow(names[idx], formatstr.format(point[0]), formatstr.format(point[1])) 
        point = points[idx]
        x = formatstr.format(point[0,0])
        y = formatstr.format(point[1,0])
        writer.writerow((names[idx], x, y))
#        print(str(x) + "," + str(y))
    return

