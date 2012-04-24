# Chapter 14

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
"""def use_walk(startdir):
    import os
    (dirpath, dirnames, filenames) = 
"""
import os
(a,b,c) = os.walk('/home/kyle/PHYS200-2')
