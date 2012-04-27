# Chapter 14

# Sections 14.1 to 14.4 Practice

def write_file(destdir,name):
    import os
    cwd = os.getcwd()
    if cwd != destdir:
        os.chdir(destdir)
    fout = open(destdir+'/'+name,'w')
    pre = ''
    if name[-4:] == '.txt':
        line1 = 'New text file \n'
    elif name[-3:] == '.py':
        line1 = '# New python code file \n'
        pre = '# '
    else:
        line1 = 'New file \n'
    fout.write(line1)
    count = 0
    for c in destdir:
        if c == '/':
            count = count+1
    line2 = pre+'This file is %d subdirectories down. \n' % (count)
    fout.write(line2)
    fout.close

write_file('/home/kyle/PHYS200-2','new_file.py')


# Ex. 14.1
def walk(startdir):
    import os
    files_in_this_level = [startdir+'/:']
    for name in os.listdir(startdir):
        path = os.path.join(startdir,name)
        if os.path.isfile(path):
            files_in_this_level.append(name)
        else:
            walk(path)
    print files_in_this_level

walk('/home/kyle/PHYS200-2')

# Ex. 14.2
def use_walk(startdir):
    import os
    import string
    for (dirpath, dirnames, filenames) in os.walk(startdir):
        for filename in filenames:
            print '/'.join([dirpath,filename])

use_walk('/home/kyle/PHYS200-2')

# Ex. 14.3

def match_anagrams():
    import string
    fin = open('words.txt')
    anagdict = {}
    flag = 'AA'
    while flag < 'zymurgieA': # Create dictionary with anagram words
# in a list as the value, with the key a list of the letters used in
# alphabetical order
        word = fin.readline().strip()
        print word
        letterlist = list(word)
        letterstring = ''
        letterlist.sort()
        print letterlist
        for e in letterlist:
            letterstring = letterstring + e
        anagdict.setdefault(letterstring,[]).append(word)
        flag = word
#    import anydbm
#    anagdb = anydbm.open('anagramdata.db','c')
#    for k in anagdict:
#        if len(anagdict[k]) > 1:
            

match_anagrams()
