def list_prime(num):
    return all(isprime(i) for i in num)
    
def isprime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n+1):
            if n % i == 0:
                return False
        return True
    
print(list_prime([0,3,4,7,9]))
print(list_prime)