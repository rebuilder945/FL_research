def is_prime(num):
    """判断一个数是否为素数"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(numbers):
    """在列表中找出所有的素数"""
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes

# 读取输入数据
numbers = eval(input())

# 找出所有素数并输出
primes = find_primes(numbers)
print(primes)
