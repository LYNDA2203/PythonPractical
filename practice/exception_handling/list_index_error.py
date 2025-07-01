def list_index_error(lst,index):
    try:
        result = lst[index]
        print("Result:",result)
    
    except IndexError:
        print("Error: index out of boundary")
        
lst=[1,2,3,4,5,6,7]
index=int(input("Enter the index:"))
list_index_error(lst,index)