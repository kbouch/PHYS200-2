# Chapter 5 Excercises

# Ex 5.1
# 1.
def check_fermat(a,b,c,n):
    if a**n + b**n == c**n and n > 2:
        print 'Holy smokes, Fermat was wrong!'
    elif n > 2:
        print "Nope, doesn't work"

check_fermat(2,10,57,5)
check_fermat(2,10,57,2.1)
check_fermat(2,19,33,7)
check_fermat(2,1,1,14)

# 2.
def input_check_fermat():
    import math
    a = int(math.floor(float(raw_input('a = '))))
    b = int(math.floor(float(raw_input('b = '))))
    c = int(math.floor(float(raw_input('c = '))))
    n = int(math.floor(float(raw_input('n = '))))
    if a <0 or b <0 or c<0 or n<0:
        print 'a, b, c, n must be integers greater than 0.'
    print 'a = '+str(a), 'b = '+str(b), 'c = '+str(c), 'n = '+str(n)
    check_fermat(a,b,c,n)

input_check_fermat()

# Ex 5.2 parts 1 and 2
def is_triangle():
    import math
    a = int(math.floor(float(raw_input('a = '))))
    b = int(math.floor(float(raw_input('b = '))))
    c = int(math.floor(float(raw_input('c = '))))
    if a <0 or b <0 or c<0:
        print 'a, b, and c must be integers greater than 0.'
    print 'a = '+str(a), 'b = '+str(b), 'c = '+str(c)
    c1 = a>=b and a>=c
    c2 = b>=a and b>=c
    if c1 == bool('true'):
        if (b+c) > a:
            print 'Yes'
        elif (b+c) < a:
            print 'No'
        elif (b+c) == a:
            print 'Degenerate case'
    elif c2 == bool('true'):
        if (a+c) > b:
            print 'Yes'
        elif (a+c) < b:
            print 'No'
        elif (a+c) == b:
            print 'Degenerate case'
    elif bool('true'):
        if (a+b) > c:
            print 'Yes'
        elif (a+b) < c:
            print 'No'
        elif (a+b) == c:
            print 'Degenerate case'

is_triangle()

# Ex 5.3
import sys
sys.path.append('/home/kyle/Downloads/epd-7.2-2-rh5-x86/lib/python2.7/site-packages/swampy-2.0')
print sys.path

from TurtleWorld import *
world = TurtleWorld()
kyle = Turtle()
print kyle

# I thought this would just draw a spiral. But it kept drawing.
def draw(t, length, n):
    t.delay= 0.01
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

#draw(kyle,10,5)

wait_for_user()
from TurtleWorld import *
world = TurtleWorld()
kyle = Turtle()
print kyle

def koch(t,l,n):
    if n == 0:
        return
    koch(t,l/3.0,n)
    lt(t,60)
    koch(t,l/3.0,n)
    lt(t,120)
    koch(t,l/3.0,n)
    lt(t,60)
    koch(t,l/3.0,n)

#koch(kyle,10,10)
# I don't understand how to do this

wait_for_user()
