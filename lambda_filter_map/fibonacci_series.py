from functools import reduce

def fibonacci_serie(n):
    return reduce(lambda x,_: x+(x[-1]+x[-2]),range(n-2),[0,1])

