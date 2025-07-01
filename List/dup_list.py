lst=[1,2,3,4,1,2,6,7]
uniq_list=[]
for i in lst:
    if i not in uniq_list:
        uniq_list.append(i)
print(uniq_list)