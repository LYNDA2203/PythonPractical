def add_three_list(lst1,lst2,lst3):
    print(f"original lists: \n{lst1} \n{lst2} \n{lst3}")
    summation_lists=list(map(lambda x,y,z:x+y+z,lst1,lst2,lst3))
    return summation_lists
lst1=[1,2,3,4,5]
lst2=[5,6,7,8,9]
lst3=[3,4,5,6,7]
print(add_three_list(lst1,lst2,lst3))
