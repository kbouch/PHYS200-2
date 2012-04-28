# Chapter 16 Exercises

# Ex. 16.1

class Time(object):
    """Represents a time, with attributes hours, minutes, and
    seconds
    """

def print_time(t):
    print '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)

friday_night = Time()
friday_night.hour = 21
friday_night.minute = 53
friday_night.second = 3

print_time(friday_night)


# Ex. 16.2

def is_after(t1, t2):
    """Returns True if the first given time is after the second given
    time, and false if the first time comes before the second time
    """
    print ((t1.hour-t2.hour)+((t1.minute-t2.minute)/60.0)+((t1.second-t2.second)/(60.0**2))) > 0


tA = Time()
tB = Time()
tC = Time()

for o in [tA,tB,tC]:
    o.hour = 13

tA.minute = 45
tB.minute = 55
tC.minute = 45

tA.second = 27
tB.second = 59
tC.second = 26

is_after(tA,tB)
is_after(tA,tC)
is_after(tC,tA)

# Ex. 16.3

def increment(t1,dt):
    (rawdm,ds) = divmod(dt,60.0)
    t1.second += ds
    (rawdh,dm) = divmod(rawdm,60.0)
    t1.minute += dm
    t1.hour   += rawdh
    print_time(t1)

import copy
tD = copy.copy(tA)

print '\n'
print_time(tD)
print 'increased by 9000 seconds to'
increment(tD,9000.0)


# Ex. 16.4

def purefn_increment(t1,dt):
    import copy
    rest = copy.deepcopy(t1)
    (rawdm,ds) = divmod(dt,60.0)
    rest.second += ds
    (rawdh,dm) = divmod(rawdm,60.0)
    rest.minute += dm
    rest.hour   += rawdh
    return rest

print '\n'
print 'input time object is:'
print_time(tB)
print '\n'
print 'output time object, incresed by 15,000 seconds is:'
print_time(purefn_increment(tB,15000))
print '\n'
print 'original object is unchanged:'
print_time(tB)
