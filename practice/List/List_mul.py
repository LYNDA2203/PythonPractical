def List_Multiply(num,len):
    res=[]
    for i in range(1,len+1):
        res.append(num*i)
    return res
output=List_Multiply(10,15)
print(output)