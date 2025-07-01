lst=[(1, 4), (3, 1), (5, 9), (2, 0)]
sort_sec_ele = sorted(lst,key = lambda x: x[1])
print(sort_sec_ele)

def sort_sec_ele(lst):
    sort=sorted(lst,key = lambda x: x[1])
    
print(sort_sec_ele([(1, 4), (3, 1), (5, 9), (2, 0)]))