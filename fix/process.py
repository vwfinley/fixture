from sys import path
from numpy import radians, dot

path.insert(0, 'C:/svn_vwf/spatial/trunk')
from spatial import point, translation, rotation

#sys.path.insert(0, '../geometry')
#from geometry import Rotation, Translation, Point

def process(points):
    pout = []
    for p in points:
        pout.append(process_point(p))
    return pout

def process_point(p):           
    t = translation(-1.5, -2.0)
    r = rotation(radians(45))
    m = t * r
    po = m * p
    return po
