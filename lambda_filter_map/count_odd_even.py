lst=[1, 2, 3, 5, 7, 8, 9, 10]
print(lst)
odd_even=list(map(lambda condn: len(list(filter(condn,lst))),[lambda x: x % 2 == 0,lambda x: x % 2 == 1]))
print(f"Even Numbers:",odd_even[0])
print(f"Odd Numbers:",odd_even[1])