#adding the elements to the first list if we pass as a collection or if we pass a element append the element
add_ele= lambda lst,ele : lst+[ele] if isinstance(ele,(int,float,complex)) else lst + ele
print(add_ele([1,2,3,4,5],[6,7,8,9]))
print(add_ele([1,2,3,4,5],44))