import math

def is_prime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 2
    return True

def primes(numbers):
    new_list = []
    for n in numbers:
        if is_prime(n):
            new_list.append(n)

    return new_list

print(primes([-5, -2, 3, 4, 5, 6, 7, 8, 9, 10]))


first1000 = range(1000)
print(primes(first1000))