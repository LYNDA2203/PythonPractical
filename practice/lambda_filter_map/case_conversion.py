def change_case(s):
    return str(s).upper(),str(s).lower()
chars= {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print("Original Charcters:\n",chars)
result=map(change_case,chars)
print("\nAfter converting above characters in upper and lower cases \nand eliminating duplicate letter:")
print(set(result))