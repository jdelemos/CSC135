# reverse.py by Jonathon Delmeos (jdelemos@csus.edu) for CSC 135 Fall 2024
# Implements List135
# Worked with Ted Krovetz
# No AI or stackoverflow, this code was built using the lecture notes. 


from List135 import List135

# Returns how many times x is found inside List135 xs (uses == to test equality)
# Your function must be recursive but it doesn't have to be tail-recursive.
# (For practice you may want to try both tail and non-tail, but turn in only
# one function called count.)
# [], 1 --> 0; [1], 1 --> 1; [1,2], 1 --> 1; [1,2,1], 1 --> 2; etc.
def count(xs, x, acc=0):
    if xs.empty()== True:
        return acc
    else: 
        newx = xs.first() 
        if newx == x:
            acc = acc+1
        newxs = xs.rest()
        return count(newxs, x, acc)
             
    

# If you run this file, the indented code below will run. This is a
# suitable place for you to put testing code. When I test your code
# using a separate file, the code below will not be run. to be eligible
# for credit, your code must run the following without sytax or runtime
# errors. Leave your test cases here, indented, so that I can see them.
if __name__ == '__main__':
    a = List135().add(1).add(2).add(1).add(1)
    print(count(a, 1) == 3)
    
