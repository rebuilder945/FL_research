def is_prime(n):  
    if n <= 1:  
        return False  
    if n == 2:  
        return True  
    if n % 2 == 0:  
        return False  
    i = 3  
    while i * i <= n:  
        if n % i == 0:  
            return False  
        i += 2  
    return True  
  
def prime_numbers(lst):  
    return [num for num in lst if is_prime(num)]  
  
# 测试样例  
input_numbers = [2,3,5,7,9,11,23]  
print(prime_numbers(input_numbers))
