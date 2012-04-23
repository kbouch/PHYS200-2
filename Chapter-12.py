# Chapter 12: Tuples

a = tuple('sandwhich') # built-in tuple creator, like dict(). If
# argument is a string, creates a tuple with each letter as a value
print a
# indicies and slices work like for lists, but you cannot reassign
# an index to a different value. you must create a new tuple using
# a slice of the old one and concatenation.

def min_max(a):
    return (min(a), max(a)) # return value is a tuple. able to return
# more than one value!
print min_max(a)

# * is used to gather all arguments so that the function can take
# an arbitrary number of arguments. It is placed in the function
# definition. The arguemnts are converted into one tuple.   * is also
# used to scatter the elements of a sequence into individual
# artguments. Written in front of the variable when you call a
# function

# Ex. 12.1
# print sum(1,2,3) sum only takes two arguements.

def sumall(*args):
    total = 0
    for i in range(len(args)):
        total = total + args[i]
    return total

print sumall(1,3,5,7,9)
print sumall(1,3,5,7,9,11,13)
print sumall(1,3,5,7,9,11,13,15,17,19,21)
print sumall(2,4,6,(2*8),10,12,14)
print sumall(2,4,6,8,10,12,(2*14),16,18,20,22,24,26)

# Section 12.5 has zip and enumerate function descritons and some uses
# Section 12.6 talks about dictionaries
# t=d.items() gives a list of tuples t of key-value pairs from the
# dictionary d
# d = dict(t) initializes a dictionary. t is a list of tuples, each
# with two elements

# Ex. 12.2 --------  I can't figure this one out. It is not randomly
# mixing the order of the words that have the same length, even
# though I think I am using the right random module function shuffle()
def sort_by_length(words):
    t = []
    for word in words:
         t.append((len(word), word))
    t.sort(reverse=True)
    print t
    import random
    start = 0
    end = 0
    while start < len(t)-1:
        print start
        for measure in range(start+1,len(t)):
            if t[start][0] != t[measure][0]:
                end = measure
                print end
                random.shuffle(t[start:end])
                restart = end + 1
                break
        start = restart
    res = []
    for length, word in t:
        res.append(word)
    return res

print sort_by_length(['yellow','cat','hi','dinosaur','belt','I','bat','hat','sat','boy','toy'])

# Ex. 12.3
def most_frequent(s):
    h = dict()
    s2 = s.lower()
    for c in s2:
        h[c] = h.get(c,0) + 1
    t = h.items()
    u = []
    for c, f in t:
        u.append((f,c))
    u.sort(reverse=True)
    for c, f in u:
        print c, f

most_frequent('Abrakedabra')

