def is_prime(n):  
    if n <= 1:  
        return False  
    if n <= 3:  
        return True  
    if n % 2 == 0 or n % 3 == 0:  
        return False  
    i = 5  
    while i * i <= n:  
        if n % i == 0 or n % (i + 2) == 0:  
            return False  
        i += 6  
    return True  
  
def filter_primes(input_list):  
    primes = []  
    for num in input_list:  
        if is_prime(num):  
            primes.append(num)  
    return primes  
a=eval(input())
print(filter_primes(a))

             
