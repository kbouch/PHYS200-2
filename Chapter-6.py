# Chapter 6

def circlearea(radius):
    return 2*math.pi*(radius**2)
   
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
# code in a function after one return is called dead code if the
# the logic reaches the first return token

def return_none(x):
    print x
return_none('kyle')

a = return_none('kyle')

print a

# the function prints something, but it returns 'None' 

# Ex. 6.1

def compare(x,y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1


# distance function

def distance(x1,y1,x2,y2):
    import math
    deltax = x2 - x1
    deltay = y2 - y1
    return math.sqrt((deltax**2)+(deltay**2))

print distance(2,2,-5,7)

# Ex. 6.2
def hypotenuse(a,b):
    """ Returns the length of the hypotenuse of a triangle with the 
        lengths of the legs given as arguments
    """
    c = a**2 + b**2
    return c**2

# Section 6.3
import math
def distance2(x1,y1,x2,y2):
    return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

def area2(r):
    return(math.pi * r**2)

def circ_area(xc,yc,x1,y1):
    """Returns the area of a circle with center at (xc,yc) and
       passing through another point (x1,y1): circ_area(xc,yc,x1,y1)
    """
    return area2(distance2(x1,xc,y1,yc))

print circ_area(2,7,0,0)

# Section 6.4

def is_divisible(x,y):
    if (x%y) == 0.0:
        return True
    else:
        return False
# more concise:
def is_divisible2(x,y):
    return x % y == 0

# Ex. 6.3
def is_between(x,y,z):
    if z > x:
        return x < y and y < z
    if x > z:
         return z < y and y < x

a = 2
b = -2
c = -6
print is_between(a,b,c),b,'is between',a,'and',c

# Section 6.5
def factorialrecurse(n): 
    if n % 1 != 0 or n < 0:
        return
    elif n == 0:
        return 1
    else:
        return n*factorialrecurse(n-1)

print factorialrecurse(20)
