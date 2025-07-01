import itertools
lst=[[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
res=list(itertools.chain(*lst)) # we are using * before that so the iterables will become [2,4,3],[1,5,6],[9],[7,9,0]==>*-->unpacking
print((res))
