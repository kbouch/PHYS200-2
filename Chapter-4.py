# I will use a text document for this chapter rather than ipython notebook

# To run this in the terminal (linux) type after the prompt:
# $ python (filename).(extention)
# which would be:
# $ python Chapter-4.py

# After you run this, and the TurtleWorld window is done with its animation,
# close the TurtleWorld window. Otherwise the terminal will not respond to
# new commands.

# first, I will add the swampy directory to the search path
# I moved the directory 'swampy-2.0' into the directory 'site-packages'.
# this directory is in the enthought python distribution directory, which I 
# added to my path by adding an 'export' line to my .bashcr file in order to
# use ipython notebook
import sys
sys.path.append('/home/kyle/Downloads/epd-7.2-2-rh5-x86/lib/python2.7/site-packages/swampy-2.0')
print sys.path
# That should allow me to use swampy every time I run this,
# assuming I don't move the swampy directory out of that location

# Now for the excercises
from TurtleWorld import *
world = TurtleWorld()
kyle = Turtle()
print kyle

# square
fd(kyle,100)
lt(kyle)
fd(kyle,100)
lt(kyle)
fd(kyle,100)
lt(kyle)
fd(kyle,100)
lt(kyle)

# Yes! now I get to learn the for loop!
for i in range(4):
    print 'Hello!'
for i in range(4):
    fd(kyle,100)
    lt(kyle)

# I found that you can clear the turtle world drawing board by using the
# function wait_for_user() and then re-importing TurtleWorld and redifining
# the variables world and the turtle's name, and reprinting the turtle.
wait_for_user()
from TurtleWorld import *
world = TurtleWorld()
kyle = Turtle()
print kyle

# Section 4.3 Excercises
def square(t,l):
    for i in range(4):
        fd(t,l)
        lt(t)
square(kyle,10)
square(kyle,20)
square(kyle,30)
square(kyle,50)
square(kyle,100)

wait_for_user()
from TurtleWorld import *
world = TurtleWorld()
kyle = Turtle()
print kyle

def polygon(t,l,n):
    for i in range(n):
        lt(t,360.0/n)
        fd(t,l)
        
polygon(kyle,10,6)
polygon(kyle,30,9)
polygon(kyle,50,11)

wait_for_user()
from TurtleWorld import *
world = TurtleWorld()
kyle = Turtle()
print kyle

# I enjoyed working on this problem. My circles are modeled as polygons with
# sides that are less than or equal to 10 turtle steps in length.
def circle(t,r):
    import math
    theta = 10.0/r #angle at tip of the 'pie wedges', at center of the circle 
    n = math.ceil((2*math.pi)/theta) # number of wedges (sides) to go around, rounded up to nearest integer
    worktheta = 360.0/n # now i am in degrees, and this number will work with my n rounded to an integer (rounded up so that sides are <= 10 steps long)
    alpha = 180-worktheta # interiror polygon angle
    l = 2*(r/math.atan(alpha/2))
    for i in range(int(n)):
        lt(t,360.0/n)
        fd(t,l)

circle(kyle,20)
circle(kyle,30)
circle(kyle,40)

wait_for_user()

