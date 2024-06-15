def is_prime(num):
    """判断一个数是否为素数"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

lst = eval(input())
prime_lst = [x for x in lst if is_prime(x)]
print(prime_lst)

