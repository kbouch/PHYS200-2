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
    for i in s[b:]:
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

