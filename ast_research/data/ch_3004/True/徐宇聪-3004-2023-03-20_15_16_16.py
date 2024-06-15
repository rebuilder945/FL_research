def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
lst = eval(input())
prime_lst = []
for num in lst:
    if is_prime(num):
        prime_lst.append(num)
print(prime_lst)
