#!/usr/bin/python

from sys import stdin, stdout, stderr, path, exit
import csv


def output(writer, headings, names, results, precision):    
    formatstr = '{0:0.'+ str(precision) +'f}'
    writer.writerow(headings)

    for idx in range(len(results)):       
        result = results[idx]
        po0 = result[0]
        po1 = result[1]
        po = result[2]

        writer.writerow((names[idx], formatstr.format(po0[0,0]), formatstr.format(po0[1,0]), formatstr.format(po1[0,0]), formatstr.format(po1[1,0]), formatstr.format(po[0,0]), formatstr.format(po[1,0])))

    return

