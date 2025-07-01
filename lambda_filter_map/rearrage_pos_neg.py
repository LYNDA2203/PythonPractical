lst=[-1, 2, -3, 5, 7, 8, 9, -10]
sorted_list=sorted(lst,key=(lambda x: x < 0))
print(sorted_list)