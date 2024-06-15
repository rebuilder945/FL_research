def is_prime(num):
    # 判断一个数是否为素数的函数
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 从输入中获取列表
input_list = input().strip()
original_list = eval(input_list)

# 找出原始列表中的素数并放入新列表
prime_list = [num for num in original_list if is_prime(num)]

# 打印输出新列表
print(prime_list)

