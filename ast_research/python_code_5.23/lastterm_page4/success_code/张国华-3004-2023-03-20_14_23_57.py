def is_prime(num):   
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
lst_str = input()
lst = eval(lst_str)
prime_lst = [num for num in lst if is_prime(num)]
print(prime_lst)
