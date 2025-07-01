#from operator import itemgetter
lst=[(2,5),(1,2),(4,4),(2,3),(2,1)]
#sorted_list=sorted(lst,key=itemgetter(1))
lst.sort(key=lambda x:x[-1])
print(lst)

            
 