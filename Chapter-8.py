# Chapter 8 practice and Excercises

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

# Section 8.5
fruit = 'banana'
print fruit[:]
#This will give me the whole word back

# Section 8.6

# Ex. 8.4
def find(letter,word,start):
    """ Given a letter as the first parameter, a word as the second parameter, and the index of the letter where you want to start searching, the function returns the all the indexes of the letter you want.
    """
    l = len(word)
    i = start
    f = False
    while i < l:
        if word[i] == letter:
            print i
            f = True
        i = i + 1
    print 'Reached end of word'
    if f == False:
        print 'No match was found'

find('a','Canada',2)

# Section 8.7
# Ex. 8.5
def count(letter,word):
    c = 0
    for i in word:
        if i == letter:
            c = c + 1
    print c

count('a','banana')

# Ex. 8.6
def count_from(letter,word,start):
    c = 0
    l = len(word)
    if start > l - 1:
        print 'Starting index exceeds index of last letter'
    frag = word[start:]
    for i in frag:
        if i == letter:
            c = c + 1
    print c

count_from('o','doodle',2)

print 'banana'.count('a') # using built-in count method
print 'banana'.upper()
print 'BANANA'.lower()

# Ex. 8.9
def is_palindrome(word):
    return word == word[::-1]

print is_palindrome('noon')

# Ex. 8.10
word = '            s p a  c   e    d         out           !'
print word
new_word = word.strip().replace(' ','') 
# I can use multiple methods in one line
# Note: lstrip() and rstrip() methods only removes leading or
# trailing instances of the given characters
# use strip() to remove all instances
print 'not '+new_word.replace('out','').replace('!','')
