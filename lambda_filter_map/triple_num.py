def triple_number(lst):
    print("Original List:",lst)
    triple_num=list(map(lambda x:x*3,lst))
    return triple_num

result=triple_number([1,2,3,4,5])
print("\nTriple of list:")
print(result)