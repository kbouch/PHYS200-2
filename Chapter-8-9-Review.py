# Chapter 8
# String slice practice
word = 'octopus'
print word[:]
print word[0:-1]
print word[-1:]
print word[-4:-1]
print word[0:]
# blanks on either side of the colon are automatically the start or ending index of the word
# negative indexes count backward from the end of the word
# the ending index can be <= the length of the word.
print word[0:len(word)]
# a single number calls one letter
print word[6]
# a single number cannot be the length of the word, because the individual indexes are ahead of the letter, starting at zero and going to the lengh minus 1.
# print word[7]

print word[-1]
print word[-7]
# even when negative indexes are used, the divider in front of the letter indexes the letter
# |o|c|t|o|p|u|s|
# 0 1 2 3 4 5 6 7
#-7-6-5-4-3-2-1

a = 'car'
b = 'car'
print a==b

c = [1,2,3]
d = [1,2,3]
print c == d

# same object?

# searching
def find(c,s,b):
    n = 0
    for i in s[b:]: # strings are iterables
        if i == c:
            n = n + 1
    if n > 0:
        print 'Found '+str(n)+' instances of '+c+' in the string "'+s+'"'
        return n
    else:
        print str(c)+' was not found.'

find('o','octopus',0)

print 'lob' in 'lobster'
print 'lob' in 'Lobster'
# letter case is important
print 'lob' in 'Lobster'.lower()
# There are many string methods. some other useful ones:
word = '       space invaders       '
word = word.strip()
# strings with methods return a value. must update the string with 
# assignment. For lists however this might be different

# now after running a method on string,
print word
word = word.replace('a','').replace('e','')
print word

another = 'casssssshhh'
print another.format('a',{'@'}) # I thought this would work...

print '-'.join(['seven','year','old'])+' boy'
# the argument of join must be a single iterable

print another.find('h',2)

print 'yellow' > 'orange'
print 'Yellow' > 'orange'
print 'greEn' > 'green'
# later letters are greater, but capital letters have lower values
# than lower case in their code representation.

# rotation of letters encoding
print ord('a')
print ord('A')
print ord('b')
print ord('B')
print ord('z'), ord('Z')

def encode(s):
    t =''
    for i in range(len(s)):
        a = ord(s[i])
        if a > 90:
            if a + 13 >= 122:
                b = 96 + ((a+13)-122)
            else:
                b = a + 13
        if a <= 90:
            if a + 13 >= 90:
                b = 64 + ((a+13)-90)
            else:
                b = a + 13
        t = t[:i+1]+chr(b)
    return t

print encode('Kyle')
print encode(encode('Kyle'))
# yes! it works, let's try to improve it

def encode_2(s):
    t =''
    for i in range(len(s)):
        a = ord(s[i])
        if a > 90:
            b = a + 13 +((a+13)/122)*(-1*(13+a)+96+((a+13)-122))
        if a <= 90:
            b = a + 13 +((a+13)/90)*(-1*(13+a)+64+((a+13)-90))
        t = t[:i+1]+chr(b)
    return t

print encode_2('Whale')
print encode_2(encode_2('Whale'))
#!!!!!!! Remeber that side by side parentheses-enclosed expressions
# do not multiply like on a calculator. I must use * as in (a)*(b).
# !!!!!!!
# I made use of floor division here, or I could have divided
# by floats 122.0 and 90.0 and used math.floor()

# Moving on to chapter 9

import sys
sys.path.append('/home/kyle/Downloads/epd-7.2-2-rh5-x86/lib/python2.7/site-packages/swampy-2.0')

fin = open('words.txt')
print fin

def wordlenpick(l):
    fin = open('words.txt')
    flag = 'AA'
    while flag < 'zymurgieA':
        line = fin.readline()
        word = line.strip()
        if len(word)>=l:
            print word
        flag = word

wordlenpick(20)
# The results are:
# counterdemonstration
# counterdemonstrations
# counterdemonstrators
# hyperaggressivenesses
# hypersensitivenesses
# microminiaturization
# microminiaturizations
# representativenesses

def has_no_e(s):
    for c in s:
        if c=='e' or c=='E':
            return False
    return True

def avoids(s,a):
    for element in a:
        for c in s:
            if c == element:
                return False
    return True

def words_that_avoid(a): # uses previously defined program avoids()
    fin = open('words.txt')
    flag = 'AA'
    while flag < 'zymurgieA':
        line = fin.readline()
        word = line.strip()
        if avoids(word,a):
            print word
        flag = word

words_that_avoid(['a','e','i','o','u'])
print 'Next output'
words_that_avoid(['a','e','i','o','u','y'])

def uses_only(a):
    fin = open('words.txt')
    flag = 'AA'
    while flag < 'zymurgieA':
        line = fin.readline()
        word = line.strip()
        for element in a:
            for c in word:
                if not c == element:
                    
        
uses_only(['a','g','n','t','v','e']
