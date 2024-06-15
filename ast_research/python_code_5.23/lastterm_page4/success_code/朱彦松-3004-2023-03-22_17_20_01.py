# 【问题描述】

# 读入一个自然数构成的列表，找出其中的每一个素数，然后放入另外一个列表，并输出这个列表。
# 【输入形式】

# 按照列表的形式输入，包括方括号，元素之间用逗号分隔。
# 【输出形式】

# 直接用print输出列表
# 【样例输入】

# [2,3,5,7,9,11,23]

# 【样例输出】

# [2, 3, 5, 7, 11, 23]

# 【样例说明】

# 所有的输入数据在一行。所有的输出在一行。


# 定义一个函数判断一个数是否为素数
def is_prime(n):
  # 如果n小于2，返回False
  if n < 2:
    return False
  # 遍历从2到n的平方根之间的所有整数，如果有能整除n的，返回False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  # 否则返回True
  return True

# 读入一个自然数构成的列表
nums = eval(input())

# 创建一个空列表存放素数
primes = []

# 遍历输入的列表中的每个元素
for num in nums:
  # 如果是素数，就添加到primes列表中
  if is_prime(num):
    primes.append(num)

# 输出primes列表
print(primes)
