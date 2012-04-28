# Chapter 15

# Ex. 15.1

def distance(a,b):
    import math
    xdist = a.x - b.x
    ydist = a.y - b.y
    d = math.sqrt((xdist)**2 + (ydist)**2)
    return d

class point(object):
    """represents a point in space"""

print point
a = point()
print a
a.x = -40.0
a.y = 25.37

b = point()

b.x = 37
b.y = 16

print str(distance(a,b))+' units'


# Ex. 15.2

class rectangle(object):
    """represents a rectangle by its width, height, and the bottom left corner. Rectangles are oriented with sides parallel to the x and y axes."""
class point(object):
    """represents a point in space"""

def make_rectangle(iwidth,iheight,icorner):
    r = rectangle()
    r.width = iwidth 
    r.height = iheight
    r.corner = point()
    r.corner.x = icorner.x
    r.corner.y = icorner.y
    return r

def move_rectangle(r,dx,dy):
    r.corner.x += dx
    r.corner.y += dy
    return r

here = point()
here.x = 35
here.y = -14

new_rectangle = make_rectangle(300,175,here)
print new_rectangle.width
print new_rectangle.height
print (new_rectangle.corner.x, new_rectangle.corner.y)

rectangle2 = move_rectangle(new_rectangle,-36,200)
print rectangle2.width
print rectangle2.height
print (rectangle2.corner.x, rectangle2.corner.y)


# Ex. 15.3

def copy_move_rectangle(r,dx,dy):
    import copy
    newr = copy.deepcopy(r)
    newr.corner.x += dx
    newr.corner.y += dy
    return newr

far_rectangle = rectangle()
far_rectangle.width = 50
far_rectangle.height = 20
far_rectangle.corner = point()
far_rectangle.corner.x = 1000
far_rectangle.corner.y = 5000


near_rectangle = copy_move_rectangle(far_rectangle,(-far_rectangle.corner.x),(-far_rectangle.corner.y))

print near_rectangle.corner.x
print near_rectangle.corner.y
