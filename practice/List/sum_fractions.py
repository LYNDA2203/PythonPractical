# lst=[[18,13],[4,5]]
# fac=0
# for i,j in lst:
#     fac += i/j
    
# print(fac)
from fractions import Fraction
def sum_fraction(lst):
    fac=Fraction(0,1)
    for i,j in lst:
        fac += Fraction(i,j)   
    return round(fac)

print((sum_fraction([[36, 4], [22, 60]])))

#return round(sum(n / d for n, d in lst))