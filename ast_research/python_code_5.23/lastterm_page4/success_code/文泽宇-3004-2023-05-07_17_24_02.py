def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = eval(input())
lst = []

for x in n:
    # 检查x是否为素数，如果是，则将x添加到列表lst中
    if is_prime(x):
        lst.append(x)

print(lst)

