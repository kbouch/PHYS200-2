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


circle(kyle,20,50)
circle(kyle,30,10)
circle(kyle,40,30)

wait_for_user()
from TurtleWorld import *
world = TurtleWorld()
kyle = Turtle()
print kyle

# The only thing different about this function from circle is that it takes
# a parameter 'a' 
def arc(t,r,a,k):
    t.delay = 0.01
    import math
    alpha = 2*math.acos(1/(2.0*(k))) # gives radians
    theta = math.pi-alpha
    n = math.ceil((a*(math.pi/180))/theta)
    print n
    worktheta = (a*(math.pi/180))/float(n)
    workalpha = math.pi-worktheta
    l = 2*r*math.cos(workalpha/2) # takes radians
    for i in range(int(n)):
        lt(t,worktheta*(180/math.pi)) # takes degrees
        fd(t,l)
    # this code returns the turtle to its starting position (needs to be
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
from TurtleWorld import *
world = TurtleWorld()
kyle = Turtle()
print kyle
