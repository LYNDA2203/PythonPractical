import numpy as np

#arr = np.array([1,2,3,4,5,4,4])
# x = np.where(arr == 4)
# for num in x:
#     print(num)
#o/p:
    #[3 5 6]
    
arr = np.array([1,2,3,4,5,6,7,8])
# x = np.where(arr % 2 == 0)
# print(x)
# o/p:
#     (array([1, 3, 5, 7]),)

# arr = np.array([1,2,3,4,5,6,7,8])
# x = np.where(arr%2 == 1)
# print(x)
# o/p:
#     (array([0, 2, 4, 6]),)

# arr = np.array([6,7,8,9,7,10])
# x = np.searchsorted(arr,7)
# print(x)
# o/p:
#     1# it inserts before the 7

# arr = np.array([6,7,8,9])
# x = np.searchsorted(arr,7,side = 'right')
# print(x)
# o/p:
# 2 # it inserts after the value of 7

#***********sort*************
# arr = np.array([3,4,2,1])
# print(np.sort(arr))
# o/p:
#   [1 2 3 4]

# arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr))
#o/p:
#   ['apple' 'banana' 'cherry']

# arr = np.array([True, False, True])
# print(np.sort(arr))
#o/p:
#   [False  True  True]

# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))
#o/p:
#   [[2 3 4]
#   [0 1 5]]    

#***********Filter***********
# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr)
# o/p:
#     [41 43]

# arr = np.array([41,42,43,44])
# filter_arr = []
# for ele in arr:
#     if ele > 42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
        
# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

# o/p:
#     [False, False, True, True]
#     [43 44]

#*********Direct filtering******
# arr = np.array([41,42,43,44])
# filter_arr = arr > 42
# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

# arr= np.array([1,2,3,4,5,6,7])
# filter_arr = arr % 2 == 0
# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

#*********Arrage*******

arr = np.arange(0,10)
print(arr)

arr = np.arange(1,10,2)
print(arr)