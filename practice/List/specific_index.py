lst=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
specific_index=[0,4,5]
new_list=[]
for i in range(len(lst)):
    if i not in specific_index:
        new_list.append(lst[i])
print(new_list)