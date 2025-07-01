n=30
lst=[]
for i in range(1,n+1):
    lst.append(i**2)

res=lst[:5] + lst[-5:]
print(res)
  
