from sys import path
from numpy import pi

path.insert(0, 'C:/svn_vwf/spatial/trunk')
from spatial import point, translation, rotation, cart2pol

def process(points):
    pout = []

    p0 = points.pop(0)
    p1 = points[0]
    n = len(points)
    theta_start = 180.0
    theta_end = 360.0
    theta_span = theta_end - theta_start
    theta_incr = theta_span / n
    i = 0

    for p in points:
        theta_step = i * theta_incr
        i += 1
        m = create_transform(p, theta_start, theta_step)

        po0 = m * p0
        po1 = m * p1
        po = m * p

        pout.append((po0, po1, po))

    return pout

def create_transform(p, theta_start, theta_step):           
    r, theta = cart2pol(p[0], p[1])
    
    t = translation(-p[0], -p[1])
    r = rotation(-theta)
    r1 = rotation(-pi)
    r2 = rotation(theta_start)
    r3 = rotation(theta_step)
    
    m = r3 * r2 * r1 * r * t

    return m
