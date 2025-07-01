def divisible_by_digit(start_num,end_num):
    return list(filter(lambda num: all(int(n) != 0 and num % int(n) == 0 for n in str(num)),range(start_num,end_num+1)))
result=divisible_by_digit(1,35)
print(result)