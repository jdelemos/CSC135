## Write a function named average_length of code that 
# computes and returns the average string length of the 
# elements of a list of strings. For example, 
# if the list contains ["belt", "hat", "jelly", "bubble gum"], 
# the average length returned should be 5.5. 
# Assume that the list has at least one element. 

def average_length(x):
    total = 0
    size = len(x)
    for char in x:
        total += len(char)  
    answer = total / size  
    return answer


        
        
        
        