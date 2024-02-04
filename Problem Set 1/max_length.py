#Write a function max_length that accepts as a 
#parameter a set of strings, and that returns the length 
#of the longest string in the set. If your function 
#is passed an empty set, it should return 0.

words=['xxx', 'yyyyy', 'ppppppp','ddddddddddddddddd']

def max_length(words):
    greatest = 0
    for word in words:
        if len(word) > greatest:
            greatest = len(word)
            answer = len(word)
           
    print(answer)
    
max_length(words)

            