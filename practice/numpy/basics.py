import numpy as np 

#***********datatype**************

# arr = np.array([1,2,3,4,5,6])
# print(arr.dtype) #o/p:int64---- dtype---->datatype

# arr = np.array(["apple","banana","mango"])
# print(arr.dtype) #o/p:<u6---->unicode "banana" with length ==>6

# arr = np.array([1,2.5,"hello"])
# print(arr.dtype) #<u32 all is converted as string

# arr = np.array([1,2,3,4,5],dtype = 'S')
# print(arr)
# print(arr.dtype) 
#o/p:[b'1' b'2' b'3' b'4' b'5']---->b==>byte
#     |S1

# arr = np.array(["hello","world"],dtype = 'S')
# print(arr)
# print(arr.dtype)

#*********view,copy,base***********

# arr = np.array([1,2,3,4,5])
# x = arr.view()
# y = arr.copy()
# x[0] = 31
# y[1] = 41

# print(arr)#[31,2,3,4,5]
# print(x)#[31,2,3,4,5] ===>view ---->it will modify original list
# print(y)#[1,41,3,4,5]====>copy ---->it create new list with modification
# print(x.base)#it dnt store..so it returns the original list
# print(y.base)#it returns none since it stores

#*******shapes********
# arr = np.array([[1,2,3,4,5],[5,6,7,8,9]])
# print(arr.shape)#(2, 5)

# arr = np.array([1,2,3,4,5],ndmin = 5)
# print(arr)
# print("Shape of array:",arr.shape) #o/p: Shape of array: (1, 1, 1, 1, 5)

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# new_arr = arr.reshape(4,3)
# print(new_arr)
# o/p:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# new_arr = arr.reshape(2,3,2)
# print(new_arr)
# o/p:
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]

#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr.reshape(2,6).base)

#**********iterating************
# arr = np.array([1,2,3])
# for x in arr:
#     print(x)
    
# arr = np.array([[1,2,3],[4,5,6]])
# for x in arr:
#     for y in x:
#         print(y)
        
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in np.nditer(arr):
#     print(x)


#arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in np.nditer(arr,flags = ['buffered'],op_dtypes = ['S']):
#     print(x)
    
# for ind,x in np.ndenumerate(arr):
#     print(ind,",",x)
    
# o/p:
#     (0, 0, 0) , 1
#     (0, 0, 1) , 2
#     (0, 0, 2) , 3
#     (0, 1, 0) , 4
#     (0, 1, 1) , 5
#     (0, 1, 2) , 6
#     (1, 0, 0) , 7
#     (1, 0, 1) , 8
#     (1, 0, 2) , 9
#     (1, 1, 0) , 10
#     (1, 1, 1) , 11
#     (1, 1, 2) , 12


# it =np.nditer(arr,flags = ['multi_index'])    
# for x in it:
#     print(x,it.multi_index)
# o/p:
#    1 (0, 0, 0)
#     2 (0, 0, 1)
#     3 (0, 0, 2)
#     4 (0, 1, 0)
#     5 (0, 1, 1)
#     6 (0, 1, 2)
#     7 (1, 0, 0)
#     8 (1, 0, 1)
#     9 (1, 0, 2)
#     10 (1, 1, 0)
#     11 (1, 1, 1)
#     12 (1, 1, 2)   

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in np.nditer(arr[:,::2]):#arr[row,column]
#     print(x)
# o/p:
#     1
#     3
#     4
#     6   

# arr1 = np.array([[1,2],[3,4]])
# arr2 = np.array([[5,6],[7,8]])
# arr = np.concatenate((arr1,arr2),axis=1)
# print(arr)
# o/p:
#     [[1 2 5 6]
#     [3 4 7 8]]
    
# arr1 = np.array([[1,2],[3,4]])
# arr2 = np.array([[5,6],[7,8]])
# arr = np.concatenate((arr1,arr2),axis=0)
# print(arr)
# o/p:
#     [[1 2]
#     [3 4]
#     [5 6]
#     [7 8]]

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr = np.stack((arr1,arr2),axis = 1)
# print(arr)
# o/p:
#     [[1 4]
#     [2 5]
#     [3 6]]


# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr =  np.stack((arr1,arr2),axis = 0)
# print(arr)
# o/p:
#     [[1 2 3]
#     [4 5 6]]

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.hstack((arr1,arr2))
# print(arr)

# o/p:
#    [1 2 3 4 5 6]
 
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 8, 9])
# arr = np.vstack((arr1,arr2))
# print(arr)
# o/p:
#     [[1 2 3]
#     [4 8 9]]

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.dstack((arr1,arr2))
# print(arr)
# o/p:
#     [[[1 4]
#     [2 5]
#     [3 6]]]


# arr = np.array([1,2,3,4,5,6])
# newarr = np.array_split(arr,3)
# print(newarr)
# o/p:
#     [array([1, 2]), array([3, 4]), array([5, 6])]

# arr = np.array([1,2,3,4,5,6])
# newarr =np.array_split(arr,4)
# print(newarr)
# o/p:
#     [array([1, 2]), array([3, 4]), array([5]), array([6])]

# arr = np.array([1,2,3,4,5,6])
# newarr = np.array_split(arr,3)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])
# o/p:
#     [1 2]
#     [3 4]
#     [5 6]

# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# newarr = np.array_split(arr,3)
# print(newarr)
# o/p:
#     [array([[1, 2],
#        [3, 4]]), array([[5, 6],
#        [7, 8]]), array([[ 9, 10],
#        [11, 12]])]

# arr =np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.array_split(arr,3)
# print(newarr)
# o/p:
#     [array([[1, 2, 3],
#        [4, 5, 6]]), array([[ 7,  8,  9],
#        [10, 11, 12]]), array([[13, 14, 15],
#        [16, 17, 18]])]

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# newarr = np.hsplit(arr,3)
# print(newarr)
# o/p:
#     [array([[1],
#        [4],
#        [7]]), array([[2],
#        [5],
#        [8]]), array([[3],
#        [6],
#        [9]])]
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# newarr = np.vsplit(arr,3)
# print(newarr)
# o/p:
#     [array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]])]

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],[10,11,12]])
arr1=arr.reshape(4,1,3)
newarr = np.dsplit(arr1,3)
print(newarr)
# o/p:
#  [array([[[ 1]],
    #    [[ 4]],
    #    [[ 7]],
    #    [[10]]]), array([[[ 2]],
    #    [[ 5]],
    #    [[ 8]],
    #    [[11]]]), array([[[ 3]],
    #    [[ 6]],
    #    [[ 9]],
    #    [[12]]])]