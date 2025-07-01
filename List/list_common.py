lst1=[1,2,3,4,5,6]
lst2=[4,5,6,7,8,9]
res=[]
for i in lst1:
    for j in lst2:
        if i == j:
             res.append(i)
print(res)