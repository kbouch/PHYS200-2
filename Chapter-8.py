# Chapter 8 practice and excercises

# Ex. 8.1
def spell_it_out_backward(s):
    l = len(s)
    i = -1
    while i >= -l:
        print s[i]
        i = i - 1

spell_it_out_backward('Hamburger')

# Ex. 8.2
def duckling_names():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for i in prefixes:
        if i == 'O':
            print 'Ouack'
        elif i == 'Q':
            print 'Quack'
        else:
            print i+suffix

duckling_names()


