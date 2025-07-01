lst1=[1,2,3,4,5,6]
lst2=[1,7,8,9,5,6]

diff_list1_list2=list(set(lst1)-set(lst2))
diff_list2_list1=list(set(lst2)-set(lst1))

total_diff=(diff_list1_list2)+(diff_list2_list1)
print(total_diff)