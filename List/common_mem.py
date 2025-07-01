def common_mem(lst1,lst2):
    for item in lst1:
        if item in lst2:
            return True
    else:
        return False
print(common_mem([1,2,3,4,5,6],[7,8,9,10,11,12]))