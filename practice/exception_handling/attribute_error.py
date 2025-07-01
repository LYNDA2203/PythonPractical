def list_operation(lst):
    try:
        r=lst.length
        print("Length of the lists:",r)
    except AttributeError:
        print("error: the list does not have a 'length' attribute")
        
lst = [1,2,3,4,5]
list_operation(lst)