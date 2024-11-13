from functools import reduce 

def clamp(xs, x): 
    newxs= list(map(lambda y: x if y > x else y, xs))
    print(newxs)  
    return list(map(lambda y: x if x > y else None, xs))
def maxevens(xs):
    newxs = list(filter(lambda y: y if y %2 == 0 else 0, xs))
    final = reduce(lambda x, y: x if x >y else y, xs)
    print(final)
def skip(xs):
    if len(xs)== 0: 
        return 0
    else: 
        newxs = xs[0]
        rest = xs[2:]
        print(newxs)
        return newxs + skip(rest)
def functionf(xs):
    return xs[0] * xs[0]
    
if __name__ == '__main__':
    a = [1,2,3,4,-5]
    clamp(a, 2)
    maxevens(a)
    skip(a)
    print(a)
   # result = maxf(a, functionf)
   # print(result)