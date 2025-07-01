array_3d=[]
for i in range(3):
    array1=[]
    for j in range(4):
        array2=[]
        for k in range(6):
            array2.append('*')
        array1.append(array2)
    array_3d.append(array1)

for row in array_3d:
    print(row,end = ' ')