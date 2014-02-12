__author__ = 'rami'

def _plot_pixel(x,y):
    print "(%s, %s)"%(x,y),

def _plot_four_corners_pixels(x,y):
    _plot_pixel(x,y)
    _plot_pixel(-x,y)
    _plot_pixel(x,-y)
    _plot_pixel(-x,-y)
    print ""

def plot_circle(r):
    if type(r) is not int:
        raise ValueError()
    for x in xrange(0, r+1, 1):
        for y in xrange(0, r+1, 1):
            if y*y >= (r*r-x*x):
                _plot_four_corners_pixels(x,y)
                break

def plot_circle_improved(r):
    if type(r) is not int:
        raise ValueError()
    last_y = r+1
    for x in xrange(0, r+1, 1):
        for y in xrange(0, last_y, 1):
            if y*y >= (r*r-x*x):
                _plot_four_corners_pixels(x,y)
                break
