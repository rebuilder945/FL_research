def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
input_list = eval(input())
prime_list = []
for num in input_list:
    if is_prime(num):
        prime_list.append(num)

# 输出素数列表
print(prime_list)

