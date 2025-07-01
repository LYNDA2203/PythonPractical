lst=[1,2,3,4,5,6,7,8,9]
n=len(lst)
for i in range(n//2):
    lst[i],lst[n-i-1]=lst[n-i-1],lst[i]
print(lst)