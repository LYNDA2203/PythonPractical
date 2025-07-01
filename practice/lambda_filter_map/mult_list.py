num = [2, 4, 6, 9, 11]
n = 2
print("original list: ",num)
print("Given num: ",n)
filtered_num = list(map(lambda num : num * n,num))
print("Result:")
print(' '.join(map(str,filtered_num)))