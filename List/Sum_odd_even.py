def Sum_of_even_odd(lst):
    # even_num = 0
    # odd_num = 0
    # for i in lst:
    #         if i % 2 == 0:
    #             even_num += i
    #         else:
    #             odd_num += i
    # return [even_num,odd_num]
    return [sum(i for i in lst if i%2==0),sum(i for i in lst if i%2==1)]
output = Sum_of_even_odd([1,2,3,4,5,6])
print(output)