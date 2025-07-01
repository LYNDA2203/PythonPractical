def add_sub(x,y):
    return x+y,x-y

lst1 = [1,2,3,4,5,6]
lst2 = [5,6,7,8,9,1]

print(f"Original lists:\n{lst1}\n{lst2}")
result = list(map(add_sub,lst1,lst2))

print("The list of subtraction and addition:")
print(result)
