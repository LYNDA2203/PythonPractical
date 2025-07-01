def get_indices(lst,ele):
    # res=[]
    # for i in range(len(lst)):
    #     if lst[i] == ele:
    #         res.append(i)
    # return res
    return [idx for idx, i in enumerate(lst) if i == ele]
    

print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
    