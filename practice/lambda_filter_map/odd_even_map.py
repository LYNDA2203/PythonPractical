nums=[1,2,3,4,5]
odd_even=list(map(lambda x:"Even" if x % 2 == 0 else "Odd",nums))
print(odd_even)