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

# 从用户那里获取输入的列表
input_list = [int(x) for x in input().split(',')]

# 创建一个空的列表来存储素数
prime_list = []

# 遍历输入的列表，检查每个数是否为素数，如果是，添加到素数列表中
for num in input_list:
    if is_prime(num):
        prime_list.append(num)

# 输出素数列表
print(prime_list)
