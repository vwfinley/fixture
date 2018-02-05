
from sys import stdin, stdout, stderr, path, exit
import csv
path.insert(0, 'C:/svn_vwf/spatial/trunk')
from spatial import point

repeat = '----'
status = 'in parse...'
errmsg1 = 'error: line must contain 3 fields'
errmsg2 = 'error: cannot convert field to float'
errmsg3 = 'error: cannot append list'

def parse(reader):

    headings = []
    names = []
    points = []
    lastcol2 = ''

    for line in reader:
        if not line:                    #skip empty
            continue
        elif line[0].find('#') >= 0:    #skip comment
            continue
        elif len(line) != 3:            #incorrect num columns
            stderr.write(errmsg1)
            exit(1)
        elif ''.join(line).istitle():   #found column headings
            headings = line
        else: 
            if str(line[2].strip()) == repeat:
                line[2] = lastcol2

            try:
                name = line[0].strip()
                x = float(line[1].strip())
                y = float(line[2].strip())
                p = point(x, y)
            except:
                stderr.write(errmsg2 + ' ' + line[0] + ' ' + line[1] + ', ' + line[2])
                exit(1)

            try:
                names.append(name)
                points.append(p) 
            except:
                stderr.write(errmsg3 + ' ' + str(points))
                exit(1)

            lastcol2 = line[2]

    return headings, names, points
    

