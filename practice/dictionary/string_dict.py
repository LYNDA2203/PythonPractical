def str_to_dict(lst):
   #return{item.split('=')[0]:item.split('=')[1] for item in lst}
    #return dict(item.split('=') for item in lst)    
    return {k:v for (k,v) in map(lambda x: x.split('='),lst)}
print(str_to_dict(["1=one", "2=two", "3=three", "4=four"]))