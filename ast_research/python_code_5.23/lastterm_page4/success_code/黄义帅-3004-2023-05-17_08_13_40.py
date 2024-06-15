def is_prime(n):
    """
    判断一个数是否为素数
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

lst = input()
lst = eval(lst)
result = []
for num in lst:
    if is_prime(num):
        result.append(num)
print(result)


