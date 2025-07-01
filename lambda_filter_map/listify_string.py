def listify_string(colour):
    print("The original list:",colour)
    listify_string=map(list,colour)
    return list(listify_string)
colour=['Red', 'Blue', 'Black', 'White', 'Pink']
print("list after the listify:")
result=listify_string(colour)
print(result)
