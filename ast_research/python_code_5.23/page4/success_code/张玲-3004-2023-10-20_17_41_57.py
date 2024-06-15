# 从键盘输入自然数构成的列表
input_list = eval(input().strip())

# 定义一个函数来判断是否为素数
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 找出输入列表中的素数并放入另外一个列表中
prime_numbers = [num for num in input_list if is_prime(num)]

# 输出素数列表
print(prime_numbers)

