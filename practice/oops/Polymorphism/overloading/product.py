#@dispatch--> it helps to increase the parameters count
from multipledispatch import dispatch
@dispatch(int,int)
def product(first,sec):
    return first * sec

@dispatch(int,int,int)
def product(first,sec,third):
    return first * sec * third

@dispatch(float,float,float)
def product(first,sec,third):
     return first * sec * third
 
print(product(2,3))
print(product(4,5,6))
print(product(2.3,4.5,6.7))
    
    
