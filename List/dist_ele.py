def two_distinct_elements(lst):
    unique_list=[]
    for i in lst:
        if lst.count(i) == 1 and i not in unique_list:
            unique_list.append(i)
    return unique_list
 
print(two_distinct_elements([1, 9, 8, 8, 7, 6, 1, 6]))
            