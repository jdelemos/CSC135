##Write a function named collapse that accepts 
#a list of integers as a parameter and returns 
#a new list where each pair of integers from the 
#original list has been replaced by the sum of that 
# pair. For example, if a list called a stores [7, 2, 8
# , 9, 4, 13, 7, 1, 9, 10], then 
# the call of collapse(a) should return a new list containing
# [9, 17, 17, 8, 19]. The first pair from the original list 
# is collapsed into 9 (7 + 2), the second pair is collapsed 
# into 17 (8 + 9), and so on.
# If the list stores an odd number of elements, the element is not collapsed. 
# For example, if the list had been [1, 2, 3, 4, 5], then the call would return 
# [3, 7, 5]. Your function should not change the list that is passed as a parameter.

num = [1,2,3,4,5,6,7]


def collapse(num):
    tish = len(num)
    print(num[tish -1])
    print(tish)
    even = len(num)%2
    div = (len(num) -1) / 2 
    other = slice(len((num))/2)
    (num[::2])
    result = []
    
    for i in range(0,len(num)-1, 2):
        result.append(num[i]+ num[i+1])
    if even == 1: 
        result.append(num[i-1])
        
    print(result)
        
    


            
            
        
        
    
collapse(num)
