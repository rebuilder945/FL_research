# 读入输入的列表
nums = eval(input())

# 创建一个新的列表用来存储素数
primes = []

# 遍历输入列表中的每个数字
for num in nums:
    # 如果当前数值不是素数，则跳过
    if num < 2:
        continue

    # 设置标志位，用于判断是否是素数
    is_prime = True

    # 从2开始遍历到num，如果num可以被任何一个数整除，就不是素数
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    # 如果num是素数，则把它加入到新列表中
    if is_prime:
        primes.append(num)

# 输出素数列表
print(primes)
