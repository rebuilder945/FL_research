num_list = eval(input())

# 定义函数来判断素数
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# 找出素数并放入新列表
prime_list = [num for num in num_list if is_prime(num)]

# 输出结果
print(prime_list)
