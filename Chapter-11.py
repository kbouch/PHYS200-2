# Chapter 11

import sys
sys.path.append('/home/kyle/Downloads/epd-7.2-2-rh5-x86/lib/python2.7/site-packages/swampy-2.0')
print sys.path

# Ex. 11.1
def make_dict(d):
    fin = open('words.txt')
    while True:
        line = fin.readline()
        word = line.strip()
        if word in d:
            break
        d[word] = len(word)

words = dict()
make_dict(words)
print 'hello' in words

# Ex. 11.2
def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d
print histogram('yellow')

# Ex. 11.3

def print_hist(s):
    h = histogram(s)
    l = h.keys()
    l.sort()
    for k in l:
        print k, h[k]

print_hist('nocturnal')

# Ex. 11.4
def reverse_lookup(d,v):
    r = []
    for k in d:
        if d[k] == v:
            r.append(k)
    return r

print reverse_lookup(histogram('trees'),1)

# Ex. 11.5
def invert_dict(d):
    inv = dict()
    for k in d:
        inv.setdefault(d[k],[])
        inv[d[k]].append(k)
    return inv

print invert_dict(histogram('yellow'))
print invert_dict(histogram('yellow'))
