def sum_list_elements_except_itself(lst):
    output = []
    for i in range(len(lst)):
        sum = 0
        for j in range(len(lst)):
            if i != j:
               sum += lst[j]
        output.append(sum)
    return output
        
print(sum_list_elements_except_itself([1,2,3,4,5]))