def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
lst_str = input().strip()
lst = eval(lst_str) 
prime_lst = [x for x in lst if is_prime(x)] 
print(prime_lst) 

