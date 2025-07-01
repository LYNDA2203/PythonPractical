from functools import reduce

lst = [1,2,3,4,5,6]
multiply=reduce(lambda x,y:x*y,lst)
print(multiply)