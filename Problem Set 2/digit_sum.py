import math 
s = [13,27,1,-4]

def stutter_list(s): 
    g = s.pop()
    x = g
    print(x)
    s.append(x)
    return stutter_list(s)

    
stutter_list(s)


