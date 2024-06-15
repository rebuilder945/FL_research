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
lst = [2,3,5,7,9,11,23]  
new_lst = [i for i in lst if is_prime(i)]  
print(new_lst)
