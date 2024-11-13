# reverse.py by Jonathon Delmeos (jdelemos@csus.edu) for CSC 135 Fall 2024
# Implements List135
# Worked with Ted Krovetz
# No AI or online resources, I referred to the lecture notes. 

from List135 import List135

# Returns a List135 that is the same as xs but in reverse order
# Function is tail-recursive to enable compiler optimization
# [] --> []; [1] --> [1]; [1,2] --> [2,1]; [1,2,3] --> [3,2,1]; etc.
def _reverse(xs, acc):
    if xs.empty() == True: 
        return acc
    else: 
        first = xs.first() 
        newxs = xs.rest()
        acc = acc.add(first)
        return _reverse(newxs, acc)

def reverse(xs):
    acc = List135()
    return _reverse(xs, acc)  # Begin accumulation with an empty list

# If you run this file, the indented code below will run. This is a
# suitable place for you to put testing code. When I test your code
# using a separate file, the code below will not be run. to be eligible
# for credit, your code must run the following without sytax or runtime
# errors. Leave your test cases here, indented, so that I can see them.
if __name__ == '__main__':
    a = List135().add(3).add(1).add(5).add(2).add(4)
    b = reverse(a)
    print(a)
    print(b)