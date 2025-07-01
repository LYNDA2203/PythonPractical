def power_list(lst,power):
    print("original list and the powers to be calculated:",lst,power)
    power_list=list(map(pow,lst,power))
    return power_list

print("powers of the list:")
lst=[1,2,3,4,5]
power=[2,3,4,5,6]
result=power_list(lst,power)
print(result)