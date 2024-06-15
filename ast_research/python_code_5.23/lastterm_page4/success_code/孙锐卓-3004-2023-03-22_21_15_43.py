def is_prime(n):
    """
    判断一个数是否为素数
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
num_list = input()
num_list = eval(num_list)
prime_list = []
for num in num_list:
    if is_prime(num):
        prime_list.append(num)
print(prime_list)

