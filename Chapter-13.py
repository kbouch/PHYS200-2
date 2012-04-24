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
            line = line.replace(c,'') # replaces all occurences, not
# just leading and trailing like strip does.
        for c in string.whitespace:
            line = line.replace(c,' ')
        wordlist = line.split() # uses any whitespace as delimeter, 
# and excludes empty strings from the list
        for i in range(0,len(wordlist)):
            wordlist[i] = wordlist[i].lower()
        wordlist_of_file = wordlist_of_file + wordlist
        line = fin.readline()
    return wordlist_of_file
print separate_text('sampletext.txt')

# a better version would keep punctuation that is part of a word or
# phrase. I should split() first, then strip leading and trailing
# punctuation

def separate_text_2(fname):
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
        for c in string.whitespace:
            line = line.replace(c,' ')
        wordlist = line.split()
        for i in range(0,len(wordlist)):
            wordlist[i] = wordlist[i].lower().strip(string.punctuation)
        wordlist_of_file = wordlist_of_file + wordlist
        line = fin.readline()
    return wordlist_of_file
print 'this version includes punctuation that is part of the word or phrase:'
print separate_text_2('sampletext.txt')


# Ex. 13.2

# This was my first version, but I improved it below.
# See comments below
def read_book(fname,start):
    """ Returns a list of strings of the words in a file, in order,
        in lower case, after removing all the punctuation and
        whitespace. The start parameter is the line that you want to
        start on in the file.
    """
    import string
    fin = open(fname)
    wordlist_of_file = []
    for i in range(0,start): # remember, the range function excludes
# the last argument given from the sequence it creates.
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


# Here is a version that only reads a specified number of lines, and
# I will use the word separator separate_text_2 that includes 
# punctuation that is in the middle of the word or phrase

def read_book_2(fname,start,end):
    """ Returns a list of strings of the words in a file, in order,
        in lower case, after removing sentence punctuation and
        whitespace. The start and end parameters are the lines that
        you want to start and end on when processing the file.
    """
    import string
    fin = open(fname)
    wordlist_of_file = []
    for i in range(0,start):
        line = fin.readline()
    for i in range(start,end+1):
        line = fin.readline()
        for c in string.whitespace:
            line = line.replace(c,' ')
        wordlist = line.split()
        for i in range(len(wordlist)-1,-1,-1):
            wordlist[i] = wordlist[i].lower().strip(string.punctuation)
            if wordlist[i] == '':
                del wordlist[i]
        wordlist_of_file = wordlist_of_file + wordlist
    return wordlist_of_file

def count_book_words_2(w):
    """ Returns a tuple: (histogram, number of different words used,
        total words used) , given a list of words.
    """
    h = dict()
    for word in w:
        h[word] = h.get(word,0) + 1
    return (h, len(h), len(w))
LesMisProcessed = read_book_2('Les_Miserables.txt',625,10000)
print LesMisProcessed

(histogram, diversity, count) = count_book_words_2(LesMisProcessed)
print 'word diversity: ',diversity, 'word total count: ',count


# Ex. 13.3
def top_twenty_used(h):
    l = len(h)
    if l < 20:
        end = l
    else:
        end = 20
    vals = h.values()
    vals.sort(reverse=True)
    keyz = []
    for v in  vals[0:20]:
        for k in h:
            if h[k] == v:
                keyz.append(k)
    return keyz


(histogram, diversity, count) = count_book_words_2(read_book_2('Les_Miserables.txt',625,1625))
print 'Top Twenty Words, with most commmon first:', top_twenty_used(histogram)

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

check_words(histogram)

# Ex. 13.9
"""def 
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
"""
