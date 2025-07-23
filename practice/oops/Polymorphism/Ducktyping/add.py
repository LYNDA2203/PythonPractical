#duck_typing:enabling the function regardless of object and datatype
def add(a,b):
    return a + b

print(add(3,4))#integer object
print(add("hello,","World!"))#string object
print(add([1,2],[3,4]))#list comprehension

