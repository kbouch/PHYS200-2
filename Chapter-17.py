# Chapter 17: Classes and Methods

# Ex. 17.1

class Time(object):
    """Represents a time, with attributes hour, minute, second"""

    # this first function is my answer. The rest were for experimenting
    def time_to_int(self):
        amass_seconds = (60**2)*self.hour + 60*self.minute + self.second
        return amass_seconds


    def time_to_int_2(t1):
        amass_seconds = (60**2)*t1.hour + 60*t1.minute + t1.second
        return amass_seconds

    def time_to_int_3(t1,self):
        amass_seconds = (60**2)*t1.hour + 60*t1.minute + t1.second
        print self
        return amass_seconds

    def time_to_int_4(t1,self):
        amass_seconds = (60**2)*self.hour + 60*self.minute + self.second
        print t1
        return amass_seconds



timeA = Time()
timeA.hour = 5
timeA.minute = 36
timeA.second = 17

print timeA.time_to_int()
print timeA.time_to_int_2() # definition of methods inside the class
# do not require that the first parameter is 'self'

print timeA.time_to_int_3(42) # I can even use self as the second
# parameter and it works. The subject is always entered as the first
# parameter; self is just the common name to use, not special (even
# though my text editor highlights it as special)

# print timeA.time_to_int_4(35)
# this doesn't work, becuase I did not make the first parameter the one
# that the function treats as the object. Don't rely on 'self' to
# path the subject object to the right parameter; subjct  always goes to
# the first parameter.



# Ex. 17.2

class Point(object):
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.x = x
        self.y = y
        self.z = z

here = Point(10,-5)
print here.x
print here.y

here.__init__(20.0,30.0,40.0) # you can use the __init__ method even after
# you instantiate an object
print here.x
print here.y
print here.z


# Ex. 17.3

class Point(object):
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return 'Point with coordinates x = %g, y = %g, z = %g' % (self.x,self.y,self.z)

place = Point(14.0,32.0,1.0)
print place


# Ex. 17.4

class Point(object):
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return 'Point with coordinates x = %g, y = %g, z = %g' % (self.x,self.y,self.z)

    def __add__(self,other):
        combined = Point()
      # for c in [x,y,z]: 
      #     combined.c = self.c + other.c
      # I thought this loop would work, except the
# instead of treating them as attribute names, python thinks they are
# variables that have not been defined yet...

        combined.x = self.x + other.x
        combined.y = self.y + other.y
        combined.z = self.z + other.z
        return combined

        



A = Point(12.0,-50.0,69.78)
B = Point(19.7,12.6,-42.0)

print A + B


# Ex. 17.5

class Point(object):
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return 'Point with coordinates x = %g, y = %g, z = %g' % (self.x,self.y,self.z)

    def __add__(self,other):
        combined = Point()
        if isinstance(other,Point):
            combined.x = self.x + other.x
            combined.y = self.y + other.y
            combined.z = self.z + other.z
        elif isinstance(other,tuple):
            combined.x = self.x + other[0]
            combined.y = self.y + other[1]
            combined.z = self.z + other[2]
        return combined

    def __radd__(self,other):
        return self.__add__(other)

C = Point(48,66.2,89.0)
print C
print (12.5,15.6,-44) + C
print C,'Point C is unchanged'


