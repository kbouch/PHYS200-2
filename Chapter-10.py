# Ex. 10.1

def cumulative_sum(t):
    new = []
    for i in range(len(t)):
        new.append(sum(t[:(i+1)]))
    return new

numbers = [1,2,3,4,5,6,7,8,9,10]

sums = cumulative_sum(numbers)
print sums
print type(sums)

# Ex. 10.2

def chop(t):
    l = len(t)
    del t[0]
    del t[len(t)-2]

t = ['a','b','c','d','e','f','g']
print t
chop(t)
print t


def middle(t):
    return t[1:len(t)-1]

print middle([1,2,3,4,5,6,7,8,9])

# Ex. 10.3
def is_sorted(t):
    previous = t[0]
    for element in t[1:]:
        if previous > element:
            return False

        previous = element
    return True

print is_sorted([0,1,2,3,4,5,6,7,8,9])
print is_sorted(['a','c','h','j'])
print is_sorted([3,2,1])
print is_sorted(['h','h','d','e'])

# Ex. 10.4
def is_anagram(a,b):
    checklist = list(a)
    for element in list(b):
        if element in checklist:
            checklist.remove(element)
    if checklist == []:
        return True
    else:
        return False

print is_anagram('read','dear')
print is_anagram('table','bleat')
print is_anagram('yellow','orange')

