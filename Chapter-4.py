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
kyle.delay = 0.01
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
# just close the TurtleWorld window when the animation stops, and the next
# one will open.
wait_for_user()
from TurtleWorld import *
world = TurtleWorld()
kyle = Turtle()
print kyle

# Section 4.3 Excercises
def square(t,l):
    t.delay = 0.001
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
    """ Draws a polygon with 'n' number of sides and side length 'l' with
    turtle 't'.
    """
    t.delay = 0.01
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

# I finally fixed my symantic errors for circle! It models a circle as a
# polygon. The number of sides used is enough to ensure that the ratio
# radius / side length = specified constant.
# My function takes 3 parameters: turtle name, radius, and accuracy constant.
# The larger the constant, the more acurate the circle. k >= 1 .
# If k < 1, only one line is drawn. If k < 0, no lines appear (n = 0).
# Higher accuracy takes more time to draw.
def circle(t,r,k):
    """ Draws a circle of radius 'r' using turtle 't'. k is the constant
    (radius)/(polygon side length) and higher k gives a more accurate circle.
    k >= 1.
    """
    t.delay = 0.01
    import math
    alpha = 2*math.acos(1/(2.0*(k))) # gives radians
    theta = math.pi-alpha
    n = math.ceil((2*math.pi)/theta)
    worktheta = (2*math.pi)/float(n)
    workalpha = math.pi-worktheta
    l = 2*r*math.cos(workalpha/2) # takes radians
    for i in range(int(n)):
        lt(t,worktheta*(180/math.pi)) # takes degrees
        fd(t,l)
    pu(t)
    lt(t,90)
    fd(t,r)
    lt(t,180)
    pd(t)
    fd(t,1)
    pu(t)
    fd(t,r-1)
    lt(t,90)
    pd(t)


circle(kyle,20,30)
circle(kyle,30,10)
circle(kyle,40,30)

wait_for_user()
from TurtleWorld import *
world = TurtleWorld()
kyle = Turtle()
print kyle

#The only thing different about this function from circle() is that it takes
#a parameter 'a' which is the angle trhough wich an arc that is part of a
#circle should be drawn
def arc(t,r,a,k):
    """ Draw part of a circle, an arc. Turtle 't' draws an arc, moving
    through an angle 'a' at radius 'r'. k is the constant (radius)/(polygon
    side length) and higher k gives a more accurate circle. k >= 1.
    """  
    t.delay = 0.01
    import math
    alpha = 2*math.acos(1/(2.0*(k))) # gives radians
    theta = math.pi-alpha
    n = math.ceil((a*(math.pi/180))/theta)
    worktheta = (a*(math.pi/180))/float(n)
    workalpha = math.pi-worktheta
    l = 2*r*math.cos(workalpha/2) # takes radians
    for i in range(int(n)):
        lt(t,worktheta*(180/math.pi)) # takes degrees
        fd(t,l)

# this code would return the turtle to its starting position (needs to be
# fixed)
#backx = 0
#for i in range(int(n)):
#    backx = backx + (l*math.cos(i*worktheta))
#backy = 0
#for i in range(int(n)):
#    backy = backy + (l*math.sin(i*worktheta))
#backr = math.sqrt((backx**2)+(backy**2))
#lt(t,(180/math.pi)*(worktheta-((math.pi/2)-math.atan(backx/backy))))
#pu(t)
#fd(t,backr)
#lt(t,(180/math.pi)*((math.pi/2)-math.atan(backx/backy)))
#pd(t)

arc(kyle,50,180,40)
arc(kyle,30,270,40)

wait_for_user()

# End of Chapter 4 Excercises
# 1. see my above functions for their doc strings
# 2. Stack diagram for my circle function
# __main__ |    |
# circle   | t > kyle, r > 20, k > 50 |
#          | alpha > 3.12159 rad      |
#          | theta > 0.020000 rad     |
#          | n > 315                  |
#          | worktheta > 0.01994662 rad |
#          | workalpha > 3.121646 rad |
#          | l > 0.39893              |

# 3. 'flower' shapes. I could work on it more to modify the petal fatness.

def flower(t,p,r,k):
    """ Draws a flower shape of 'p' petals made of arc segments of a circle
    with radius 'r'. Drawn using turtle 't'. Accuracy of the circle is
    determined by k. Higher k gives better accuracy, but takes longer to
    draw. This function uses the 'arc' function defined previously.
    """
    import math
    t.delay = 0.01
    angle = 180-(360.0/p)
    arc(t,r,angle,k)
    lt(t,(180-angle))
    for i in range(int(p-1)):
        arc(t,r,2*angle,k)
        lt(t,(180-angle))
    arc(t,r,angle,k)

from TurtleWorld import *
world = TurtleWorld()
kyle = Turtle()
print kyle

flower(kyle,3,50,30)

wait_for_user()
from TurtleWorld import *
world = TurtleWorld()
kyle = Turtle()
print kyle

flower(kyle,5,100,30)

wait_for_user()
from TurtleWorld import *
world = TurtleWorld()
kyle = Turtle()
print kyle

flower(kyle,8,100,30)

wait_for_user()
from TurtleWorld import *
world = TurtleWorld()
kyle = Turtle()
print kyle

flower(kyle,12,100,30)

wait_for_user()
