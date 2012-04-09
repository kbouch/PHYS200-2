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

