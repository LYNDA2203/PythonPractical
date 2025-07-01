num_list = [1,2,3,4,5]
num_tuple = (1,2,3,4,5)

print(f"Original list and tuple: \n{num_list} \n{num_tuple}")
result_list=list(map(str,num_list))
result_tuple=tuple(map(str,num_tuple))

print("\nList of strings:")
print(result_list)

print("\nString of tuple")
print(result_tuple)