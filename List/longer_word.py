n=3
lst=[]
s="The sun rises in the east"
txt=s.split(" ")
for i in txt:
    if len(i) > n:
        lst.append(i)
print(lst)