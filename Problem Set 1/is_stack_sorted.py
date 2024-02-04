## The following stack is not
# sorted (the 15 is out of place), 
# so passing it to your function should 
# return a result of False:

num = [1]

def is_stack_sorted(num):
    i = (len(num)) -1
    
    if i == 1:
        True 
    
   
    while num[i-1] >= num[i]:
        print(num[i])
        if i - 1 == 0 :
            print(i)
            return True
        i = i -1
    if num[i-1] == num[i]:
        return true
    else: 
        return False 
    
        
is_stack_sorted(num)
    
    
