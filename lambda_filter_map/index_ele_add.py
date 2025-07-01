nums=[10,20,30,40]
result=list(map(lambda index : index[0] + index[1] ,enumerate(nums)))
print(result)