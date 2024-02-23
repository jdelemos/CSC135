# Persistent list data structure for Sac State CSC 135 by Ted Krovetz
# Adding is done only at front of list, maintaining existing views.


#class list for exam, to review 
class List135:
    
    # create new list node. Defaults to a node representing the empty list
    def __init__(self, initdata=None, initnext=None):
        self._data = initdata
        self._next = initnext
    
    # is the list beginning with self the end of the list?
    def empty(self):
        return self._next == None
    
    # return the first element of the list that starts with self
    def first(self):
        return self._data
    
    # return the list that begins after the list that starts with self
    def rest(self):
        return self._next
    
    # return a list beginning with data, followed by list beginning with self
    def add(self, data):
        return List135(data, self)
    
    # tail-recursively accumulates "," + str(cur._data) for each remaining item
    def _str(self, cur, acc):
        if cur._next == None:
            return acc
        else:
            nextacc = acc + "," + str(cur._data)
            nextcur = cur._next
            return self._str(nextcur, nextacc)
    
    def __str__(self):
        if self._next == None:
            return "[]"
        else:
            acc = str(self._data)   # init accumulator with first item
            cur = self._next        # continue accumulation with next
            return "[" + self._str(cur, acc) + "]"

# The following is a trick to make this testing code be ignored
# when this file is being imported, but run when run directly
# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    a = List135()  # a --> []
    b = a.add(1)   # b --> [1]
    c = b.add(2)   # c --> [2,1]
    print(a)
    print(b)
    print(c)
    
    
    #1 solve
    f = lambda x,y: y + ", " + x
    
    #Define a lambda expression named f 
    # that accepts two integer parameters and 
    # returns the larger of the two; for example, 
    # if passed 4 and 11, it would return 11. Do not 
    # write an entire function; just write a statement of the form:
    f = lambda x,y: x if x > y else y
    
    
    #3 solve
    #Define a lambda expression named f 
    # that accepts an integer parameter and 
    # converts it into the square of that 
    # integer; for example, if 4 were passed, 
    # your lambda would return 16. Do not 
    # write an entire function; just write 
    # a statement of the form:
    f = lambda x: x*x
    
    #4 solve 
    #question prevented from being shared by codeStepbyStep
    output = [10, 28, 33, 28, 49, 56, 49]    
    
    #5 solve 
    #same as 4
    answer = [10, -28, 28, 56]
    
    #5 solve 
    #Write a function named abs_sum that takes a list of integers as a parameter and returns the sum of the absolute values of each element in the list. For example, the absolute sum of [-1, 2, -4, 6, -9] is 22. If the list is empty, return 0.
    #Use Python's functional programming constructs, such as list comprehensions, map, filter, reduce, to implement your function. Do not use any loops or recursion in your solution.

    def abs_sum(n): 
        f = reduce(lambda a, b: a + abs(b), n, 0)
        return f
    #most of these answers are veryyy short in terms of code, but require super specific methods 
    
    #6
    #Write a function named count_negatives that takes a list of integers as a parameter and returns how many numbers in the list are negative. For example, if the list is [5, -1, -3, 20, 47, -10, -8, -4, 0, -6, -6], you should return 7.
    #Use Python's functional programming constructs, such as list comprehensions, map, filter, reduce, to implement your function. Do not use any loops or recursion in your solution.
    import functools

    def count_negatives(n):
        numbers = functools.reduce(lambda x, n: x+1 if n < 0 else x, n, 0)
        return numbers

    #7Write a function named double_list that takes a list as a parameter and returns a list of integers that contains double the elements in the initial list. For example, if the initial list is [2, -1, 4, 16], you should return [4, -2, 8, 32].
    #Use Python's functional programming constructs, such as list comprehensions, map, filter, reduce, to implement your function. Do not use any loops or recursion in your solution.
    def double_list(n):
        numbers = map(lambda x:x*2, n)
        return list(numbers)
    
    
    #8Write a function called four_letter_words accepts a string representing a file name as a parameter and returns a count of the number of words in the file that are exactly four letters long. Words are separated by whitespace. Do not worry about punctuation; look for any four-character token.
    #Use Python's functional programming constructs, such as list comprehensions, map, filter, reduce, to implement your function. Do not use any loops or recursion in your solution.
    def four_letter_words(filename):
        try:
            with open(filename, 'r') as file:
            # Read the entire content of the file into a string
                file_content = file.read()
            
            # Split the content into words
                words = file_content.split()
            
            # Count the number of four-letter words using map and lambda function
                count = sum(map(lambda word: 1 if len(word) == 4 else 0, words))
            
                return count
        except FileNotFoundError:
            print("File not found:", filename)
            return -1  # Return -1 to indicate file not found
