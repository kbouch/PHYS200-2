# Chapter 13: Case Study: Data Structure selection

# Ex. 13.1
def separate_text(fname):
    """ Opens a file in the current directory that is specified, with
        it's name as a string in the argument. Then returns a 
        single list containing all the words in the file in lower
        case, in order.
    """
    import string
    fin = open(fname)
    wordlist_of_file = []
    line = fin.readline()
    while line != '':
        for c in string.punctuation:
            line = line.replace(c,'')
        for c in string.whitespace:
            line = line.replace(c,' ')
        wordlist = line.split(' ')
        for i in range(0,len(wordlist)):
            wordlist[i] = wordlist[i].lower()
        wordlist_of_file = wordlist_of_file + wordlist
        line = fin.readline()
    return wordlist_of_file
print separate_text('sampletext.txt')


# Ex. 13.2

def read_book(fname,start):
    """ Returns a list of strings of the words in a file, in order,
        in lower case, after removing all the punctuation and
        whitespace. The start parameter is the line that you want to
        start on in the file.
    """
    import string
    fin = open(fname)
    wordlist_of_file = []
    for i in range(0,start):
        line = fin.readline()
    line = fin.readline()
    while line != 'LETTER TO M. DAELLI':
        for c in string.punctuation:
            line = line.replace(c,'')
        for c in string.whitespace:
            line = line.replace(c,' ')
        wordlist = line.split(' ')
        for i in range(0,len(wordlist)):
            wordlist[i] = wordlist[i].lower()
            print wordlist[i]
        wordlist_of_file = wordlist_of_file + wordlist
        line = fin.readline()
    return wordlist_of_file

def count_book_words(fname,start):
    t = read_book(fname,start)
    h = dict()
    for i in t:
        print h[i]
        h[i] = h[i].get(i,0) + 1
    return (h, len(h), len(t))

# These lines took too line to execute...
# print read_book('Les_Miserables.txt',625)
# or
# (histogram, diversity, count) = count_book_words('Les_Miserables.txt',625)
# print 'word diversity: ',diversity, 'word total count: ',count
# 67 thousand lines long. Taking forever to process....
# Memory that the python process is taking going 
# up slowly by tenths of a megabyte. it is at 19.3 MiB after 20
# minutes. It isn't finished after over 30 minutes?
# Taking up a whole cpu for itself.


# Here is a version that only reads a specified number of lines

def read_book_2(fname,start,end):
    """ Returns a list of strings of the words in a file, in order,
        in lower case, after removing all the punctuation and
        whitespace. The start and end parameters are the lines that
        you want to start and end on when processing the file.
    """
    import string
    fin = open(fname)
    wordlist_of_file = []
    for i in range(0,start):
        line = fin.readline()
    line = fin.readline()
    for i in range(start,end+1):
        for c in string.punctuation:
            line = line.replace(c,'')
        for c in string.whitespace:
            line = line.replace(c,' ')
        wordlist = line.split(' ')
        for i in range(0,len(wordlist)):
            wordlist[i] = wordlist[i].lower()
            print wordlist[i]
        wordlist_of_file = wordlist_of_file + wordlist
        line = fin.readline()
    return wordlist_of_file

def count_book_words_2(fname,start,end):
    t = read_book_2(fname,start,end)
    h = dict()
    for i in t:
        h[i] = h[i].get(i,0) + 1
    return (h, len(h), len(t))

# print read_book_2('Les_Miserables.txt',625,1625)
# I don't know why my loops do not end when I run the above line.

#(histogram, diversity, count) = count_book_words_2('Les_Miserables.txt',625,1625)
#print 'word diversity: ',diversity, 'word total count: ',count


# Ex. 13.3
def top_twenty_used(h):
    l = len(h)
    if l < 20:
        values = h.values()
        keys = h.keys()
    for k,v in zip(keys,values):
        print (k, v)
    else:
        t = h.items()
        t.sort(reverse=True)
        for i in range(0,20):
            print t[i][0], t[i][1]

(histogram, diversity, count) = count_book_words('sampletext.txt',1)
top_twenty_used(histogram)

# Ex. 13.4
def check_words(h):
    fin2 = open('words.txt')
    w = []
    flag = 'AA'
    while flag < 'zymurgieA':
        line = fin2.readline()
        word = line.strip()
        w.append(word)
        flag = word
    keys = h.keys()
    for k in keys:
        if not k in w:
            print k

# Ex. 13.9
